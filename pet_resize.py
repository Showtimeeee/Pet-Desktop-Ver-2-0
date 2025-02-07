import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk, ImageDraw
import keyboard
import random
import webbrowser

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
        if self.x <= 0 or self.x >= screen_width - 128:
            self.dir_x = -(self.dir_x)
        if self.y <= 0 or self.y >= screen_height - 128:
            self.dir_y = -(self.dir_y)
        self.window.geometry('128x128+{}+{}'.format(str(self.x), str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(self.speed, self.update)  # Скорость обновления
        self.window.lift()

    def quit_program(self):
        self.window.destroy()

    def speed_up(self, event):
        self.speed = 5  # Увеличиваем скорость обновления

    def slow_down(self, event):
        self.speed = 10  # Возвращаем нормальную скорость обновления

def create_rounded_rectangle(width, height, corner_radius, fill_color):
    # Создаем новое изображение с прозрачным фоном
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Рисуем закругленный прямоугольник
    draw.rounded_rectangle((0, 0, width, height), corner_radius, fill=fill_color)

    return image

def select_pet():
    def start_pet(gif_path, speed):
        root.destroy()
        Pet(gif_path, speed)

    def open_link(event):
        webbrowser.open('https://github.com/Showtimeeee')

    root = tk.Tk()
    root.title("Select Pet")
    root.geometry("900x300")
    root.resizable(False, False)
    root.configure(bg='#1e1e2f')  # Тёмный фон для современного вида

    # Установка пользовательской иконки
    root.iconbitmap('0465.ico')  # Укажите путь к вашей иконке

    # Центрирование окна
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (900 // 2)
    y = (screen_height // 2) - (300 // 2)
    root.geometry(f'900x300+{x}+{y}')

    # Стилизация кнопок
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton",
                    padding=5,
                    relief="flat",
                    background="#ff6f61",
                    foreground="#ffffff",
                    font=('Helvetica', 10, 'bold'),
                    borderwidth=0,
                    focuscolor="#ff6f61",
                    focusthickness=2,
                    bordercolor="#ff6f61")
    style.map("TButton",
              background=[("active", "#ff4a40")],
              foreground=[("active", "#ffffff")])

    # Заголовок
    label = tk.Label(root,
                     text="Выбери питомца!",
                     font=('Helvetica', 20, 'bold'),
                     bg='#1e1e2f',
                     fg='#ffffff')
    label.pack(pady=20)

    # Ползунок для управления скоростью
    speed_label = tk.Label(root,
                           text="Скорость пета:",
                           font=('Helvetica', 10),
                           bg='#1e1e2f',
                           fg='#ffffff')
    speed_label.pack(pady=5)

    speed_scale = tk.Scale(root,
                           from_=1, to=50,
                           orient=tk.HORIZONTAL,
                           bg='#1e1e2f',
                           fg='#ffffff',
                           highlightthickness=0,
                           troughcolor='#ff6f61',
                           activebackground='#ff4a40',
                           length=200)
    speed_scale.set(10)  # Начальная скорость
    speed_scale.pack(pady=5)

    # Кнопки выбора питомца
    pets = [
        ("Мопс", 'dasad.gif'),
        ("Пингвин", 'Z5cP.gif'),
        ("Пикачу", '28ei.gif'),
        ("Котик", '6no.gif'),
        ("Гомер", '6md.gif'),
        ("НЛО", 'Vp3M.gif'),
        ("Феникс", 'ARm.gif')
    ]

    # Создаем фрейм для кнопок
    button_frame = tk.Frame(root, bg='#1e1e2f')
    button_frame.pack(pady=10)

    # Добавляем кнопки в фрейм
    for pet_name, gif_path in pets:
        # Создаем закругленный прямоугольник для фона кнопки
        button_image = create_rounded_rectangle(100, 30, 10, "#ff6f61")
        button_photo = ImageTk.PhotoImage(button_image)

        btn = ttk.Button(button_frame,
                          text=pet_name,
                          command=lambda path=gif_path: start_pet(path, speed_scale.get()),
                          image=button_photo,
                          compound="center",
                          style="TButton")
        btn.image = button_photo  # Сохраняем ссылку на изображение
        btn.pack(side=tk.LEFT, padx=5, pady=5)

    # Текст в нижнем углу слева
    footer_label_left = tk.Label(root,
                                    text="v.siv",
                                    font=('Helvetica', 10),
                                    bg='#1e1e2f',
                                    fg='#ffffff',
                                    cursor="hand2")
    footer_label_left.place(relx=0.0, rely=1.0, anchor='sw', x=10, y=-10)
    footer_label_left.bind("<Button-1>", open_link)

    # Текст в нижнем углу справаqqq
    footer_label_right = tk.Label(root,
                                    text="v1.9",
                                    font=('Helvetica', 10),
                                    bg='#1e1e2f',
                                    fg='#ffffff',
                                    cursor="hand2")
    footer_label_right.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    root.mainloop()

select_pet()
