from tests.system.base_test import BaseTest
import json

class TestHome(BaseTest):
    
    def test_home(self):
        
        expected_dict = {'message': 'Hello, world!'}
        
        with self.app as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(
                json.loads(resp.get_data()) , 
                expected_dict)
