from flask import Flask, Response, make_response, url_for

app = Flask(__name__)

@app.route('/board', methods=['GET'])
#def IoT_Board():
#	print("IoT_Board")
#	return "<img src=\"https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png\">"
def board_list_get():
	return"GET"
@app.route('/board', methods =['POST'])
def board_list_post():
	return"POST"
@app.route("/")
def IoT_http_prepost_response():


	return "<img src=" + url_for("static", filename = "1.jpg") + ">"


if __name__ == "__main__":

	app.run(host = "192.168.0.206")

