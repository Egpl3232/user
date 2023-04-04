import json

def greet_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""

    filename = 'username.json'

    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_stored_username():
    """Запрашивает новое имя пользователя."""

    username = input("Как вас зовут? ")

    filename = 'username.json'

    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
        return username

def greet_user():
    """Приветствует пользователя по имени."""

    user = get_stored_username()

    if user:
        print("С возвращением, " + user.title())
    else:
        username = get_stored_username()
        print("Мы будем помнить тебя, когда ты вернешься, " + username.title())

greet_user()