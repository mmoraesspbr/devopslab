
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Marcelo 23/03/2023 - Pipeline DevOps - v1"

if __name__ == '__main__':
    app.run()