import tkinter as tk
from tkinter import ttk
from Fishing_log_app import pgsql_method as pgsql
from Fishing_log_app import regist_window


def main():
    # 列の識別名
    column = ('Fishing_Date','Fish_Name', 'Fish_Weight', 'Fish_Scale', 'Fishing_Place')

    root = tk.Tk()
    root.title('釣果記録テーブル')
    root.geometry('1000x500')

    frame1 = tk.Frame(root)
    label1 = tk.Label(frame1, text='釣果記録テーブル', font=("Arial", 25))
    label1.pack()

    frame2 = tk.Frame(root)

    frame3 = tk.Frame(root)
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 20))
    style.configure("Treeview", font=("Arial", 15))

    # Treeviewの生成
    # 一度に表示できる件数は50件　height=20
    tree = ttk.Treeview(frame3, height=20, columns=column, show='headings')

    # 列の指定(テキストの配置:anchor,列名:id,minwidth:列の最小幅(最小20px),
    # 列幅の変更可否:stretch(TrueまたはFalse),列の横幅:width(デフォルト200px))
    tree.column('#0', width=0, stretch=0)
    tree.column('Fishing_Date', anchor='center', stretch=1)
    tree.column('Fish_Name', anchor='center', stretch=1)
    tree.column('Fish_Weight', anchor='center', stretch=1)
    tree.column('Fish_Scale', anchor='center', stretch=1)
    tree.column('Fishing_Place', anchor='center', stretch=1)

    # 列の見出し設定
    tree.heading('#0', text='')
    tree.heading('Fishing_Date', text='釣った日時', anchor='center')
    tree.heading('Fish_Name', text='魚の名前', anchor='center')
    tree.heading('Fish_Weight', text='魚の重さ(kg)', anchor='center')
    tree.heading('Fish_Scale', text='魚の大きさ(cm)', anchor='center')
    tree.heading('Fishing_Place', text='釣った場所', anchor='center')


    def btn1_click():
        regist_window.window1()


    # postgreSQLから釣果情報を取得
    def btn2_click():
        # 更新ボタンクリック時にTreeviewに表示されている値を全て削除
        # その後、再度DBから釣果情報を取得
        for s in tree.get_children():
            tree.delete(s)
        list_sql, t = pgsql.select_all()
        for i in range(0,t):
            tree.insert(parent='', index='end', values=(list_sql[i][5], list_sql[i][1], list_sql[i][2], list_sql[i][3], list_sql[i][4]))


    button1 = tk.Button(frame2, text='登録', command=lambda:btn1_click())
    button1.grid(row=1,column=0,padx=5, pady=5)

    button2 = tk.Button(frame2, text='更新', command=lambda:btn2_click())
    button2.grid(row=1,column=1,padx=5, pady=5)

    # ウィジェットの配置
    frame1.pack()
    frame2.pack()
    frame3.pack()
    tree.pack(padx=10, pady=10, fill=tk.BOTH)

    root.mainloop()

