'''
This is the main file of the intelligent trade show business card app with GPT chat functionality.
'''
import tkinter as tk
from chatbot import ChatBot
class BusinessCardApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Business Card App")
        self.geometry("800x600")
        self.chatbot = ChatBot()
        self.create_widgets()
    def create_widgets(self):
        self.chat_history = tk.Text(self, height=20, width=80)
        self.chat_history.pack(pady=10)
        self.user_input = tk.Entry(self, width=80)
        self.user_input.pack(pady=10)
        self.user_input.bind("<Return>", self.send_message)
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)
    def send_message(self, event=None):
        message = self.user_input.get()
        self.user_input.delete(0, tk.END)
        response = self.chatbot.generate_response(message)
        self.chat_history.insert(tk.END, "User: " + message + "\n")
        self.chat_history.insert(tk.END, "ChatBot: " + response + "\n")
        self.chat_history.insert(tk.END, "\n")
        self.chat_history.see(tk.END)
if __name__ == "__main__":
    app = BusinessCardApp()
    app.mainloop()