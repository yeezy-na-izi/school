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


def zagruzit(dum):
    with open('some.pickle', 'wb') as f:
        pickle.dump(dum, f)


def download():
    with open('some.pickle', 'rb') as f:
        for_print = pickle.load(f)
        return for_print


q = download()
text = input().split()
q.append(Pickle(text[0], text[1], int(text[2]), text[3]))
zagruzit(q)
for i in download():
    print(i)
