from flask import Flask
import utils
app = Flask(__name__, static_folder='CesiumUnminified',
            template_folder='templates')


@app.route('/')
def hellow_world():
    return utils.get_main_page()


@app.route('/earth')
def hellow_world1():
    return utils.get_earth_page()


@app.route('/time')
def hellow_world2():
    return utils.get_time()


@app.route('/sum')
def hellow_world3():
    return utils.get_sum()


if __name__ == '__main__':
    app.run(host='192.168.1.106', port=5001)
