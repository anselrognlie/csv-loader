from app import db
from app.models.user import User
from app.models.role import Role
import csv

def seed():
    role_uuids = {}
    with open("data/roles.csv") as csvfile:
        roles = csv.DictReader(csvfile)
        for row in roles:
            # print(f"{row['name']=},{row['uuid']=}")
            record = Role(name=row['name'], uuid=row['uuid'])
            db.session.add(record)
            role_uuids[row['uuid']] = record
        db.session.commit()

    with open("data/users.csv") as csvfile:
        users = csv.DictReader(csvfile)
        for row in users:
            # print(f"{row['display_name']=},{row['email']=},{row['role_uuid']=}")
            record = User(
                display_name=row['display_name'], 
                email=row['email'], 
            )
            record.role = role_uuids[row['role_uuid']]
            db.session.add(record)
        db.session.commit()
