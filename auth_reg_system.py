from typing import Optional


class User:
    """
    Используется для получения логина и пароля пользователя.
    """

    def verefication_login(self) -> str:
        """
        Проверка логина пользователя по требованиям.
        :return: str (возвращает проверенный логин)
        """
        user_login = self.request_user_data(user_login=True)
        while True:
            if len(user_login) < 3 or len(user_login) > 20:
                user_login = input('Неверное количество символов, введите логин заново: ')
            else:
                break
        return user_login

    def verefication_password(self) -> str:
        """
        Проверка пароля пользователя по требованиям.
        :return: str (возвращает проверенный пароль)
        """
        user_password = self.request_user_data()
        while True:
            if len(user_password) < 4 or len(user_password) > 32:
                user_password = input('Неверное количество символов, введите пароль заново: ')
            else:
                break
        return user_password

    def request_user_data(self, user_login=False) -> str:
        """
        Запрос логина и пароля у пользователя.
        :return: str (возвращает пароль или логин)
        """
        if user_login:
            return input('Введите логин (от 3 до 20 символов): ')
        else:
            return input('Введите пароль (от 4 до 32 символов): ')


class FileData:
    """
    Используется для чтения списка с данными пользователей или для добавления в список новых данных.
    """

    def read_file_data(self) -> list:
        """
        Открывает файл на чтение и возвращает список.
        :return: list (возвращает список для проверки)
        """
        with open('users', 'r', encoding='UTF-8') as read_file:
            return read_file.read().splitlines()

    def add_file_data(self, user_login: str, user_password: str) -> None:
        """
        Открывает файл и добавляет в него новые логин и пароль.
        :param user_login: str (проверенный логин пользователя)
        :param user_password: str (проверенный пароль пользователя)
        :return: None
        """
        with open('users', 'a', encoding='UTF-8') as add_file:
            add_file.write(f'{user_login}\n')
            add_file.write(f'{user_password}\n')


class AuthSystem:
    """
    Используется для осуществления авторизации или регистрации пользователя.
    """

    file_data = FileData()
    user = User()

    def start(self) -> None:
        """
        Осуществляет запуск логики класса.
        :return: None
        """
        while True:
            if self.run_user_action():
                break

    def authorization(self) -> Optional[bool]:
        """
        Проведение авторизации пользователя.
        :return: Optional[bool] (возвращает True если авторизация прошла успешно)
        """
        if self.user.verefication_login() not in self.file_data.read_file_data():
            answer = input(
                'Пользователя с таким логином не найдено. '
                'Хотите пройти регистрацию? Введите "да" или "нет": ')
            if answer == 'да':
                self.registration()
            else:
                print('Удачного времяпрепровождения!')
                return True
        else:
            self.user.request_user_data()
            print('Авторизация прошла успешно!')
            return True

    def registration(self) -> bool:
        """
        Проведение регистрации пользователя.
        :return: bool (возвращает True если регистрация прошла успешно)
        """
        data = self.file_data.read_file_data()
        user_login = self.user.verefication_login()
        while True:
            if user_login in data:
                print('Такой логин уже существует, придумайте новый новый: ')
                user_login = self.user.verefication_login()
            else:
                self.file_data.add_file_data(user_login, self.user.verefication_password())
                break
        print('Вы успешно зарегистрированы!')
        return True

    def auth(self, action: int) -> bool:
        """
        Запуск авторизации или регистрации в зависимости от выбора пользователя.
        :param action: int (выбранное действие пользователя)
        :return: bool (возвращает запуск авторизации или регистрации)
        """
        if action == 1:
            return self.authorization()
        return self.registration()

    def run_user_action(self) -> bool:
        """
        Проверка действия пользователя.
        :return: bool (возвращает запуск auth с выбранным действием)
        """
        action = self.select_action()
        if action == 1 or action == 2:
            return self.auth(action)
        else:
            print('Неверное действие! Выберите заново: ')

    def select_action(self) -> int:
        """
        Запрос на действие пользователя.
        :return: int (возвращает действие выбранное пользователем)
        """
        return int(input(
            'Приветствуем Вас в нашей системе! '
            'Вы хотите пройти авторизацию(1) или зарегистрироваться(2)? '
            'Введите "1" или "2": '))


if __name__ == '__main__':
    artem = AuthSystem()
    artem.start()
