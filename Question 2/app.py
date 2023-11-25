import os

from flask import Flask

from routes.main_routes import main_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
