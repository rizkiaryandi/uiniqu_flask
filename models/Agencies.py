from config.uiniqu import db
import uuid
import datetime


class Agencies(db.Model):
    uuid = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    agency_name = db.columns.Text()
    agency_detail = db.columns.Text()
    created_by = db.columns.UUID()
    created_at = db.columns.DateTime(default=datetime.datetime.now())
    updated_at = db.columns.DateTime()
# db.sync_db()