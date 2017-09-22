#!/usr/bin/python
'''
A little web controller for the Dream Cheeky USB turret.
'''

__author__ = 'Joe Vacovsky Jr.'
from flask import Flask, render_template, request
from dreamcheekyturret import turret

APP = Flask(__name__)

T = turret()

@APP.route('/', methods=["GET"])
def main():
    if request.method == "GET":
        pass
        # return render_template("index.html",
        #                        caldata=caldata,
        #                        mincaltime=calminmax['min'],
        #                        maxcaltime=calminmax['max'],
        #                        version=config.VERSION)


@APP.route('/fire', methods=["GET"])
def web_fire():
    T.fire()


if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True, port=9999, threaded=False)
