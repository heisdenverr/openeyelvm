# Flask Image Downloader Web Application

This Flask web application allows users to download images from the web based on a search query and create a dataset. The images are downloaded concurrently for better performance, and the final dataset is provided as a ZIP file for download.

## Features

- Specify a folder name, search query, and the number of images per keyword.
- Concurrent image downloading for faster dataset creation.
- Create a ZIP file containing the downloaded images.
- Simple web interface for inputting search parameters and downloading the dataset.

## Technologies Used

- Python
- Flask
- Gunicorn
- Bing Image Downloader
- Dotenv
- HTML/CSS

## Requirements

- Python 3.8 or higher
- Pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/flask-image-downloader.git
    cd flask-image-downloader
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your environment variables:
    ```plaintext
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter the folder name, search query, and the number of images per keyword.

4. Click the "Create Dataset" button to download the images and create the ZIP file.

5. Download the ZIP file containing the dataset.

## Deployment

### Deploying to Render

1. Ensure you have a `requirements.txt` file and a `Procfile` in the root directory.

2. Your `requirements.txt` should include:
    ```plaintext
    Flask==2.1.2
    gunicorn==20.1.0
    bing-image-downloader==1.1.2
    python-dotenv==0.20.0
    ```

3. Your `Procfile` should include:
    ```plaintext
    web: gunicorn app:app
    ```

4. Push your code to a Git repository (e.g., GitHub).

5. Log in to [Render](https://render.com/) and create a new Web Service.

6. Connect your repository and configure the build and start commands:
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app`

7. Set any necessary environment variables in the Render dashboard.

8. Deploy the service and monitor the logs for any errors.

## File Structure

