from bs4 import BeautifulSoup as bs
import requests as rq
import os
import csv

class Parser():
    def __init__(self) -> None:
        self.base_url: str = 'https://jaehyojjang.dev'
        self.headers: dict[str,str] = {'user-agent': 'Mozilla/5.0'}
    
    @staticmethod
    def get_soup_object(response: rq.Response) -> bs:
        return bs(response.text,'html.parser')
    
    def parsing(self) -> list[dict[str,str]]:
        # List
        save_list : list[dict[str,str]] = list()
        
        with rq.Session() as session:
            with session.get(url=self.base_url,headers=self.headers) as response:
                # Get soup Object
                soup : bs = self.get_soup_object(response=response)
                
                # Get items
                item_length : int = len(soup.select('div.list__item'))
                
                for idx in range(item_length):
                    # Dictionary
                    save_dict : dict[str,str] = dict()
                    
                    # Get Items
                    items : list[bs] = soup.select('div.list__item')

                    # Get link
                    link : str = self.base_url + items[idx].select_one('h2 > a').attrs['href']
                    
                    # Get title
                    title : str = items[idx].select_one('h2 > a').text.strip()
                    
                    # Get date
                    dated : str = items[idx].select_one('p.page__meta time').text.strip()
                    
                    save_dict['text'] = f'[{title}]({link}) -'
                    save_dict['dated'] = dated
                    save_list.append(save_dict)
        return save_list

class CSV():
    def __init__(self,save_path: str, file_name: str) -> None:
        self.parser : Parser = Parser()
        self.save_path = save_path
        self.file_name = file_name

    def upload_data_to_csv(self) -> None:
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path) 
    
        # Get results
        results : list[dict[str,str]] = self.parser.parsing()
        
        # Get reverse length
        leng : list[str] = list(reversed([_ for _ in range(len(results))]))
        
        with open(self.file_name,'w',newline='') as fp:
            writer = csv.writer(fp)
            for r_idx in leng:
                writer.writerow([results[r_idx]['text'],results[r_idx]['dated']])
                print(f'{results[r_idx]}\n')

def main() -> None:
    # Set Path & file name
    save_path : str = 'csv/'
    file_name : str = os.path.join(save_path,'parsing.csv')
    
    # Create CSV Instance
    csv : CSV = CSV(save_path=save_path,file_name=file_name)
    
    csv.upload_data_to_csv()

if __name__ == '__main__':
    main()
