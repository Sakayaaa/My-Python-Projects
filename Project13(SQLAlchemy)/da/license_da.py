from da.tools.database_manager import *
from model.license import License

session = get_session()


# DEFs RESPONSIBLE FOR ACTIONS ON TARGET TABLE IN MYSQL SERVER
def save(license):
    session.add(license)
    session.commit()


def edit(license):
    session.merge(license)
    session.commit()


def remove(license):
    license = session.query(License).get(license.id)
    session.delete(license)
    session.commit()


def find_all():
    return session.query(License).all()


def find_by_id(license_id):
    return session.query(License).get(license_id)


def find_by_name(name):
    return session.query(License).filter(License.name == name).all()
