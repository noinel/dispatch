#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask,url_for, render_template


from subprocess import PIPE, Popen 
import psutil
import RPi.GPIO as GP
ledpin = 18
GP.setmode(GP.BCM)
GP.setup(ledpin, GP.OUT)

app = Flask(__name__)
app.debug = True

#===========================================================

def iot_measure_temp(): 
	process = Popen(["vcgencmd", "measure_temp"], stdout=PIPE) 
	output, _error = process.communicate() 
	return float(output[output.index("=") + 1:output.rindex("'")])

@app.route("/info")
def iot_sys_info():
#========================================================
	
	cpu_temp            = iot_measure_temp()
	cpu_percent         = psutil.cpu_percent() 
	cpu_count           = psutil.cpu_count()
#=======================================================

	memory              = psutil.virtual_memory()
	mem_total           = memory.total
	mem_percent			= memory.percent
#=======================================================

	hd_disk             = psutil.disk_usage("/")
	disk_percent		= hd_disk.percent
#======================================================

	iot_sys_info_dict = { "cpu 온도":cpu_temp,
							"cpu 사용률":cpu_percent,
							"cpu 코어 갯수":cpu_count,
							"전체 메모리":mem_total,
							"메모리 사용률":mem_percent,
							"디스크 사용률":disk_percent}
	return render_template("h_info.html", hw_info =iot_sys_info_dict)

@app.route("/led/<led_state>")
def led_onoff(led_state):
	if "on" == led_state:
		GP.output(ledpin,GP.LOW)
	if "off" == led_state:
		GP.output(ledpin,GP.HIGH)
	if "toggle" == led_state:
		GP.output(ledpin, not GP.input(ledpin))
	return iot_sys_info()

@app.route("/")
def IoT_http_prepost_response():
	return "<img src=" + url_for("static", filename = "1.jpg") + ">"


if __name__ == "__main__":

	app.run(host = "192.168.0.206")

