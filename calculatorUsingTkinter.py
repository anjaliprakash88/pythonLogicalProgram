import tkinter as tk
class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("calculator")
        self.result = tk.StringVar()
        self.result.set("0")
        self.entry = tk.Entry(self.root, width=25, textvariable=self.result, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)
        self.buttons = ["7", "8", "9", "+",
                        "4", "5", "6", "-",
                        "1", "2", "3", "*",
                        "c", "0", "=", "/"]
        self.create_buttons()
        self.root.mainloop()
    def create_buttons(self):
       row = 1
       col = 0
       for button in self.buttons:
           command = lambda x = button: self.button_click(x)
           tk.Button(self.root, text=button, width=3, height=3, command=command).grid(row=row, column=col)
           col = col + 1
           if col > 3:
               col = 0
               row = row + 1
    def button_click(self, char):
       if char == "c":
           self.result.set("0")
       elif char == "=":
           try:
               result = str(eval(self.result.get()))
           except:
               result = "error"
           self.result.set(result)
       else:
           if self.result.get() == "0":
               self.result.set(char)
           else:
               self.result.set(self.result.get() + char)

Calculator()

