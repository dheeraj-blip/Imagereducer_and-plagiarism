import tkinter as tk
import subprocess

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.configure(bg='lightblue')
        self.default_font = ("Arial", 20)
        self.create_widgets()

    def create_widgets(self):
        window_size = 400
        self.root.geometry(f"{window_size}x{window_size}")

        frame = tk.Frame(self.root, bg='lightblue')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button_image_resizer = tk.Button(frame, text="Image Resizer", command=self.launch_image_resizer, font=self.default_font, bg='white')
        self.button_image_resizer.pack(pady=20)

        self.button_plagiarism_checker = tk.Button(frame, text="Plagiarism Checker", command=self.launch_plagiarism_checker, font=self.default_font, bg='white')
        self.button_plagiarism_checker.pack(pady=20)

    def launch_image_resizer(self):
        subprocess.run(["python", "Image.py"], shell=True)

    def launch_plagiarism_checker(self):
        subprocess.run(["python", "Plagarism.py"], shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()
