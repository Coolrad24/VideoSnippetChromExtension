from flask import Flask, jsonify, render_template, send_file, request
from flask_cors import CORS, cross_origin
import json
import requests
import time
from snippet import VideoEngine
from pytube import YouTube
app=Flask(__name__)
cors=CORS(app)

app.config['CORS_HEADERS'] = "Content-Type"
@app.route('/videos', methods=['GET','POST'])
def hello():
    data='no videos'
    start=0
    stop=0
    if request.method == 'POST':
      data=request.get_json()
      try:
        
        print(data)
        yt=YouTube(data)
        stream = yt.streams.get_by_itag(22)
        stream.download(filename='video.mp4')
        print('downloaded')
        time.sleep(5)
        ve=VideoEngine()
        newVid=ve.cut_video(start,stop,'video.mp4')
      except:
        print('not a video')
      
    return jsonify(data)
if __name__ ==  '__main__':
  app.run(debug=True)
 