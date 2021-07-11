import tkinter as tk

def answer_win():
    def clozed_win():
        win_first.quit()
        win_second.quit()
    win_second = tk.Tk()
    win_second.title('Результат')
    win_second.geometry('400x200+350+300')
    long = long_entry.get()
    for i in range(3):
        for j in range(14):
            label_2 = tk.Label(win_second, text=' ').grid(row=i, column=j)
    label_win_second = tk.Label(win_second, text=f'Ваш рост {long} см\n)))', font=('Arial', 13, 'normal')).grid(row=4, column=10)
    win_second.columnconfigure(15, minsize=70)
    btn_second = tk.Button(win_second, text='Ок', command=clozed_win).grid(row=4, column=15, stick='we')
    win_second.mainloop()

win_first = tk.Tk()
win_first.title('Калькулятор роста')
win_first.geometry('400x200+300+250')

for i in range(3):
    for j in range(9):
        label = tk.Label(win_first, text=' ').grid(row=i, column=j)

long_label = tk.Label(win_first, text='Введите Ваш рост:', font=('Arial', 12, 'normal')).grid(row=4, column=0)
long_entry = tk.Entry(win_first)
long_entry.grid(row=4, column=7)
btn_new_win = tk.Button(win_first, text='Дальше', command=answer_win).grid(row=8, column=10)

win_first.mainloop()