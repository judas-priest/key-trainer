import tkinter as tk
import random

class KeyTrainer:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='black')
        self.root.title("KeY Trainer")

        # Текстовое поле с перечнем клавиш для нажатий
        self.sequence_text = tk.Text(root, font=("SF Pro Rounded", 24), height=1, width=6,
                                      borderwidth=0, highlightthickness=0,
                                      bg='black', fg='white')
        self.sequence_text.config(state=tk.DISABLED)
        self.sequence_text.tag_configure("center", justify='center')
        self.sequence_text.insert("1.0", "text")
        self.sequence_text.tag_add("center", "1.0", "end")
        self.sequence_text.pack()


        self.root.bind('<KeyPress>', self.check_input)

        # Сообщение об ошибке
        self.result_label = tk.Label(root, text="", font=("SF Pro Rounded", 24), bg='black', fg='white')
        self.result_label.pack()

        # Перечень клавиш в последовательности
        self.keys = ['W', 'A', 'S', 'D', '⌃', '⇧']
        self.sequence = []
        self.current_index = 0

        self.generate_sequence()

        self.error = False

    def clear_result(self):
        if self.error == True:
            self.result_label.config(text="")

    def generate_sequence(self):
        self.sequence = random.choices(self.keys, k=3)
        self.current_index = 0
        self.update_sequence_display()

    def update_sequence_display(self):
        self.sequence_text.config(state=tk.NORMAL)
        self.sequence_text.delete(1.0, tk.END)
        for i, key in enumerate(self.sequence):
            if i < self.current_index:
                self.sequence_text.tag_configure("bold_color", font=("SF Pro Rounded", 24, "bold"), foreground="green")
                self.sequence_text.insert(tk.END, key + " ", "bold_color")
            else:
                self.sequence_text.insert(tk.END, key + " ")
        #self.sequence_text.tag_configure("bold", font=("SF Pro Rounded", 24, "bold"))
        self.sequence_text.config(state=tk.DISABLED)

    def check_input(self, event):
        key_pressed = event.keysym

        if key_pressed == 'Control_L':
            key_pressed = '⌃'
        elif key_pressed == 'Shift_L':
            key_pressed = '⇧'

        if key_pressed.upper() == self.sequence[self.current_index].upper():
            self.current_index += 1
            self.update_sequence_display()
            if self.current_index == len(self.sequence):
                self.error = False
                self.result_label.config(text="")
                #self.result_label.config(text="Верно!", fg="green")
                self.generate_sequence()
        else:
            self.error = True
            self.result_label.config(text="Ошибка!", fg="red")
            self.current_index = 0
            self.update_sequence_display()
            #self.root.after(3000, self.clear_result)
        print(key_pressed)

if __name__ == "__main__":
    root = tk.Tk()
    trainer = KeyTrainer(root)
    root.geometry("256x144")
    root.mainloop()
