import tkinter


class Calculator(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.width_button = self.height_button = 50
        self.y0 = 50 # initial coordinate x
        self.x0 = 25 # initial coordinate y
        self.button = ["C", "CE", "%", "/", "7", "8", "9", "*", "4", "5",
                       "6", "-", "1", "2", "3", "+", "+/-", "0", ",", "="]
        self.field = tkinter.Text(width=600, height=2)
        self.master = master
        self.pack()
        self.create_window()

    def create_window(self):
        self.field.pack()
        counter = 0
        for i in range(5):
            for j in range(4):
                self.button_name = "button_" + self.button[counter]
                self.button_name = tkinter.Button(text=self.button[counter]).place(
                    x=self.x0 + j * (self.width_button + self.x0),
                    y=self.y0 + i * (self.height_button + self.x0),
                    width=50, height=50)
                counter += 1


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('325x425')
    app = Calculator(master=root)
    app.mainloop()
