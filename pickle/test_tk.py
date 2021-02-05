import tkinter as tk
import pickle


class Pickle:
    def __init__(self, surname, name, phone, date):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.date = date

    def __str__(self):
        x = f'{self.surname} {self.name} {self.phone} {self.date}'
        return x


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.surname = tk.StringVar()
        self.name = tk.StringVar()
        self.number = tk.IntVar()
        self.date = tk.StringVar()
        self.name_text = tk.Label(self, text='Имя', bg='red')
        self.surname_text = tk.Label(self, text='Фамилиия', bg='red')
        self.number_text = tk.Label(self, text='Номер телефона', bg='red')
        self.date_text = tk.Label(self, text='Дата рождения(через точку)', bg='red')
        self.name_label = tk.Entry(self, textvariable=self.name)
        self.surname_label = tk.Entry(self, textvariable=self.surname)
        self.number_label = tk.Entry(self, textvariable=self.number)
        self.date_label = tk.Entry(self, textvariable=self.date)
        self.save_button = tk.Button(self, text='Save', command=self.sosi_jopu)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.save_button.pack(side='bottom')
        self.date_label.pack(side='bottom')
        self.date_text.pack(side='bottom')
        self.number_label.pack(side='bottom')
        self.number_text.pack(side='bottom')
        self.surname_label.pack(side='bottom')
        self.surname_text.pack(side='bottom')
        self.name_label.pack(side='bottom')
        self.name_text.pack(side='bottom')

    def __str__(self):
        x = f'{self.surname} {self.name} {self.name} {self.date}'
        return x

    def zagruzit(self, dum):
        with open('some.pickle', 'wb') as f:
            pickle.dump(dum, f)

    def download(self):
        with open('some.pickle', 'rb') as f:
            for_print = pickle.load(f)
            return for_print

    def sosi_jopu(self):
        if self.name.get() and self.surname.get() and self.number.get() and self.date.get():
            self.download().append(Pickle(self.surname.get(), self.name.get(), self.number.get(), self.date.get()))
        for i in self.download():
            print(i)


def sort_by(list_friends):
    return sorted(list_friends, key=lambda x: int(x.date.split('.')[2] + x.date.split('.')[1] + x.date.split('.')[0]))


root = tk.Tk()
root.title('Спецкурс')
root.configure(bg='blue')
app = Application(master=root)
app.mainloop()
