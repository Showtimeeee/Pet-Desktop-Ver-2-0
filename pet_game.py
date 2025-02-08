import tkinter as tk
import time
from PIL import Image, ImageTk
import keyboard
import random
import os

class Pet:
    def __init__(self, gif_path, speed):
        self.window = tk.Tk()
        self.gif_path = gif_path
        self.speed = speed  # Начальная скорость обновления

        # Открываем GIF с помощью PIL, чтобы получить количество кадров
        with Image.open(self.gif_path) as img:
            self.num_frames = img.n_frames

        # Код ниже генерирует строку для каждого кадра в GIF
        self.moveleft = []
        self.moveright = []

        for i in range(self.num_frames):
            frame = Image.open(self.gif_path)
            frame.seek(i)
            self.moveright.append(ImageTk.PhotoImage(frame))
            self.moveleft.append(ImageTk.PhotoImage(frame.transpose(Image.FLIP_LEFT_RIGHT)))

        self.frame_index = 0  # Начальный кадр
        self.img = self.moveright[self.frame_index]  # Начальное направление GIF
        self.timestamp = time.time()
        self.window.config(background='black')
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.overrideredirect(True)  # Делает окно без рамки
        self.window.attributes('-topmost', True)  # Размещает окно поверх всех остальных
        self.label = tk.Label(self.window, bd=0, bg='black')  # Создает метку в качестве контейнера для GIF

        # Начальные координаты
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.x = random.randint(0, screen_width - 128)
        self.y = random.randint(0, screen_height - 128)
        self.window.geometry('128x128+{}+{}'.format(str(self.x), str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(0, self.update)
        self.dir_x = random.choice([-1, 1])  # Начальное направление по оси X
        self.dir_y = random.choice([-1, 1])  # Начальное направление по оси Y

        # Привязываем клавишу "q" к функции закрытия программы
        keyboard.add_hotkey('q', self.quit_program)

        # Привязываем события мыши для изменения скорости
        self.window.bind('<Enter>', self.speed_up)
        self.window.bind('<Leave>', self.slow_down)

        self.window.mainloop()

    def changetime(self, direction):
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            self.frame_index = (self.frame_index + 1) % self.num_frames  # Скорость смены кадров
            self.img = direction[self.frame_index]

    def changedir(self):
        self.dir_x = -(self.dir_x)
        self.dir_y = -(self.dir_y)

    def go(self):
        self.x = self.x + self.dir_x
        self.y = self.y + self.dir_y
        if self.dir_x < 0:
            direction = self.moveleft
        else:
            direction = self.moveright
        self.changetime(direction)

    def update(self):
        self.go()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Проверяем, является ли питомец "Мопс", "Пикачу", "Пингвин" или "Котик"
        pet_name = os.path.basename(self.gif_path)
        if pet_name in ['dasad.gif', '6vw5.gif', '6no.gif']:
            # Ограничиваем движение по нижней части экрана
            if self.x <= 0 or self.x >= screen_width - 128:
                self.dir_x = -(self.dir_x)
            if self.y <= screen_height - 168 or self.y >= screen_height - 48:
                self.dir_y = -(self.dir_y)
            # Удерживаем питомца в нижней части экрана
            self.y = screen_height - 128
        else:
            # Полет по экрану для летающих петов
            if self.x <= 0 or self.x >= screen_width - 128:
                self.dir_x = -(self.dir_x)
            if self.y <= 0 or self.y >= screen_height - 128:
                self.dir_y = -(self.dir_y)

        self.window.geometry('128x128+{}+{}'.format(str(self.x), str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(self.speed, self.update)  # Скорость обновленияй
        self.window.lift()

    def quit_program(self):
        self.window.destroy()

    def speed_up(self, event):
        self.speed = 5  # Увеличиваем скорость обновления

    def slow_down(self, event):
        self.speed = 10  # Возвращаем нормальную скорость обновления
