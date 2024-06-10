class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return nickname

class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user = ''
    def __init__(self):
        pass
    # def __init__(self, users, videos, current_user):
    #     self.users = []
    #     self.videos = []
    #     self.current_user = ''

    def register(self, nickname, password, age):
        self.users.append(User(nickname, hash(password), age))
    # def log_in(login, password):
    #     if login in self.users:
            

basa = UrTube
basa.register(basa,'John',1234, 38)
print(basa.users)