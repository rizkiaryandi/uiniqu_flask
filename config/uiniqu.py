# import library flask dkk

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_cqlalchemy import CQLAlchemy
import os

# inisialisasi objek flask dkk
app = Flask(__name__)
api = Api(app)
CORS(app)
SECRET_KEY = "AnJ4YBROWAKA1<4KAKA.!"

# konfigurasi database
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "latihan_1"
app.config['CASSANDRA_SETUP_KWARGS'] = {'protocol_version': 3, 'port': '9042'}
db = CQLAlchemy(app)

if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
    os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'