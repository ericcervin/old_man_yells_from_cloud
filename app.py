from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_port = os.environ.get('PORT', '5000 (Local Default)')
    return f'<h1>Hello, World!</h1><p>Flask is running! Port used: {current_port}</p>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
