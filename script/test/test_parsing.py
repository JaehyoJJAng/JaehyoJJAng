from __init__ import parser,get_soup_obj,download_csv
from typing import Dict,List
import requests as rq
import os
import unittest

class ParsingTest(unittest.TestCase):
    def test_get_soup_obj(self):
        test_url : str = 'https://www.naver.com/'
        
        with rq.Session() as session:
            with session.get(url=test_url,headers={'user-agent':'Mozilla/5.0'}) as response:
                soup : bs = get_soup_obj(res=response)                
                self.assertIn('네이버',str(soup.text))
    
    def test_parser(self):
        results : List[Dict[str,str]] = parser()
        
        for result in results:
            for key,value in result.items():
                self.assertTrue(value)
    
    def test_download_csv(self):
        check : bool = os.path.isfile('/home/runner/work/JaehyoJJAng/JaehyoJJAng/csv/parsing.csv')
        self.assertTrue(check)
        
if __name__ == '__main__':
    unittest.main()