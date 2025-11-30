import json

import pytest

from source.api.utils.AipHelper import AipHelper
from source.genericUtil.configurationManager import ConfigurationManager
import logging


@pytest.fixture
def setUp():
    apihelper = AipHelper(timeout=5)
    config = ConfigurationManager
    yield apihelper,config


def test_getBooking(setUp):
    apihelper, config = setUp
    response=apihelper.getCall(config.getProperty('baseurl')+config.getProperty('get_bookings'))
    assert response.status_code == 200

def test_createBooking(setUp):
    apihelper, config = setUp
    jsonBody='''
    {
    "firstname" : "KimPra",
    "lastname" : "Brownee",
    "totalprice" : 121,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
} '''
    print(config.getProperty('baseurl')+config.getProperty('post_booking'))
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    print(headers)
    createBookingresponse=apihelper.postCall(config.getProperty('baseurl')+config.getProperty('post_booking'),json=json.loads(jsonBody),headers=headers)
    assert createBookingresponse.status_code == 200
    startNode = json.loads(apihelper.getResponseAsText(createBookingresponse))
    print(startNode)
    actuallBody = json.loads(jsonBody)
    print( startNode['bookingid'])
    assert startNode['booking']['firstname'] == actuallBody['firstname']
    print(startNode['booking']['bookingdates'])
