from logging import log
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

from routes.user_bp import user_bp

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
db.init_app(app)


app.register_blueprint(user_bp, url_prefix='/api/users')

if __name__ in '__main__':
    app.run()
