from tkinter import *


class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To - D0 - List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='TO - DO - List.app', font="arial, 25 bold", width=10, bd=5, bg='light blue',
                           fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', font="arial, 18", width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', font="arial, 18", width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=8, bd=5, width=22, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        # ********************* Add Task ******************#

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as files:
                files.write(content)
                files.seek(0)
                files.close()
            self.text.delete(1.0, END)

        # ****************** Delete **************** #

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)
            with open('dueData.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        # ************ due ************ #

        def due():
            with open("dueData.txt", "a") as files:
                due_ = self.main_text.curselection()
                look = self.main_text.get(due_)
                content = self.text.get(1.0, END)
                temp = str((''.join(look)) + "---" + content)
                files.write(temp)
                files.seek(0)
                files.close()
            self.text.delete(1.0, END)

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        # ************** show due ************** #

        def show():
            with open('dueData.txt', 'r') as file:
                read = file.readlines()
                for i in read:
                    ready = i.split()
                    self.main_text.insert(END, ready)
                file.close()

        self.button = Button(self.root, text="ADD", font='serif, 20 bold italic', width=10, bd=5, bg='light green',
                             fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="DELETE", font='serif, 20 bold italic', width=10, bd=5, bg='red',
                              fg='black', command=delete)
        self.button2.place(x=30, y=340)

        self.button3 = Button(self.root, text="SET DUE", font='serif, 20 bold italic', width=10, bd=5, bg='violet',
                              fg='black', command=due)
        self.button3.place(x=30, y=260)

        self.button4 = Button(self.root, text="DUE", font='serif, 15 bold italic', height=0, width=5, bd=1, bg='violet',
                              fg='black', command=show)
        self.button4.place(x=500, y=54)


def main():
    root = Tk()
    todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()

