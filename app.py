from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Lorem Ipsum"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host=os.environ.get("IP", '0.0.0.0'), port=port)