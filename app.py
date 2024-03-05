from flask import Flask,jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app,resources={r"/api/*":{"origins":"*"}}) 

# Configuración para servir los archivos estáticos de React
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data',methods=['GET'])
def get_data():
    data = {
        "message":"Hello this is api end point"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

