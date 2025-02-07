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