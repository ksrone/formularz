from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obsługa przesłanych danych z formularza
        name = request.form['name']
        return f'Witaj, {name}! Dane zostały przesłane.'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)