#!/usr/bin/env python3
from flask import Flask
from CLI_Bot import Bot

app = Flask(__name__)

@app.route('/')
def helper():
    bot = Bot()
    run = bot.run()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
