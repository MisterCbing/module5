from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Видео "{self.title}", продолжительностью {self.duration}'

class UrTube:
    users = []
    videos = []
    current_user = None
    def __init__(self):
        pass

    def register(self, nickname, password, age):
        flag = 0
        for i in self.users:
            if nickname == i.nickname:
                print(f"Пользователь {nickname} уже существует")
                flag = 1
        if flag == 0:
            temp = User(nickname, hash(password), age)
            self.users.append(temp)
            self.current_user = temp

    def log_in(self, login, password):
        flag = 0
        for i in self.users:
            if login == i.nickname:
                if hash(password) == i.password:
                    self.current_user = i
                    break

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            flag = 0
            for j in self.videos:
                if j.title == i.title:
                    flag = 1
                    break
            if flag == 0:
                self.videos.append(i)

    def get_videos(self, word):
        res = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                res.append((i.title))
        return res

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        for i in self.videos:
            if title == i.title:
                if i.adult_mode == True:
                    if self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        break
                for t in range(1, i.duration + 1):
                    sleep(1)
                    print(t, end = ' ')
                    i.time_now += 1
                print("Конец видео")
                i.time_now = 0
                break

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)