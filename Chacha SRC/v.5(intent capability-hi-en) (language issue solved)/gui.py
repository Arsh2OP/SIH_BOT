import tkinter as tk


def send_message():
    message = input_entry.get()
    if message:
        chat_listbox.insert(tk.END, "You: " + message)
        input_entry.delete(0, tk.END)


def select_language(event):
    selected_language = language_var.get()
    print("Selected Language:", selected_language)

root = tk.Tk()
root.title("Chat Interface")
root.geometry("400x600")
root.configure(bg="#121212") 


chat_frame = tk.Frame(root, bg="#121212")
chat_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_listbox = tk.Listbox(
    chat_frame, bg="#121212", fg="white", font=("Helvetica", 12), selectbackground="#121212", selectforeground="white", yscrollcommand=scrollbar.set
)
chat_listbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=chat_listbox.yview)

languages = ["English", "Hindi"]
language_var = tk.StringVar()
language_var.set(languages[0])  
language_dropdown = tk.OptionMenu(root, language_var, *languages)
language_dropdown.pack(side=tk.LEFT, padx=(10, 0))
language_dropdown.bind("<Configure>", select_language)


input_entry = tk.Entry(root, bg="#303030", fg="white", font=("Helvetica", 12), insertbackground="white")
input_entry.pack(side=tk.LEFT, pady=(0, 10), padx=10, fill=tk.X, expand=True)

mic_button = tk.Button(root, text="🎤", command=None, bg="#009688", fg="white", font=("Helvetica", 12))
mic_button.pack(side=tk.RIGHT, padx=(0, 10))

send_button = tk.Button(root, text="Send", command=send_message, bg="#009688", fg="white", font=("Helvetica", 12))
send_button.pack(side=tk.RIGHT, padx=(0, 10))

root.mainloop()
