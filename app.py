from flask import Flask, request, render_template, send_file
import os
from zipfile import ZipFile
from bing_image_downloader import downloader

app = Flask(__name__)

class ImageDownloader:
    def __init__(self):
        self.downloader = downloader

    def download_images(self, fname, query, limits):
        
        if not os.path.exists(fname):
            os.mkdir(fname)

        
        keywords = query.lower().split(",")

        
        for keyword in keywords:
            keyword = keyword.strip()

            
            keyword_dir = os.path.join(fname, keyword)
            if not os.path.exists(keyword_dir):
                os.mkdir(keyword_dir)

            
            self.downloader.download(keyword, limits, output_dir=fname)
        
        return f"Dataset created for query: {query}"

    def create_zip_file(self, fname):
        zip_path = f"{fname}.zip"
        with ZipFile(zip_path, "w") as zip_file:
            for root, dirs, files in os.walk(fname):
                for file in files:
                    zip_file.write(os.path.join(root, file),
                                   os.path.relpath(os.path.join(root, file), fname))
        return zip_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-dataset', methods=['POST'])
def create_dataset():
    fname = request.form['fname']
    query = request.form['query']
    limits = int(request.form['limits'])

    downloader_app = ImageDownloader()
    message = downloader_app.download_images(fname, query, limits)
    
    zip_path = downloader_app.create_zip_file(fname)
    
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)