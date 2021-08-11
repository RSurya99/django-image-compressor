# Image Compressor Website
 ![version](https://img.shields.io/badge/version-1.0-blue.svg)

Is a web app to compress image file (jpg/png) without compromising with the quality of image.

## Environment
- Python ver above 3.8.5

## Installation
- Create environment and install all the requirement based on `requirements.txt`
    ```bash
    pip3 install requirements.txt
    ```
- Create .env file in core folder and add this
    ```bash
    DEBUG=TRUE
    SECRET_KEY=YOUR_SECRET_KEY
    ```
- Run your app first to create the sqlite file
    ```bash
    python manage.py runserver
    ```
- Stop your app and migrate all the migrations
    ```bash
    python manage.py makemigrations
    ```
    ```bash
    python manage.py migrate
    ```
- Run again your app