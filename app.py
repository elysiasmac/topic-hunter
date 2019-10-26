from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

@app.route("/json")
def json():
    return render_template('index.html')

@app.route("/background_process_test")
def background_process_test():
    print("hello")
    return "nothing"