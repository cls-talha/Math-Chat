from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample messages (you can replace these with actual messages from your backend)
    messages = [
        {"name": "John", "text": "Hello, how are you?", "time": "9:00 AM"},
        {"name": "Jane", "text": "I'm doing great! What about you?", "time": "9:05 AM"},
        {"name": "John", "text": "I'm doing well too, thanks!", "time": "9:10 AM"},
    ]

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
