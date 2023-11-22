# JuJu Video Player

This project utilizes Flask to create a video player web application allowing users to view videos with various settings.

## Overview

The application serves videos stored in the `static/videos` directory, generating thumbnails for each video in the `static/thumbnails` folder. Videos are displayed with associated thumbnails, and users can control video playback based on defined settings.

## Features

- **Video Playback**: Allows users to watch videos from the provided directory.
- **Thumbnails**: Automatically generates thumbnails for videos in the `static/videos` folder.
- **Settings Management**: Provides settings for configuring video playback times and enabling/disabling night mode.

## Installation

1. Clone this repository.
2. Ensure you have Python 3 installed.
3. Install required dependencies using the following command:

    ```bash
    pip install flask opencv-python-headless
    ```

4. Run the application with `python app.py`.

## File Structure

- `/static`: Contains static files (videos, thumbnails).
- `/templates`: HTML templates for rendering web pages.
- `app.py`: Main Flask application file.
- `settings.json`: JSON file storing initial and updated settings.
- `/templates/controls.html`: HTML file for controlling settings.
- `/templates/index.html`: HTML file for the main video player interface.

## Usage

1. Start the Flask application with `python app.py`.
2. Access the application in your web browser at `http://localhost:5000`.
3. Navigate between the video player and control settings pages.

## Additional Notes

- The application runs on `http://localhost:5000` by default.
- Video thumbnails are automatically generated upon startup.
- Controls/Settings are still a work in progress.

## Folder Structure

```
/home/JuJuVideoPlayer/
│
├── static/
│   ├── thumbnails/
│   └── videos/
│
├── templates/
│   ├── controls.html
│   └── index.html
│
├── app.py
├── README.md
└── settings.json
```

---
