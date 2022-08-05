import unittest
import requests
import yaml
from nose.tools import assert_true
from unittest.mock import patch
from api import FindNextBus


config = yaml.safe_load(open("./config.yaml"))

BASEURL = config["baseurl"]

class TestNextBus(unittest.TestCase):

    def test_request_response(self):
        resp = requests.get(BASEURL.format('Routes'))
        assert_true(resp.ok)

    def test_parse_datetime(self):
        testDate1 = "/Date(1659664620000-0500)/"
        testDate2 = "/Date(1659664620000+0500)/"
        testDate3 = "/Date(1659664620000)/"
        print(type(FindNextBus.parse_datetime(self,testDate1)))
        self.assertEqual(type(FindNextBus.parse_datetime(self,testDate1)),int)
        self.assertEqual(type(FindNextBus.parse_datetime(self,testDate2)),int)
        self.assertEqual(type(FindNextBus.parse_datetime(self,testDate3)),int)
        


if __name__ == "__main__":
    unittest.main()
        