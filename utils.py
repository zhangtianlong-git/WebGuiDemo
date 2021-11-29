import time
from flask import request
from flask import jsonify
from flask import render_template


def get_main_page():
    # return render_template('index.html')
    return render_template('fullpageTest.html')


def get_earth_page():
    return render_template('app.html')


def get_sum():
    d1 = int(request.values.get('d1'))
    d2 = int(request.values.get('d2'))
    d3 = int(request.values.get('d3'))
    return jsonify({'d': d1+d2+d3})


def get_time():
    time_str = time.strftime('%Y{}%m{}%d{} %X')
    return time_str.format('年', '月', '日')
