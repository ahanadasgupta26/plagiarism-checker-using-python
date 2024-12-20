from difflib import SequenceMatcher
import tkinter as tk
from tkinter import filedialog,ttk
import threading

def select_file1():
    file_path=filedialog.askopenfilename(filetypes=[("Text Files","*.txt")])
    if file_path:
        file1_entry.delete(0,tk.END)
        file1_entry.insert(0,file_path)

def select_file2():
    file_path=filedialog.askopenfilename(filetypes=[("Text Files","*.txt")])
    if file_path:
        file2_entry.delete(0,tk.END)
        file2_entry.insert(0,file_path)

def check_plagiarism():
    file1_path=file1_entry.get()
    file2_path=file2_entry.get()
    if not file1_path or not file2_path:
        result_label.config(text="Please select both files.")
        return
    progress_bar['value']=0
    progress_bar['maximum']=100
    threading.Thread(target=calculate_plagiarism,args=(file1_path,file2_path)).start()

def calculate_plagiarism(file1_path,file2_path):
    try:
        with open(file1_path) as file_1,open(file2_path) as file_2:
            data_file1=file_1.read()
            data_file2=file_2.read()
            progress_bar['value']=50
            matches=SequenceMatcher(None,data_file1,data_file2).ratio()
            progress_bar['value']=100
            result_label.config(text=f"Plagiarized content:{matches*100:.2f}%")
    except Exception as e:
        result_label.config(text=f"An error occurred:{e}")

root=tk.Tk()
root.title("Plagiarism Detector")
root.geometry("500x350")

file1_label=tk.Label(root,text="Select File 1:",font=("Helvetica",10,"bold"))
file1_label.pack(pady=5)
file1_entry=tk.Entry(root,width=50)
file1_entry.pack(pady=5)
file1_button=tk.Button(root,text="Browse",command=select_file1)
file1_button.pack(pady=5)

file2_label=tk.Label(root,text="Select File 2:",font=("Helvetica",10,"bold"))
file2_label.pack(pady=5)
file2_entry=tk.Entry(root,width=50)
file2_entry.pack(pady=5)
file2_button=tk.Button(root,text="Browse",command=select_file2)
file2_button.pack(pady=5)

check_button=tk.Button(root,text="Check Plagiarism",command=check_plagiarism)
check_button.pack(pady=20)

progress_bar=ttk.Progressbar(root,orient='horizontal',length=200,mode='determinate')
progress_bar.pack(pady=10)

result_label=tk.Label(root,text="Plagiarized content: ",font=("Helvetica",15,"bold"))
result_label.pack(pady=10)

root.mainloop()