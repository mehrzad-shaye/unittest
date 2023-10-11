import unittest
import json
from flask import request

from app import app


class TestApi(unittest, unittest.TestCase):

    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post(
                '/ner', json={"sentense": "steve Malkmu is in a god band"})
            assert response._status_code == 200

    def test_ner_endpoint_given_json_body_with_known_entities_returns_result_in_response(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentense": "Kamala Harris"})
            data = json.loads(response.get_data())
            assert data['entities'][0]['ents'] == 'Kamala Harris'
            assert data['entities'][0]['Label'] == 'Person'
