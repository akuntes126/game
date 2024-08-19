from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route untuk melayani file CSS
@app.route('/styles.css')
def css():
    return send_from_directory('.', 'styles.css')

# Route untuk melayani file gambar
@app.route('/image.jpg')
def image():
    return send_from_directory('.', 'image.jpg')

@app.route('/Tebak_angka/thumbnail.png')
def tebak_angka_thumbnail():
    return send_from_directory('Tebak angka', 'thumbnail.png')

@app.route('/snake-game/thumbnail.jpg')
def snake_game_thumbnail():
    return send_from_directory('snake-game', 'thumbnail.jpg')

if __name__ == '__main__':
    app.run(debug=True)
