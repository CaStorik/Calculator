import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both")

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                if text == "":
                    continue
                btn = tk.Button(
                    frame, text=text, font=("Arial", 16),
                    command=lambda t=text: self.on_click(t)
                )
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            frame.grid_rowconfigure(i, weight=1)

    def on_click(self, char):
        if char == "C":
         self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
             self.expression = str(eval(self.expression))
            except Exception:
             self.expression = "Ошибка"
        else:
            self.expression += char
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
d

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
    