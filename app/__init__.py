from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inisialisasi Flask app
app = Flask(__name__)

# Konfigurasi aplikasi, seperti URI database
app.config.from_object('config')

# Inisialisasi database dengan SQLAlchemy
db = SQLAlchemy(app)

# Mengimpor routes setelah inisialisasi app dan db
from app import routes, models