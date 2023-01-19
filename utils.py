import json
from datetime import datetime


class Utils:
    """Класс Utils представляет собой вспомогательные функции"""

    @staticmethod
    def load_data(file_name):
        """Метод класса Utils, который загружает все данные"""
        with open(file_name, encoding='utf-8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def weekdays():
        """Метод класса Utils, который определяет сегодняшний день недели"""
        number_of_day = datetime.isoweekday(datetime.now())
        if number_of_day == 1:
            return 'пн', 'вт'
        elif number_of_day == 2:
            return 'вт', 'ср'
        elif number_of_day == 3:
            return 'ср', 'чт'
        elif number_of_day == 4:
            return 'чт', 'пт'
        elif number_of_day == 5:
            return 'пт', 'сб'
        elif number_of_day == 6:
            return 'сб', 'вс'
        else:
            return 'вс', 'пн'

    @staticmethod
    def print_subjects(weekday):
        """Метод класса Utils, который выводит список занятий на сегодня и завтра"""
        today = []
        tomorrow = []
        for sub in Utils.load_data("data.json"):
            if weekday[0] == sub["day_week"]:
                today.append(sub)
            if weekday[1] == sub["day_week"]:
                tomorrow.append(sub)
        return today, tomorrow

    @staticmethod
    def find_weekday_by_subject(discipline):
        """Метод класса Utils, который возвращает все занятия по одной дисциплине в неделю"""
        weekdays = []
        for sub in Utils.load_data("data.json"):
            if discipline == sub["discipline"]:
                weekdays.append(sub)
        return weekdays
