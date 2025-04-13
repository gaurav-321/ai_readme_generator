# Project Documentation

## Table of Contents
1. [Assignment Solver](#assignment-solver)
2. [Flask Video Stream](#flask-video-stream)
3. [Music Discord Bot](#music-discord-bot)
4. [Proxy-API-Service](#proxy-api-service)

---

## Assignment Solver

### Purpose
The `Assignment Solver` program converts plain text input into images that appear handwritten, supporting custom fonts and notebook-style backgrounds.

### Key Elements
- Converts text to handwritten images.
- Supports custom fonts and notebook backgrounds.
- Uses OpenCV for image processing and PIL for text overlay.
- Configurable via OpenCV trackbars for spacing and font size.

### Dependencies
- `OpenCV`
- `PIL` (Python Imaging Library)

### Output
Handwritten-style images saved in the `output/` directory.

---

## Flask Video Stream

### Purpose
A Flask web application that serves and allows searching of video files stored locally.

### Key Elements
- `app.py`: Sets up the Flask application, handles routing, and provides functionality to serve videos and search for them.
- Uses Flask library for web server functionality.
- Handles routing for displaying videos and search results.

### Dependencies
- Flask

### Output
A web interface allowing users to browse and search video files.

---

## Music Discord Bot

### Purpose
Music_Discord_Bot is a Discord bot designed to enhance the music experience by allowing users to play, skip, manage, and stop music directly from voice channels using commands.

### Key Elements
- `app.py`: Handles commands and events for the bot.
- `functions.py`: Contains functions for YouTube audio downloads and managing the song queue.
- `.env` file: Stores environment variables like the Discord bot token.

### Dependencies
- `discord.py` for interacting with Discord
- `youtube-dl` for downloading YouTube videos
- `python-dotenv` for handling environment variables

### Output
The bot responds to commands in Discord by playing music, managing the queue, and providing status updates.

---

## Proxy-API-Service

### Purpose
The Proxy-API-Service is a Python-based FastAPI application designed to scrape, filter, and verify public HTTP/SOCKS proxies from GitHub repositories. It provides an API for downloading raw and verified proxy lists with secure authentication.

### Key Elements
- **FastAPI Server**: Handles API requests efficiently.
- **GitHub Scraping Logic**: Searches for proxy-related files on GitHub.
- **Proxy Testing Module**: Validates proxies using HTTP/SOCKS support.
- **Background Collection Loop**: Automatically updates proxy lists every 30 minutes.
- **Secure Authentication**: Protects download endpoints with basic authentication.

### Dependencies
- `fastapi`
- `uvicorn`

### Output
The file returns a JSON object containing the content of requested files (e.g., raw.txt, proxies.txt). It also logs working proxies and their count when testing.