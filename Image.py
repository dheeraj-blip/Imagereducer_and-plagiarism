import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='lightblue')
        self.default_font = ("Arial", 20)
        self.root.title("Image Resizer")

        self.create_widgets()

    def create_widgets(self):
        window_height = 550
        window_width = 800
        self.root.geometry(f"{window_width}x{window_height}")

        frame = tk.Frame(self.root, bg='lightblue')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label_path = tk.Label(frame, text="Enter Image Path:", font=self.default_font, bg='lightblue')
        self.label_path.pack()

        self.entry_path = tk.Entry(frame, width=40, font=("Arial", 16), justify='center')
        self.entry_path.pack()

        self.button_browse = tk.Button(frame, text="Browse", command=self.browse_image, font=self.default_font, bg='white')
        self.button_browse.pack(pady=10)

        self.label_path = tk.Label(frame, text="", font=self.default_font, bg='lightblue')
        self.label_path.pack()

        self.label_scale = tk.Label(frame, text="Enter Scale (e.g., 0.5 for 50% reduction):", font=self.default_font, bg='lightblue')
        self.label_scale.pack()

        self.entry_scale = tk.Entry(frame, width=5, font=("Arial", 16), justify='center')  
        self.entry_scale.pack()

        self.label_path = tk.Label(frame, text="", font=self.default_font, bg='lightblue')
        self.label_path.pack()

        self.label_output = tk.Label(frame, text="Output Resized Image Path (include the new filename):", font=self.default_font, bg='lightblue')
        self.label_output.pack()

        self.entry_output = tk.Entry(frame, width=40, font=("Arial", 16), justify='center')
        self.entry_output.pack()

        self.button_resize = tk.Button(frame, text="Resize Image", command=self.resize_image, font=self.default_font, bg='white')
        self.button_resize.pack(pady=10)

        self.label_message = tk.Label(frame, text="", font=("Arial", 16), bg='lightblue', fg='red')
        self.label_message.pack()

        self.button_back = tk.Button(frame, text="Back", command=self.root.destroy, font=("Arial", 14), bg='white')
        self.button_back.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        self.entry_path.delete(0, tk.END)
        self.entry_path.insert(0, file_path)

    def resize_image(self):
        try:
            image_path = self.entry_path.get()
            scale = float(self.entry_scale.get())
            output_path = self.entry_output.get()

            if not image_path or not output_path:
                self.show_error("Please provide both the image path and the output path.")
                return

            if not os.path.isfile(image_path):
                self.show_error("Invalid image path. Please provide a valid image file.")
                return

            image = Image.open(image_path)

            original_width, original_height = image.size
            new_width = int(scale * original_width)
            new_height = int(scale * original_height)

            resized_image = image.resize((new_width, new_height), Image.LANCZOS)

            resized_image.save(output_path)

            self.show_message("Success: Image resized and saved successfully!")

        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def show_error(self, message):
        self.label_message.config(text=message, fg='red')

    def show_message(self, message):
        self.label_message.config(text=message, fg='green')

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()
