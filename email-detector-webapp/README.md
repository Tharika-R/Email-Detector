# Email Detector Web Application

This project is a web application designed to detect suspicious tags in HTML files. It allows users to upload HTML files, which are then processed to identify any potentially harmful elements.

## Project Structure

```
email-detector-webapp
├── app.py                # Main entry point of the web application
├── detector.py           # Contains functions to read HTML files and detect suspicious tags
├── templates             # Directory for HTML templates
│   └── index.html       # Main page template with file upload form
├── static                # Directory for static files
│   └── style.css         # CSS styles for the web application
├── requirements.txt      # Lists dependencies required for the project
└── README.md             # Documentation for the project
```

## Requirements

To run this application, you need to have the following Python packages installed:

- Flask
- BeautifulSoup4

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Application

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the application using the following command:

```
python app.py
```

4. Open your web browser and go to `http://127.0.0.1:5000/`.
5. Use the file upload form to upload an HTML file for processing.

## Usage

After uploading an HTML file, the application will analyze the file for suspicious tags and display the results on the same page. If any suspicious elements are found, they will be listed along with the reasons for their classification.

## License

This project is open-source and available for modification and distribution.