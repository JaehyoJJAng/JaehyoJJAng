from typing import Dict,List
from bs4 import BeautifulSoup as bs
import requests as rq
import os  
import csv 

RESULTS = List[Dict[str,str]]

class Parser:
    def __init__(self,url:str) -> None:
        self.url = url
        self._headers : Dict[str,str] = {'user-agent': 'Mozilla/5.0'}
        
    @staticmethod
    def get_soup_object(res:rq.Response)-> bs:
        return bs(res.text,'html.parser')

    def parsing(self)-> RESULTS:
        # data on list
        save_list : RESULTS = []
        
        with rq.Session() as session:
            with session.get(url=self.url,headers=self._headers) as response:
                if response.ok:
                    soup : bs = self.get_soup_object(res=response)
                    
                    # Get content length
                    content_length : int = len(soup.select('li.list_horizontal_item',limit=5))
                    
                    for idx in range(content_length):
                        # data on dict
                        save_dict : Dict[str,str] = {}
                        
                        # Get Content
                        contents : list = soup.select('li.list_horizontal_item',limit=5)
                        
                        # 제목
                        title : str = contents[idx].select_one('strong.title_post').text.strip().replace(',','')
                        
                        # 날짜
                        dated : str = contents[idx].select_one('.date').text.strip().split(' ')[0].replace('.','-')

                        # 링크
                        link : str = "https://www.waytothem.com" + contents[idx].select_one('.link_article').attrs['href']
                        
                        save_dict['text'] = f"[{title}]({link}) -"
                        save_dict['dated'] = dated
                        save_list.append(save_dict)
                    return save_list     
            
class CSV(Parser):
    def __init__(self,url:str,save_path:str,file_name:str) -> None:
        super().__init__(url=url)
        self.save_path = save_path
        self.file_name = file_name

    def upload_data_to_csv(self)-> None:
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)
        
        # Get results
        results : RESULTS = self.parsing()
        
        leng : List[str] = [v for v in range(len(results))]
        leng.reverse()        
        
        with open(self.file_name,'w',newline='') as fp:
            writer = csv.writer(fp)
            for r_idx in leng:
                writer.writerow([results[r_idx]['text'],results[r_idx]['dated']])
                print(f'{results[r_idx]}\n')

def main()-> None: 
    url : str = 'https://waytothem.com/blog/'
    
    save_path : str = 'csv/'
    file_name : str = os.path.join(save_path,'parsing.csv')

    # Create CSV instance
    csv : CSV = CSV(url=url,save_path=save_path,file_name=file_name)    
    csv.upload_data_to_csv()
    
if __name__ == '__main__':
    main()