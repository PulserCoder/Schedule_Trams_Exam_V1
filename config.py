import json
from random import choice

#  Config data
weekdays = [0, 1, 2, 3, 4]
weekends = [5, 6]


def add_pk():
    """Load to our json new pk (id)"""
    ll = []
    t = list(range(0, 455))
    for i in json.load(open('data1.json')):
        i['pk'] = choice(t)
        ll.append(i)
    json.dump(ll, open('data1.json', 'w'))


if __name__ == '__main__':
    add_pk()
