#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask, Response, make_response, url_for, render_template, request,session, redirect
import requests
from  bs4 import BeautifulSoup
app = Flask(__name__)
app.debug = True
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
@app.route("/login", methods=["POST","GET"])
def login():
	if request.method == "POST":
		session_check = request.form.get("uname", None)	
		if None == session_check:
			if "logged_in" in session:
				if True == session["logged_in"]:
					return session["uname"] + "님 환영합니다"

			return login_test()
	
		if request.form["uname"] == "iott":
				if request.form["passwd"] =="2019":
					session["logged_in"] = True
					session["uname"] = request.form["uname"]
			
					return request.form["uname"] + "님 환영합니다"
		
		return "로그인 실패"
	else:
		if "logged_session" in session:
			if True == session["logged_in"]:	

				return	session["uname"] +"님 환영 합니다"
		return login_test()
app.secret_key = "iot_key"

@app.route("/logout")
def logout():
	session["logged_in"] - False
	session.pop("uname", None)
	return "로그아웃 되셨습니다"
@app.route("/template")
@app.route("/template/")
@app.route("/template/<iot_number>")
def template_test(iot_number = None):
	iot_member = ["최성주", "jusuhong","최재원"]
	return render_template( "template_test.html",iot_number = iot_number, iot_member=iot_member)
@app.route("/iot")
@app.route("/iot/")
def iot():
#	result_req = requests.get("http://btc.ac.kr/p/j=41")

#	result_req = requests.get("https://media.daum.net/ranking/bestreply/")
	result_req = requests.get("https://naver.com/")
	result_txt = result_req.text
	result_head = result_req.headers
	result_status = result_req.status_code
	if True == result_req.ok:
		obj_soup = BeautifulSoup(result_txt , "html.parser")
#		iot_data =obj_soup.select("table.ej-tbj>tbody>tr>td>a")
#		iot_data =obj_soup.select("div.cont_thumb>strong.tit_thumb>a")
		iot_data =obj_soup.select("div#news_cast>div.area_newstop>div.cast_flash>h3.cf_tit>a")
		return render_template("main.html",iot_data = iot_data)
	else:
		return "가져오기 오류"
@app.route("/gugu")
@app.route("/gugu/")
@app.route("/gugu/<int:iot_num>")
def iotgugu(iot_num=None):
	return render_template("gugu.html", iot_num = iot_num)
@app.route("/calcul", methods = ["POST"])
def calcul(iot_num = None):
	if request.method == "POST":
		if "" == request.form["iot_num"]:
			cal_num= None
		else:
			cal_num= request.form["iot_num"]
	else:
		cal_num = None

	return redirect(url_for("iotgugu",iot_num=cal_num))


@app.route("/")
def IoT_http_prepost_response():
	return "<img src=" + url_for("static", filename = "1.jpg") + ">"


if __name__ == "__main__":

	app.run(host = "192.168.0.206")

