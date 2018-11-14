from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, name, surname, email, password, age, gender):
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password.encode()
        self.age = int(age)
        self.gender = gender
        print("User object created")

    # A method to get user id from DB might be needed like such. (will be implemented in SQL.)
    # @login.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))
   


class Music:
    def __init__(self, name, genre, duration_in_minutes, singer, year):
        self.name= name
        self.genre = genre
        self.duration_in_minutes = duration_in_minutes
        self.singer = singer
        self.year = year
        print("Music object created")


class Movie:
    def __init__(self, title, year, duration_in_minutes, director, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.duration_in_minutes = duration_in_minutes
        self.director = director
        print("Movie object created")