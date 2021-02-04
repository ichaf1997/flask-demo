from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_page():
    return "This A Flask Demo !"

@app.route('/health/')
def health_page():
    return "If you see this Page. Your Server is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
