# Soundcloud2Mp3
Python3 tool to retrieve MP3 sound from a given Soundcloud song url

**You should only retrieve copyright free MP3 sounds**

## Requirements

ffmepg, Python3, os, logging, subprocess, yt-dlp

Install FFmpeg first
````
brew install ffmpeg
````
Then
````
python3 -m venv myenv
source myenv/bin/activate
pip install yt-dlp
python3 soundcloud2mp3.py 'https://soundcloud.com/ACCOUNT_NAME/SONG_NAME' 
````

## How to execute

Go in the same folder than the python script and type

````
$ python3 soundcloud2mp3.py https://soundcloud.com/ACCOUNT_NAME/SONG_NAME
````