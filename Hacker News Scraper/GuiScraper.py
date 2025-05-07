#GuiScraper.py

import csv 
import tkinter as tk
from tkinter import ttk
import webbrowser

def load_headlines(file_path):
    #load headlines from the csv file
    headlines = []
    try:
        with open(file_path, "r", encoding = "utf-8") as file:
            reader = csv.reader(file)
            next(reader) #skip the header row
            for row in reader:
                headlines.append((row[1], row[2])) #headline and url
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return headlines

def open_link(url):
    #open the given url in a web browser
    if url == "No URL Found" or not url:
        print("No valid URL to open")
    else:
        webbrowser.open(url)


def create_gui(headlines):
    #create the gui to display the headlines
    root = tk.Tk()
    root.configure(bg="black")
    root.title("Hacker News Headlines")
    root.geometry("600x400")

    frame = tk.Frame(root, bg="black")
    frame.pack(fill="both", expand =  True)

    canvas = tk.Canvas(frame, bg="black")
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="black")
    

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for index, (headline, url) in enumerate(headlines):
        display_text = f"{index + 1}. {headline}" + (" (No URL)" if url == "No URL Found" else "")
        btn = tk.Button(
            scrollable_frame, 
            text= display_text,
            command=lambda url=url: open_link(url), 
            wraplength=500,
            anchor="center",
            justify="center",
            bg="gray",
            fg="white",
            activebackground="darkgray",
            activeforeground="black",
            font=("Arial", 12, "bold"), 
            relief="raised",

        )
        btn.pack(anchor="center", pady=2, padx=10)

    root.mainloop()