import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import re
import difflib
import PyPDF2
import os

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    return tokens

# Function to calculate plagiarism score
def plagiarism_score(text1, text2):
    text1_processed = preprocess_text(text1)
    text2_processed = preprocess_text(text2)
    similarity = difflib.SequenceMatcher(None, text1_processed, text2_processed).ratio()
    return similarity

# Function to handle plagiarism detection
def detect_plagiarism():
    text1 = text_area1.get("1.0", tk.END)
    text2 = text_area2.get("1.0", tk.END)

    if not text1.strip() or not text2.strip():
        messagebox.showwarning("Input Error", "Please enter text in both fields.")
        return

    score = plagiarism_score(text1, text2)
    feedback = "No plagiarism detected."
    if score >= 0.8:
        feedback = "Warning: High similarity detected! Please review your texts."

    messagebox.showinfo("Plagiarism Score", f"Plagiarism Score: {score:.2f}\n{feedback}")

# Function to upload PDF and extract text
def upload_pdf1():
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            text_area1.delete("1.0", tk.END)
            text_area1.insert(tk.END, text)

def upload_pdf2():
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            text_area2.delete("1.0", tk.END)
            text_area2.insert(tk.END, text)

# Setting up the main window
root = tk.Tk()
root.title("Plagiarism Detection Tool")
root.geometry("600x600")
root.configure(bg="#f2f2f2")

# Frame for the text areas and labels
frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(padx=20, pady=20)

# Label and text area for first text input
label1 = tk.Label(frame, text="Enter First Text or Upload PDF:", bg="#f2f2f2", font=("Arial", 12))
label1.grid(row=0, column=0, padx=5, pady=(5, 10))
text_area1 = scrolledtext.ScrolledText(frame, width=70, height=10, font=("Arial", 10))
text_area1.grid(row=1, column=0, padx=5, pady=10)

# Button to upload first PDF
upload_button1 = tk.Button(frame, text="Upload PDF 1", command=upload_pdf1, bg="#2196F3", fg="white", font=("Arial", 10))
upload_button1.grid(row=2, column=0, padx=5, pady=(5, 10))

# Label and text area for second text input
label2 = tk.Label(frame, text="Enter Second Text or Upload PDF:", bg="#f2f2f2", font=("Arial", 12))
label2.grid(row=3, column=0, padx=5, pady=(10, 5))
text_area2 = scrolledtext.ScrolledText(frame, width=70, height=10, font=("Arial", 10))
text_area2.grid(row=4, column=0, padx=5, pady=10)

# Button to upload second PDF
upload_button2 = tk.Button(frame, text="Upload PDF 2", command=upload_pdf2, bg="#2196F3", fg="white", font=("Arial", 10))
upload_button2.grid(row=5, column=0, padx=5, pady=(5, 10))

# Button to start plagiarism detection
detect_button = tk.Button(frame, text="Detect Plagiarism", command=detect_plagiarism, bg="#4CAF50", fg="white", font=("Arial", 12))
detect_button.grid(row=6, column=0, padx=5, pady=20)

# Run the application
root.mainloop()
