from flask import Flask
import puzzle


# initialize the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'haha' # for session values


@app.route("/")
def main():
	return puzzle
