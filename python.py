import tkinter as tk
from tkinter import scrolledtext

# Function to send message
def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return
    chat_window.config(state='normal')
    chat_window.insert(tk.END, "You: " + user_msg + "\n")
    chat_window.insert(tk.END, "Bot: " + generate_reply(user_msg) + "\n")
    chat_window.config(state='disabled')
    entry.delete(0, tk.END)

# Simple bot reply logic
def generate_reply(msg):
    return f"I heard you say '{msg}'"

# Create the main window
root = tk.Tk()
root.title("Simple Chat App")

# Chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=50, height=20)
chat_window.pack(padx=10, pady=10)

# Entry field
entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
entry.bind("<Return>", lambda event: send_message())

# Send button
send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT, padx=10, pady=(0, 10))

# Run the app
root.mainloop()
