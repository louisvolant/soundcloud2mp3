#!/usr/local/bin/python3
__author__ = 'Louis Volant'
__version__= 1.0

TARGET_BITRATE = "128K"
BASE_OUTPUT_FILENAME = "output.mp3"

import subprocess
import argparse
import logging, re
import shutil

# README
# First step : ensure to have ffmpeg installed
# execute with
# python3 -m venv myenv
# source myenv/bin/activate
# pip install yt-dlp
# python3 soundcloud2mp3.py 'https://soundcloud.com/ACCOUNT_NAME/SONG_NAME' 
# Once finished, simply desactivate the virtual environment using "deactivate"


def sanitize_filename(input):
    # Remove invalid characters from filename
    return re.sub(r'[<>:"/\\|?*]', '', input)

def get_soundcloud_title(url):
    # Define the command to get the title of the Soundcloud video
    command = ['yt-dlp', '--get-title', url]
    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def download_soundcloud_audio(url, output_path=BASE_OUTPUT_FILENAME, audio_quality=TARGET_BITRATE):

    # Check if ffmpeg is installed
    if shutil.which('ffmpeg') is None:
        print("ffmpeg is not installed. Please install ffmpeg and make sure it's in your PATH.")
        return
    
    # Define the command to download and convert the audio
    command = [
        'yt-dlp',
        '-f', 'bestaudio',
        '-x',  # Extract audio
        '--audio-format', 'mp3',  # Convert to mp3
        '--audio-quality', '0',  # Best quality
        '-o', output_path,
        url
    ]

    # Run the command
    subprocess.run(command, check=True)
    
    print(f'Audio has been downloaded and converted to {output_path}')


def main():
    parser = argparse.ArgumentParser(description='Download Soundcloud audio and convert to MP3.')
    parser.add_argument('url', type=str, help='The URL of the Soundcloud audio')
    # Example : python3 soundcloud2mp3.py https://soundcloud.com/ACCOUNT_NAME/SONG_NAME output_example.mp3
    parser.add_argument('-o', '--output', default='downloads', help='Output directory')
    parser.add_argument('-q', '--audio-quality', default=TARGET_BITRATE, help='Audio quality (e.g., 128K, 192K, 320K)')

    args = parser.parse_args()

    # Get the audio title and sanitize it for use as a filename
    audio_title = get_soundcloud_title(args.url)
    sanitized_title = sanitize_filename(audio_title)
    output_path = f"{sanitized_title}.mp3"

    logging.info('Processing: {0} and storing to {1}'.format(args.url, output_path))

    download_soundcloud_audio(args.url, output_path, args.audio_quality)


if __name__ == '__main__':
    ## Initialize logging before hitting main, in case we need extra debuggability
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    main()