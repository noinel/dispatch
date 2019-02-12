#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask, Response, make_response, url_for, render_template, request,session

app = Flask(__name__)
app.debug = False
@app.route("/login_test")
def login_test():
	return render_template('login.html')

@app.route("/log")
def IoT_logging_test():
	test_value = 20190211
	app.logger.debug("디버깅 시행 중")
	app.logger.warning(str(test_value) + "=====")
	app.logger.error("에러발생")
	return " 로거끝 "

@app.route("/user/<uname>")
def IoT_user_name(uname):
	return "User Name : %s" %uname

@app.route("/user/<int:num_id>")
def IoT_user_number_id(num_id):
	return "ID Number : %d" % num_id

@app.route('/board', methods=['GET'])
def board_list_get():
	return"GET"

@app.route('/board', methods =['POST'])
def board_list_post():
	return"POST"
@app.route("/get_test", methods=['GET'])
def get_test():
	if request.method == "GET":
		if(request.args.get("uname") == "iot"
				and request.args.get("passwd") =="2019"):
			return request.args.get("uname") + "님 환영합니다"
		else:
			return "로그인 실패"
	else:
		return "다시 시도해주십시오"

@app.route("/")
def IoT_http_prepost_response():
	return "<img src=" + url_for("static", filename = "1.jpg") + ">"


if __name__ == "__main__":

	app.run(host = "192.168.0.206")

