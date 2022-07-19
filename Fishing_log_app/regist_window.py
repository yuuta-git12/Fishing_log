import tkinter
import tkinter as tk
from tkinter import ttk
from Fishing_log_app import pgsql_method as pgsql


def window1():
    win1 = tk.Tk()
    win1.title('釣果入力フォーム')
    win1.geometry('650x350')

    frame1 = tkinter.Frame(win1)
    label1 = ttk.Label(frame1, text='釣果入力フォーム', font=("Times New Roman", 30))
    label1.pack(pady=20)

    frame2 = tkinter.Frame(win1)
    tk.Label(frame2, text='魚を釣った日時：', font=("Times New Roman", 15)).grid(row=0, column=0, padx=5, pady=5)

    date_year = tk.Entry(frame2, width=10, font=('', 15), relief="ridge", bd=2)
    date_year.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame2, text='年', font=("Times New Roman", 15)).grid(row=0, column=2, padx=5, pady=5)

    date_month = tk.Entry(frame2, width=10, font=('', 15), relief="ridge", bd=2)
    date_month.grid(row=0, column=3, padx=5, pady=5)
    tk.Label(frame2, text='月', font=("Times New Roman", 15)).grid(row=0, column=4, padx=5, pady=5)

    date_day = tk.Entry(frame2, width=10, font=('', 15), relief="ridge", bd=2)
    date_day.grid(row=0, column=5, padx=5, pady=5)
    tk.Label(frame2, text='日', font=("Times New Roman", 15)).grid(row=0, column=6, padx=5, pady=5)

    tk.Label(frame2, text='釣った魚の名前：', font=("Times New Roman", 15)).grid(row=1, column=0, padx=5, pady=5)
    fish_name = tk.Entry(frame2, width=10, font=('', 15), relief="ridge", bd=2)
    fish_name.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame2, text='釣った魚の大きさ(cm)：', font=("Times New Roman", 15)).grid(row=2, column=0, padx=5, pady=5)
    fish_size = tk.Entry(frame2, width=10, font=('', 15), relief="ridge", bd=2)
    fish_size.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame2, text='釣った魚の重さ(kg)：', font=("Times New Roman", 15)).grid(row=3, column=0, padx=5, pady=5)
    fish_weight = tk.Entry(frame2, width=10, font=('', 15), relief="ridge", bd=2)
    fish_weight.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame2, text='魚を釣った場所：', font=("Times New Roman", 15)).grid(row=4, column=0, padx=5, pady=5)
    fish_place = tk.Entry(frame2, width=10, font=('', 15), relief="ridge", bd=2)
    fish_place.grid(row=4, column=1, padx=5, pady=5)

    # 入力フォームに入れた文字を変数に格納し、DBに登録
    def btn_click():
        year = date_year.get()
        month = date_month.get()
        day = date_day.get()
        date = year + "-" + month + "-" + day

        name = fish_name.get()
        size = fish_size.get()
        weight = fish_weight.get()
        place = fish_place.get()

        pgsql.form_insert(name, size, weight, place, date)
        win1.destroy()

    button1 = tk.Button(frame1, text='登録', command=btn_click)
    button1.pack(pady=10)

    frame1.pack()
    frame2.pack()

    win1.mainloop()