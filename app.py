print("FILE IS RUNNING")

from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


knowledge_base = {
    "hi": "Hello. How can I assist you?",
    "hello": "Hello. How can I assist you?",
    "hey": "Hello. How can I assist you?",

    "how are you": "I am fine.",
    
    "what is your name": "I am BASICBOT, a rule-based chatbot.",
    "who are you": "I am BASICBOT, a rule-based chatbot.",

    "/help": (
        "Available commands:- \n"

        "> greetings: hi, hello, hey\n"
        "> utilities: time, date\n"
        "> information: features, developer, what is a chatbot, how does chatbot work, types of chatbot\n"
        "> exit: bye, goodbye, quit"
    ),

    "help": "Type /help for available commands.",

    "thanks": "You are welcome.",
    "thank you": "You are welcome.",

    "exit": "Goodbye.",
    "bye": "Goodbye.",
    "goodbye": "Goodbye.",
    "quit": "Goodbye.",

    "introduce yourself": "I am BASICBOT, a rule-based assistant.",
    "what can you do": "I can respond to commands, provide time, date, and basic information.",
    "features": "I support greetings, utilities like time and date, and basic responses.",
    "developer": "Developed as a rule-based chatbot system.",

    "what is a chatbot": "A chatbot is a software application that simulates human conversation.",
    "how does chatbot work": "It processes user input and returns predefined responses.",
    "types of chatbot": "Rule-based and AI-based chatbots.",
    "rule based chatbot": "A chatbot that works using predefined rules.",
    "ai chatbot": "A chatbot that uses machine learning and natural language processing. BASICBOT is a rule-based chatbot."
}


def get_response(message):
    message = message.lower().strip()

    # TIME
    if message in ["time", "what is the time", "current time"]:
        return datetime.now().strftime("Current time is %H:%M:%S")

    # DATE
    if message in ["date", "today date", "what is the date"]:
        return datetime.now().strftime("Today's date is %Y-%m-%d")

    return knowledge_base.get(
        message,
        "Command not recognized. Type /help."
    )


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    reply = get_response(user_message)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    print("Starting server...")
    app.run(debug=True)