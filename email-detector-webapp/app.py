from flask import Flask, render_template, request
from detector import find_suspicious_tags

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    message = None
    if request.method == 'POST':
        if 'file' not in request.files:
            message = "No file part"
        else:
            file = request.files['file']
            if file.filename == '':
                message = "No selected file"
            else:
                html = file.read().decode('utf-8')
                results = find_suspicious_tags(html)
                if not results:
                    message = "✅ No suspicious elements found."
    return render_template('index.html', results=results, message=message)

if __name__ == '__main__':
    app.run(debug=True)