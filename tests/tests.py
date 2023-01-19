import pytest
from utils import *


def test_load_all_info():
    assert type(load_all_info()) == list
    assert type(load_all_info()[0]) == dict
    assert load_all_info()[0]['departure'] == '0:10'


def test_load_info_by_days():
    assert type(load_info_by_days('раб.')) == list
    assert type(load_info_by_days('раб.')[0]) == dict
    assert load_info_by_days('раб.')[0]['departure'] == '0:10'


def test_load_info_by_station():
    assert type(load_info_by_station('Жел-дор')) == list
    assert type(load_info_by_station('Жел-дор')[0]) == dict
    assert load_info_by_station('Жел-дор')[0]['departure'] == '0:40'


def test_load_info_by_time():
    assert type(load_info_by_time()) == list
    assert type(load_info_by_time()[0]) == dict
    assert load_info_by_time()[0]['departure'] == '0:10'


def test_load_info_by_nowtime():
    assert type(load_info_by_time()) == list
    assert type(load_info_by_time()[0]) == dict
