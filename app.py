from flask import Flask, render_template, request
from utils import Utils

app = Flask(__name__)


@app.route('/')
def index():
    """ Главная страница, где осуществляется поиск конкретного предмета; вывод расписания"""
    today = Utils.print_subjects(Utils.weekdays())[0]
    tomorrow = Utils.print_subjects(Utils.weekdays())[1]
    return render_template('index.html', today=today, tomorrow=tomorrow)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route('/subject/', methods=["POST"])
def subject():
    """ Страница предмета, где осуществляется вывод всех занятий по предмету"""
    days = Utils.find_weekday_by_subject(request.form['name_of_subject'])
    if len(days) >= 1:
        return render_template('subject.html', subject=request.form['name_of_subject'], days=days)
    else:
        return render_template('none.html', subject=request.form['name_of_subject'])


if __name__ == "__main__":
    app.run(debug=False)
