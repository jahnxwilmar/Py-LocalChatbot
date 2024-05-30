from tkinter import *
from chat import chat_with_model

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_windows()

    def run(self):
        self.window.mainloop()

    def _setup_main_windows(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1000, height=550, bg=BG_COLOR)

        # HEAD LABEL
        head_label = Label(
            self.window,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            text="CHATBOT",
            font=FONT_BOLD,
            pady=10
        )
        head_label.place(relwidth=1)

        # TINY DIVIDER
        line = Label(
            self.window,
            width=450,
            bg=BG_GRAY,
        )
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget
        self.text_widget = Text(
            self.window,
            width=20,
            height=2,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT,
            padx=5,
            pady=5
        )
        self.text_widget.place(rely=0.08, relheight=0.745, relwidth=1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # SCROLL BAR
        scrollbar = Scrollbar(
            self.text_widget,
        )
        scrollbar.place(relheight=1, relx=-1)
        scrollbar.configure(command=self.text_widget.yview)

        # BOTTOM LABEL
        bottom_label = Label(
            self.window,
            bg=BG_GRAY,
            height=80
        )
        bottom_label.place(relwidth=1, rely=0.825)

        # MESSAGE ENTRY BOX
        self.msg_entry = Entry(
            bottom_label,
            bg="#2C3E50",
            fg=TEXT_COLOR,
            font=FONT,
        )
        self.msg_entry.place(
            relwidth=0.74,
            rely=0.008,
            relx=0.11,
            relheight=0.06
        )
        self.msg_entry.focus()
        self.msg_entry.bind(
            "<Return>",
            self._on_enter_pressed
        )

        # SEND BUTTON
        send_button = Button(
            bottom_label,
            text="Send",
            font=FONT_BOLD,
            width=20,
            bg=BG_GRAY,
            command=lambda: self._on_enter_pressed(None)
        )
        send_button.place(
            relx=0.855,
            rely=0.008,
            relheight=0.06,
            relwidth=0.1
        )

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(
            msg, "You"
        )

    def _insert_message(self, msg, sender):
        if not msg:
            return

        if msg.lower() in ['exit', 'quit']:
            self.window.destroy()

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"Chatbot: {chat_with_model(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()

    # while True:
    #     human_input = input("Human: ")
    #
    #     if human_input.lower() in ["exit", "quit", "bye"]:
    #         print("Chatbot: Goodbye! Come back if you have any questions!")
    #         break
    #
    #     model_response = chat_with_model(human_input)
    #
    #     print("Chatbot: ", model_response)
