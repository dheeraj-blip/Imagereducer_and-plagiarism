import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import html2text

class PlagiarismCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='lightblue')
        self.default_font = ("Arial", 20)
        self.root.title("Plagiarism Checker")

        self.create_widgets()

    def create_widgets(self):
        window_height = 350
        window_width = 600
        self.root.geometry(f"{window_width}x{window_height}")

        frame = tk.Frame(self.root, bg='lightblue')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label_url = tk.Label(frame, text="Enter Website URL:", font=self.default_font, bg='lightblue')
        self.label_url.pack()

        self.entry_url = tk.Entry(frame, width=40, font=("Arial", 16), justify='center')
        self.entry_url.pack()

        self.label_user_text = tk.Label(frame, text="Enter User Text:", font=self.default_font, bg='lightblue')
        self.label_user_text.pack()

        self.entry_user_text = tk.Entry(frame, width=40, font=("Arial", 16), justify='center')
        self.entry_user_text.pack()

        self.button_check_plagiarism = tk.Button(frame, text="Check Plagiarism", command=self.check_plagiarism, font=self.default_font, bg='white')
        self.button_check_plagiarism.pack(pady=20)

        self.label_similarity_score = tk.Label(frame, text="", font=("Arial", 16), bg='lightblue', fg='red')
        self.label_similarity_score.pack()

        self.button_back = tk.Button(frame, text="Back", command=self.root.destroy, font=("Arial", 14), bg='white')
        self.button_back.pack(pady=10)

    def get_text_from_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = html2text.html2text(soup.get_text())
            return text_content
        except requests.exceptions.RequestException as e:
            return None

    def preprocess_text(self, text):
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]
        preprocessed_text = ' '.join(tokens)
        return preprocessed_text

    def doc2vec_similarity(self, text1, text2):
        documents = [TaggedDocument(word_tokenize(text1), tags=[0]), TaggedDocument(word_tokenize(text2), tags=[1])]
        model = Doc2Vec(documents, vector_size=200, window=50, min_count=1, workers=4)
        similarity = model.dv.similarity(0, 1)
        return similarity

    def check_plagiarism(self):
        url = self.entry_url.get()
        user_input = self.entry_user_text.get()

        if not url or not user_input:
            self.label_similarity_score.config(text="Please enter both Website URL and User Text.")
            return

        reference_text = self.get_text_from_url(url)

        if reference_text:
            preprocessed_reference_text = self.preprocess_text(reference_text)
            preprocessed_user_input = self.preprocess_text(user_input)
            similarity_score = self.doc2vec_similarity(preprocessed_user_input, preprocessed_reference_text)
            self.label_similarity_score.config(text=f"Similarity Score: {similarity_score}")
        else:
            self.label_similarity_score.config(text="Error: Unable to retrieve content from the specified website.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismCheckerApp(root)
    root.mainloop()
