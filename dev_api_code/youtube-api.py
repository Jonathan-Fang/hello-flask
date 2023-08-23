# API key is "AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM"

import requests

keyword = input("What video would you like to search for?\n") # keyword print success

API_response = requests.get ('https://youtube.googleapis.com/youtube/v3/search?q=' + keyword + '&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM')
# response = requests.get ('https://youtube.googleapis.com/youtube/v3/search?q=barbie&key=AIzaSyDkxZGugtLQ_4-Ugz2iw-JxxvBJtssrKiM')

json = API_response.json() # json print success

video = json["items"][0]["id"]["videoId"] # video print success

video_url = ("https://youtube.com/watch?v=" + video)

print(video_url)

"""
ok, here's what im going to do
this is a test file because idk why it doesn't work in the hello-flask project

and import requests is like module not found

but what i want to do is

on website
make html search bar button

user input keyword

keyword gets put into search

select the first video

then fetch the link of that and embed into my website
"""