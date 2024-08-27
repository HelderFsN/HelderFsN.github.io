from frask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return "Tá funcionando o Flask"

if __name__ == '__main__':
	app.run()