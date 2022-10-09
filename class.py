from typing import Optional


class User:
    """
    Используется для получения логина и пароля пользователя.
    """

    def verefication_login(self) -> str:
        """
        Проверка логина пользователя по требованиям.!!!
        :return: str (возвращает проверенный логин)
        """
        user_login = self.request_user_login()
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
        user_password = self.request_user_password()
        while True:
            if len(user_password) < 4 or len(user_password) > 32:
                login = input('Неверное количество символов, введите пароль заново: ')
            else:
                break
        return user_password

    def request_user_login(self) -> str:
        """
        Завпрос логина у пользователя.
        :return: str (возвращает введенный логин)
        """
        return input('Введите логин (от 3 до 20 символов): ')

    def request_user_password(self) -> str:
        """
        Запрос пароля у пользователя.
        :return: str (возвращает введенный пароль)
        """
        return input('Введите пароль (от 4 до 32 символов): ')


class FileData:
    """
    Используется для чтения списка с логинами и паролями пользователей или для добавления в список новых логинов и паролей.
    """

    def read_file_data(self) -> list:
        """
        Открывает файл на чтение и возвращает список.
        :return: list (возвращает список список для проверки)
        """
        with open('users', 'r', encoding='UTF-8') as read_file:
            return read_file.read().splitlines()

    def add_file_data(self, user_login: str, user_password: str) -> None:
        """
        Открывает файл и добавляет в него новые логин и пароль.
        :param user_login: str (проверенный логин пользователя)
        :param user_password: str (провереннный пароль пользователя)
        :return: None
        """
        with open('users', 'a', encoding='UTF-8') as add_file:
            add_file.write(user_login + '\n')
            add_file.write(user_password + '\n')


class AuthSystem:
    """
    Используется для осуществления авторизации или регистрации пользователя.
    """
    file_data = FileData()
    user = User()

    def start(self) -> None:
        """
        Осуществляет запуск скрипта.
        :return: None
        """
        while True:
            if self.run_user_action():
                break

    def authorization(self) -> Optional[bool]:
        """
        Проведение авторизации пользователя.
        :return: Optional[bool] (возвращает введенный логин)
        """
        if self.user.verefication_login() not in self.file_data.read_file_data():
            answer = input('Пользователя с таким логином не найдено. Хотите пройти регистрацию? Введите "да" или "нет": ')
            if answer == 'да':
                self.registration()
            else:
                print('Удачного времяпрепровождения!')
                return True
        else:
            self.user.request_user_password()
            print('Авторизация прошла успешно!')
            return True

    def registration(self) -> bool:
        """
        Проведение регистрации пользователя.
        :return:
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
        :return:
        """
        if action == 1:
            return self.authorization()
        else:
            return self.registration()

    def run_user_action(self) -> bool:
        """
        Проверка действия пользователя.
        :return:
        """
        action = self.select_action()
        if action == 1 or action == 2:
            return self.auth(action)
        else:
            print('Неверное действие! Выберите заново: ')

    def select_action(self) -> int:
        """
        Запрос на действие пользователя.
        :return:
        """
        return int(input('Приветствуем Вас в нашей системе! Вы хотите пройти авторизацию(1) или зарегистрироваться(2)? Введите "1" или "2": '))



artem = AuthSystem()
artem.start()
