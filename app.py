from flask import Flask, render_template
from parser import parse_habr_news

app = Flask(__name__)

@app.route('/')
def home():
    news = parse_habr_news()  # Получаем данные из парсера
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)