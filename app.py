from flask import Flask, redirect, url_for, request, flash # request from Flask not Python library
from flask import render_template
import requests
app = Flask(__name__)
app.secret_key = 'why_is_this_necessary'

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
        print('if success') #debugging
        youtube_url = execute_function(keyword) # if youtube url unable to be fetched, then return flashed error message
        # for invalid responses
        if youtube_url == 'Invalid video search':
            return render_template("youtube_api.html", error = youtube_url)

        response = requests.get(youtube_url)
        print(response)
        print(response.status_code)
        return redirect(url_for('youtube_api', value=keyword, yurl = youtube_url)) # dash, HTML can access Python functions
    else:
        keyword = request.args.get('search')
        youtube_url = request.args.get('yurl')
        if youtube_url == None:
            youtube_url = 'https://www.youtube.com/embed/bp2GF8XcJdY' # default video playing, since it'd be better to have new page if delete video
        return render_template("youtube_api.html", value=keyword, yurl = youtube_url) # function doesn't know each other

def execute_function(keyword):
    # Insert function's logic here
    # YouTube API.py
    # test if I can do this first, and then try to make the function work
    
    # import requests

    # keyword = input("What video would you like to search for?\n") # keyword print success
    error = None
    API_response = requests.get ('https://youtube.googleapis.com/youtube/v3/search?q=' + keyword + '&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM')
    # response = requests.get ('https://youtube.googleapis.com/youtube/v3/search?q=barbie&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM')

    json = API_response.json() # json print success
    print('https://youtube.googleapis.com/youtube/v3/search?q=' + keyword + '&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM') #debug

    # how to break the youtube thing: kjsadnnnaisuhydq73e4h3whijsbcehwbfesdf
    num=0
    print(num, " debug") #debug
    if bool(json["items"]): #check if items list is empty
        while "youtube#video" not in json["items"][num]["id"]["kind"]:
            num = num + 1
            print(num + "debug inside") #debug
            if num >= 4:
                error = 'Invalid video search'
                return error
    else:
        error = 'Invalid video search'
        return error

    video = json["items"][num]["id"]["videoId"] # navigating

    video_url = ("https://youtube.com/embed/" + video)

    print(video_url) # console only
    
    return video_url

@app.route("/weather_api/", methods=['POST', 'GET'])
def weather_api():
    error = None
    if request.method == 'POST':
        location_query = request.form['weather_search']
        weather_data = execute_weather_function(location_query)
        if weather_data == None:
            error = 'This location is invalid, would you like to try again?'
            flash('This location is invalid, would you like to try again?')
            return redirect(url_for('weather_results', weather_val = location_query, weather_html = ''))
        return redirect(url_for('weather_results', weather_val = location_query, weather_html = weather_data))
    else:
        location_query = request.args.get('weather_search')
        weather_data = request.args.get('weather_val')
        return render_template("weather_api.html", weather_val = location_query, weather_html = weather_data)

def execute_weather_function(location_query):
    # ask what city they want the weather for and take user input
    # turn the user input, feed it into geocode, return latitude and longitude
    get_link = "https://geocode.maps.co/search?q=" + location_query

    geocode_API = requests.get(get_link)

    # spit out json
    geocode_json_output = geocode_API.json()

    # navigate
    lat = geocode_json_output[0]["lat"]
    lon = geocode_json_output[0]["lon"]

    response_API = requests.get('https://api.weather.gov/points/' + lat + ',' + lon)

    # for invalid responses
    status_code = response_API.status_code
    if status_code != 200: # if not valid
        return None

    # rename and takes output
    coords_json_output = response_API.json()

    # print dict; key and value
    # print(coords_json_output["properties"]["forecast"]) # success

    # rename
    gridpoint = coords_json_output["properties"]["forecast"]

    # navigate to the thing; gridpoint to forecast; fetch data
    forecast_response_API = requests.get(gridpoint)

    # rename and takes output
    forecast_response_output = forecast_response_API.json()

    # rename
    checkpoint = forecast_response_output["properties"]["periods"][0]

    weather_prompt = location_query + "'s weather: "
    weather_str = weather_prompt + checkpoint["detailedForecast"]
    print(weather_str) #console only

    # print(weather_prompt + checkpoint["detailedForecast"]) # success
    return weather_str

@app.route("/weather_results/") # required to load the page
def weather_results():
    result_location = request.args.get('weather_html')
    return render_template("weather_results.html", weather_html = result_location)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application on the local development server
    app.run(debug=True)