from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    # Arahkan ke direktori root atau direktori lain tempat file `index.html` berada
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run()