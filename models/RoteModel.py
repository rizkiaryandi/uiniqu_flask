from config.uiniqu import db
import uuid
import datetime


class Rote(db.Model):
    uuid = db.columns.UUID(default=uuid.uuid4)
    user_uid = db.columns.UUID(primary_key=True)
    history = db.columns.Text()
    created_at = db.columns.DateTime(default=datetime.datetime.now())
# db.sync_db()