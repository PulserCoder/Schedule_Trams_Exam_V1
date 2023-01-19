## вариант 1
from flask import Flask, render_template, request, jsonify
from utils import *
from datetime import datetime
import logging

app = Flask(__name__, template_folder='templates')

logger = logging.getLogger()
file_handler = logging.FileHandler("log.logs")
logger.addHandler(file_handler)


@app.route('/')
def show_now_info():
    logger.warning('Главная страничка запущена')
    """Return main index view with departures which are after now"""
    return render_template('index.html', departures=load_info_by_nowtime(), data=datetime.today().date())


@app.route('/schedule')
def show_all_info():
    logger.warning('Страничка расписания была запущена')
    """Return all departures as in file json"""
    return render_template('all_schedule.html', departures=load_all_info())


@app.route('/station')
def show_stations():
    """Return all sorted stations or by station"""
    if request.args.get('s') != None:
        logger.warning(f'Был сделан запрос на поиск {request.args.get("s")}')
        return render_template('stations.html', departures=load_info_by_station(request.args.get('s')))
    else:
        logger.warning(f'Была запущена страничка со станциями')
        return render_template('stations.html', departures=sorted(load_all_info(), key=lambda x: x['station']))


@app.errorhandler(404)
def not_found_error(error):
    return f'<h1>{error}</h1>'


@app.errorhandler(500)
def error_on_server(error):
    return f'<h1>{error}</h1>'


@app.route('/api/departures')
def send_json_all_info():
    return jsonify(load_all_info())


@app.route('/api/departures')
def send_json_all_info():
    return jsonify(load_all_info())


@app.route('api/stations/<station>')
def send_info_by_station(station):
    return jsonify(load_info_by_station(station))


if __name__ == '__main__':
    app.run()
