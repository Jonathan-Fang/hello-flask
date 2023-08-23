from flask import Flask, redirect, url_for, request # request from Flask not Python library
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

@app.route("/youtube_api/", methods=['POST', 'GET']) # Flask requires method
def youtube_api():
    if request.method == 'POST':
        keyword = request.form['search']
        youtube_url = execute_function(keyword)
        return redirect(url_for('youtube_api', value=keyword, yurl = youtube_url)) # dash, HTML can access Python functions
    else:
        keyword = request.args.get('search')
        youtube_url = request.args.get('yurl')
        return render_template("youtube_api.html", value=keyword, yurl = youtube_url) # function doesn't know each other

def execute_function(keyword):
    # Insert function's logic here
    # YouTube API.py
    # test if I can do this first, and then try to make the function work
    
    # import requests

    # keyword = input("What video would you like to search for?\n") # keyword print success

    API_response = requests.get ('https://youtube.googleapis.com/youtube/v3/search?q=' + keyword + '&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM')
    # response = requests.get ('https://youtube.googleapis.com/youtube/v3/search?q=barbie&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM')

    json = API_response.json() # json print success

    video = json["items"][0]["id"]["videoId"] # video print success

    video_url = ("https://youtube.com/embed/" + video)

    print(video_url) # console only
    
    return video_url

@app.route("/weather_api/")
def weather_api():
    if request.method == 'POST':
        location_query = request.form['weather_search']
        weather_data = execute_weather_function(location_query)
        return redirect(url_for('weather_results', weather_html = weather_data))
    else:
        location_query = request.args.get('weather_search')
        weather_data = request.args.get('')
        return render_template("weather_api.html", weather_html = weather_data)

def execute_weather_function(location_query):
    # insert function here
    return render_template("weather_api.html")

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application on the local development server
    app.run(debug=True)