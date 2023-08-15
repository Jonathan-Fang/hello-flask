from flask import Flask, jsonify
from flask import render_template
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/youtube-api/")
def youtube():
    return render_template("youtube-api.html")

def execute_function():
    # Insert function's logic here
    # YouTube API.py
    # test if I can do this first, and then try to make the function work
    
    # import requests

    keyword = input("What video would you like to search for?\n") # keyword print success

    API_response = requests.get ('https://youtube.googleapis.com/youtube/v3/search?q=' + keyword + '&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM')
    # response = requests.get ('https://youtube.googleapis.com/youtube/v3/search?q=barbie&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM')

    json = API_response.json() # json print success

    video = json["items"][0]["id"]["videoId"] # video print success

    video_url = ("https://youtube.com/watch?v=" + video)

    print(video_url)
    
    return {"message": "Function executed successfully"}

@app.route('/execute-function', methods=['Get'])
def handle_execute_function():
    # what is handle?
    result = execute_function()
    return jsonify(result)