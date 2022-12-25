from config.uiniqu import db
import uuid
import datetime


# membuat schema model Tadarus
class Tadarus(db.Model):
    uuid = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    user_uid = db.columns.UUID(primary_key=True)
    surah_name = db.columns.Text()
    surah_number = db.columns.Integer()
    ayah_number = db.columns.Integer()
    created_at = db.columns.DateTime(default=datetime.datetime.now())
# db.sync_db()