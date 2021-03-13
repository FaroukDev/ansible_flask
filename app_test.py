import unittest
import testing.postgresql
import psycopg2
from app import increment , showData , showCurentId, Flask
from flask_testing import TestCase
app = Flask(__name__)

class TestRoutesAnsible(unittest.TestCase):
    def test_increment(self):
        self.postgresql = testing.postgresql.Postgresql(port=5000)

    def test_some_json(self):
        response = self.app.get('/id')
        print(response.data)
    
 
if __name__ == '__main__':
    unittest.main()