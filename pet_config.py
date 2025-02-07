import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk, ImageDraw
import os
from pets_data import pets

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

def update_speed_label(value):
    return f"Скорость пета: {value}"

def select_pet():
    def start_pet(gif_path, speed):
        root.destroy()
        from pet_game import Pet
        Pet(gif_path, speed)

    def open_link(event):
        webbrowser.open('https://github.com/Showtimeeee')

    def open_purchase_link():
        webbrowser.open('https://t.me/PetsShowBot')

    root = tk.Tk()
    root.title("Select Pet")
    root.geometry("300x600")
    root.resizable(False, False)
    root.configure(bg='#1e1e2f')  # Тёмный фон для современного вида

    # Установка пользовательской иконки
    root.iconbitmap('0465.ico')  # Укажите путь к вашей иконке

    # Центрирование окна
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (300 // 2)
    y = (screen_height // 2) - (600 // 2)
    root.geometry(f'300x600+{x}+{y}')

    # Заголовок
    label = tk.Label(root,
                     text="Выбери питомца!",
                     font=('Helvetica', 20, 'bold'),
                     bg='#1e1e2f',
                     fg='#ffffff')
    label.pack(pady=5)

    # Ползунок для управления скоростью
    speed_label = tk.Label(root,
                           text="Скорость пета: 10",
                           font=('Helvetica', 8),
                           bg='#1e1e2f',
                           fg='#ffffff')
    speed_label.pack(pady=2)

    speed_scale = tk.Scale(root,
                           from_=1, to=50,
                           orient=tk.HORIZONTAL,
                           bg='#1e1e2f',
                           fg='#ffffff',
                           highlightthickness=0,
                           troughcolor='#bf13bf',  # Фиолетовый цвет ползункайй
                           activebackground='#800080',
                           length=100,
                           showvalue=0,  # Убираем число, которое бегает за ползунком
                           command=lambda value: speed_label.config(text=update_speed_label(value)))
    speed_scale.set(10)  # Начальная скорость
    speed_scale.pack(pady=5)

    # Создаем фрейм для кнопок
    button_frame = tk.Frame(root, bg='#1e1e2f')
    button_frame.pack(pady=5)

    # Добавляем кнопки в фрейм
    for pet_name, gif_path in pets:
        canvas = tk.Canvas(button_frame, width=150, height=40, bg='#1e1e2f', highlightthickness=0)
        rounded_rect = create_rounded_rectangle(canvas, 5, 5, 145, 35, 10, fill="#bf13bf", outline="")  # Фиолетовый цвет
        text_id = canvas.create_text(75, 20, text=pet_name, font=('Helvetica', 12, 'bold'), fill='#ffffff')
        canvas.pack(pady=5)

        # Привязываем события наведения и нажатия
        if pet_name == "Приобрести":
            canvas.tag_bind(rounded_rect, '<Button-1>', lambda event: open_purchase_link())
            canvas.tag_bind(text_id, '<Button-1>', lambda event: open_purchase_link())
        else:
            canvas.tag_bind(rounded_rect, '<Button-1>', lambda event, path=gif_path: start_pet(path, speed_scale.get()))
            canvas.tag_bind(text_id, '<Button-1>', lambda event, path=gif_path: start_pet(path, speed_scale.get()))

        canvas.tag_bind(rounded_rect, '<Enter>', lambda event, c=canvas, r=rounded_rect, t=text_id: on_enter(c, r, t))
        canvas.tag_bind(rounded_rect, '<Leave>', lambda event, c=canvas, r=rounded_rect, t=text_id: on_leave(c, r, t))
        canvas.tag_bind(text_id, '<Enter>', lambda event, c=canvas, r=rounded_rect, t=text_id: on_enter(c, r, t))
        canvas.tag_bind(text_id, '<Leave>', lambda event, c=canvas, r=rounded_rect, t=text_id: on_leave(c, r, t))

    # Текст в нижнем углу слева
    footer_label_left = tk.Label(root,
                                  text="v.siv",
                                  font=('Helvetica', 10),
                                  bg='#1e1e2f',
                                  fg='#ffffff',
                                  cursor="hand2")
    footer_label_left.place(relx=0.0, rely=1.0, anchor='sw', x=10, y=-10)
    footer_label_left.bind("<Button-1>", open_link)

    # Текст в нижнем углу справа
    footer_label_right = tk.Label(root,
                                   text="v1.9",
                                   font=('Helvetica', 10),
                                   bg='#1e1e2f',
                                   fg='#ffffff',
                                   cursor="hand2")
    footer_label_right.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    root.mainloop()

def on_enter(canvas, rect, text):
    canvas.itemconfig(rect, fill="#4B0082")  # Темно-фиолетовый цвет при наведении
    canvas.itemconfig(text, fill="#ffffff")

def on_leave(canvas, rect, text):
    canvas.itemconfig(rect, fill="#bf13bf")  # Возвращаем фиолетовый цвет
    canvas.itemconfig(text, fill="#ffffff")

if __name__ == "__main__":
    select_pet()
