import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import cv2
import json
import random

app = Flask(__name__)

# Specify the path to the folder containing videos and where to save thumbnails
video_dir = 'static/videos'
thumbnail_dir = 'static/thumbnails'

# Create the thumbnails folder if it doesn't exist
os.makedirs(thumbnail_dir, exist_ok=True)

# Create an empty list to store video information
videos = []

# Helper function to generate a video thumbnail
def generate_thumbnail(video_path):
    video_capture = cv2.VideoCapture(video_path)
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    start_frame = 30 * fps  # Start capturing frames from 30 seconds
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    success, image = video_capture.read()
    if success:
        thumbnail_filename = os.path.splitext(os.path.basename(video_path))[0] + '.jpg'
        thumbnail_path = os.path.join(thumbnail_dir, thumbnail_filename)
        cv2.imwrite(thumbnail_path, image)
        return thumbnail_filename
    return None

# Generate the list of video information
for video_file in os.listdir(video_dir):
    if video_file.endswith(('.mp4', '.avi', '.mkv')):
        video_path = os.path.join(video_dir, video_file)
        thumbnail_filename = generate_thumbnail(video_path)
        if thumbnail_filename:
            videos.append({'video_path': video_path, 'thumbnail_path': os.path.join('thumbnails', thumbnail_filename)})

# Path to the JSON settings file
settings_file = 'settings.json'

# Load initial settings from JSON
if not os.path.exists(settings_file):
    initial_settings = {
        'play_time_enabled': False,
        'play_start_time': '09:00',
        'play_end_time': '18:00',
        'night_mode_enabled': False,
        'night_start_time': '20:00',
        'night_end_time': '06:00',
    }
    with open(settings_file, 'w') as file:
        json.dump(initial_settings, file)

# Route to display the video page
@app.route('/')
def index():
    random.shuffle(videos)

    # Load the settings from the JSON file
    with open(settings_file, 'r') as file:
        settings = json.load(file)
    
    return render_template('index.html', videos=videos, settings=settings)


# Route for the control page
@app.route('/controls')
def controls():
    # Load the settings from the JSON file
    with open(settings_file, 'r') as file:
        settings = json.load(file)
    
    return render_template('controls.html', settings=settings)

# Route to handle form submissions for settings
@app.route('/apply_settings', methods=['POST'])
def apply_settings():
    data = request.get_json()
    updated_settings = data['settings']

    # Save the updated settings to the JSON file
    with open(settings_file, 'w') as file:
        json.dump(updated_settings, file)

    return jsonify({'message': 'Settings saved successfully'})

# Route to fetch the current settings
@app.route('/get_settings', methods=['GET'])
def get_settings():
    # Read the settings from the JSON file
    with open(settings_file, 'r') as file:
        settings = json.load(file)

    return jsonify(settings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)