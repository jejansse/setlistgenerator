from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_site():
	return "Setlist Generator"


@app.route("/solve")
def solve():
	return None


if __name__ == "__main__":
	app.run(debug=True)