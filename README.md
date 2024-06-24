# Openeyelvm for custom datasets Creation

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
    git clone https://github.com/heisdenverr/openeyelvm.git
    cd flask-image-downloader
    ```
