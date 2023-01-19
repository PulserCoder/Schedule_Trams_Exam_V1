import json
import datetime
import config


def load_all_info() -> list:
    """Return all data from json"""
    with open('data1.json') as file:
        return json.load(file)


def load_info_by_days(day: str) -> list:
    """Return departure by day (weekend, weekday, everyday) from json"""
    ll = []
    for depart in load_all_info():
        if day == depart['days'] or depart['days'] == 'ежедн.':
            ll.append(depart)
    return ll


def load_info_by_station(station: str) -> list:
    """Return departure by station from json"""
    ll = []
    for depart in load_all_info():
        if station.lower() == depart['station'].lower():
            ll.append(depart)
    return ll


def load_info_by_time() -> list:
    """Return departure by now time"""
    ll = []
    if datetime.datetime.today().weekday() in config.weekdays:
        for i in load_info_by_days('раб.'):
            ll.append(i)
    elif datetime.datetime.today().weekday() in config.weekends:
        for i in load_info_by_days('вых.'):
            ll.append(i)
    return ll


def load_info_by_nowtime() -> list:
    """Return departure which are after nowtime"""
    ll = []
    time = list(map(int, str(datetime.datetime.today().time()).split(':')[:2]))
    for i in load_info_by_time():
        time_departure = list(map(int, i['departure'].split(':')))
        if time_departure[0] > time[0] or time_departure[0] == time[0] and time_departure[1] > time[1]:
            ll.append(i)
    return ll

