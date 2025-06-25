import tkinter as tk
from tkinter import scrolledtext
import random
import datetime
import webbrowser

# Initialize global variable for user's name
user_name = None

# Bot responses dictionary
def get_response(user_input):
    global user_name
    
    # If user name isn't set, ask for it
    if user_name is None:
        user_name = user_input.strip()
        return f"Nice to meet you, {user_name}! How can I help you today?"
    
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return f"Hello, {user_name}! How can I assist you today?"
    elif "how are you" in user_input:
        return f"I'm just a bot, but I'm doing great! How about you, {user_name}?"
    elif "your name" in user_input:
        return "I'm Lulu, your friendly assistant!"
    elif "bye" in user_input:
        return f"Goodbye, {user_name}! Have a wonderful day!"
    elif "date" in user_input or "today's date" in user_input:
        return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}."
    elif "link" in user_input or "information about" in user_input:
        query = user_input.replace("link", "").replace("information about", "").strip()
        if query:
            google_link = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            return f"Here's a link to help you find more information: {google_link}"
        else:
            return "Please tell me what information you need, and I'll find a link for you!"
    else:
        return random.choice([
            "I'm not sure how to respond to that.",
            "Can you clarify your question?",
            "That's interesting! Could you tell me more?"
        ])

# Function to handle sending messages
def send_message():
    user_input = entry.get().strip()
    if user_input:
        chat_window.config(state=tk.NORMAL)
        
        # Display user message
        chat_window.insert(tk.END, f"You: {user_input}\n", "user_bubble")
        
        # Display bot response
        response = get_response(user_input)
        chat_window.insert(tk.END, f"Bot: {response}\n", "bot_bubble")
        
        # If the bot response contains a link, make it clickable
        if "https://" in response:
            def open_link(event):
                webbrowser.open(response.split(": ")[1])
            chat_window.tag_add("link", f"end-{len(response)+2}c linestart", "end")
            chat_window.tag_config("link", foreground="blue", underline=True)
            chat_window.tag_bind("link", "<Button-1>", open_link)
        
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        entry.delete(0, tk.END)

# Function to clear the chat window
def clear_chat():
    global user_name
    user_name = None  # Reset user's name
    chat_window.config(state=tk.NORMAL)
    chat_window.delete(1.0, tk.END)
    chat_window.config(state=tk.DISABLED)

# Create the main Tkinter window
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#4A4AFF")

# Header
header = tk.Frame(root, bg="#4A4AFF", height=100)
header.pack(fill="x")
header_label = tk.Label(
    header, text="Hello, I'm LuLu :)", bg="#4A4AFF", fg="white",
    font=("Arial", 20, "bold")
)
header_label.pack(pady=20)

# Chat window
chat_window = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, state=tk.DISABLED, bg="#F5F5F5", fg="#333",
    font=("Arial", 12), height=20, bd=0
)
chat_window.pack(padx=10, pady=10, fill="both", expand=True)

# Text styling
chat_window.tag_config("user_bubble", background="#D4E6FF", foreground="#333", font=("Arial", 12), spacing3=5)
chat_window.tag_config("bot_bubble", background="#FFF5F8", foreground="#4A4AFF", font=("Arial", 12), spacing3=5)

# Input frame
input_frame = tk.Frame(root, bg="#F5F5F5", height=50)
input_frame.pack(side="bottom", fill="x")

# Entry widget
entry = tk.Entry(input_frame, bg="#FFF", fg="#333", font=("Arial", 14), bd=1, relief="flat")
entry.pack(side="left", padx=10, pady=10, fill="x", expand=True)
entry.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(
    input_frame, text="Send", bg="#4A4AFF", fg="white", font=("Arial", 12, "bold"),
    command=send_message, width=10
)
send_button.pack(side="right", padx=10, pady=10)

# Run the application
root.mainloop()
