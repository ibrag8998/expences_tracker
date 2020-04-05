from tkinter import *
from tkinter import ttk


def save():
    if product.get() == '':
        return product_entry.focus()
    elif price.get() == '':
        return price_entry.focus()
    with open(FILENAME, 'a') as f:
        f.write(SEP.join([product.get(), price.get()]) + '\n')
    product.set('')
    price.set('')


def show():
    saved.set('')
    with open(FILENAME) as f:
        for i in f.readlines():
            i = i.split(SEP)
            saved.set(saved.get() + ': '.join(i))
    ttk.Label(mainframe, textvariable=saved).grid(row=4, column=1)


FILENAME = 'products_list.txt'
SEP = ':mykey:'


root = Tk()

product = StringVar()
price = StringVar()
saved = StringVar()

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(row=0, column=0)

product_entry = ttk.Entry(mainframe, textvariable=product)
product_entry.grid(row=1, column=1)
price_entry = ttk.Entry(mainframe, textvariable=price)
price_entry.grid(row=2, column=1)

ttk.Label(mainframe, text='Product name').grid(row=1, column=0)
ttk.Label(mainframe, text='Price').grid(row=2, column=0)

ttk.Button(mainframe, text='Save', command=save).grid(row=3, column=1)
ttk.Button(mainframe, text='Show saved', command=show).grid(row=3, column=0)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    product_entry.focus()
    root.bind('<Return>', save)


if __name__ == '__main__':
    root.mainloop()
