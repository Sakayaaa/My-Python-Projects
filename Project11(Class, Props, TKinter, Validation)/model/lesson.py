# from validation import *
from model.validation import time_validator, code_validator, day_validator, duration_validator, teacher_validator


class Lesson:
    def __init__(self, name, code, day, start_time, duration, teacher):
        self.name = name
        self.code = code
        self.day = day
        self.start_time = start_time
        self.duration = duration
        self.teacher = teacher

    # GETTER-SETTER
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = code_validator(value)

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = day_validator(value)

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = time_validator(value)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = duration_validator(value)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        self._teacher = teacher_validator(value)

    def to_tuple(self):
        return self.name, self.code, self.day, self._start_time, self.duration, self.teacher
