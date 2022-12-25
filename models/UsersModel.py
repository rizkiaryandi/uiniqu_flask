from config.uiniqu import db
import uuid
import datetime


# membuat schema model (login, register)
class Users(db.Model):
    uuid = db.columns.UUID(default=uuid.uuid4)
    username = db.columns.Text(primary_key=True)
    password = db.columns.Text()
    name = db.columns.Text()
    photo_url = db.columns.Text(default="")
    role = db.columns.Integer(default=1)
    created_at = db.columns.DateTime(default=datetime.datetime.now())
    updated_at = db.columns.DateTime(default=datetime.datetime.now())
# db.sync_db()