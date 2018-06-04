import json
import requests
from unittest import TestCase
from unittest import main

from constants import (TEST_DATA, DEVICE_FIELDS, SUCCESS)


class APITest( TestCase ):

    db = None
    device_endpoint = "http://127.0.0.1:8888/device/"

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        print("------test is over------")

    def test_create(self):
        values = {
            "device_uuid": "b21ad0676f26439482cc9b1c8e827ce4",
            "sensor_type": "temperature",
            "sensor_value": 50,
            "sensor_reading_time": 1510094202
        }

        resp = requests.post(self.device_endpoint,
                             json=values)
        self.assertTrue(resp.text)

        resp_json = json.loads(resp.text)
        self.assertEqual(resp_json.get('status'), SUCCESS)
        self.assertTrue(resp_json.get('response'))
        for field_name in DEVICE_FIELDS:
            self.assertTrue(resp_json['response'].get(field_name))

    def test_lookup(self):
        values = {
            "device_uuid": "b21ad0676f26439482cc9b1c8e827ce4",
            "sensor_type": "temperature",
            "start_time": 1510094202,
            "end_time":   1510095202,
        }

        resp = requests.get(self.device_endpoint,
                            params=values)
        self.assertTrue(resp.text)

        resp_json = json.loads(resp.text)
        self.assertEqual(resp_json.get('status'), SUCCESS)
        self.assertTrue(resp_json.get('response'))
        for record in resp_json['response']:
            for field_name in DEVICE_FIELDS:
                self.assertTrue(record.get(field_name))


if __name__ == "__main__":
    main()