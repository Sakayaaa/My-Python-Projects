from sqlalchemy import Column, Integer, String, Date

from model.base import Base
from model.validation import name_validator, grade_validator, license_date_validator, license_no_validator


class License(Base):
    __tablename__ = 'licenses'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _grade = Column("grade", Integer)
    _license_date = Column("license_date", Date)
    _license_no = Column("license_no", Integer)

    def __init__(self, id, name, grade, license_date, license_no):
        self.id = id
        self.name = name
        self.grade = grade
        self.license_date = license_date
        self.license_no = license_no

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = name_validator(value)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = grade_validator(value)

    @property
    def license_date(self):
        return self._license_date

    @license_date.setter
    def license_date(self, value):
        self._license_date = license_date_validator(value)


    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = license_no_validator(value)