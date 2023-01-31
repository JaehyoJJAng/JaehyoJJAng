from bs4 import BeautifulSoup as bs
from typing  import List,Dict
import requests as rq
import os
import csv
 
def get_soup_obj(res)-> bs:
    """ Soup 객체 리턴 """
    return bs(res.text,'html.parser')

def parser()-> List[Dict[str,str]]:
    """ soup 파싱 """
    URL : str = "https://waytothem.com/blog/"
    save_data : List[Dict[str,str]] = list()
    with rq.Session() as session:
        with session.get(url=URL) as response:
            if response.ok:
                soup=get_soup_obj(res=response)
            
                content_length : int = len(soup.select('li.list_horizontal_item',limit=5))
                for idx in range(content_length):
                    dataDic : Dict[str,str] = dict()
                    contents : list = soup.select('li.list_horizontal_item',limit=5)
                    
                    # 제목
                    title : str = contents[idx].select_one('strong.title_post').text.strip()
                    
                    # 날짜
                    dated : str = contents[idx].select_one('.date').text.strip().split(' ')[0].replace('.','-')

                    # 링크
                    link : str = "https://www.waytothem.com" + contents[idx].select_one('.link_article').attrs['href']
                    
                    dataDic['text'] = f"[{title}]({link}) -"
                    dataDic['dated'] = dated
                    save_data.append(dataDic)
                return save_data
                    
def main()-> None:
    results : List[Dict[str,str]] = parser()

    download_csv(results=results)

def download_csv(results: list)-> None:
    savePath = os.path.abspath('/home/wogy12395/github/JaehyoJJAng/csv')
    fileName = os.path.join(savePath,'parsing.csv')

    if not os.path.exists(savePath):
        os.mkdir(savePath)
        
    leng : List[int] = [v for v in range(len(results))]
    leng.reverse()

    with open(fileName,'w',newline='') as fp:
        writer = csv.writer(fp)
        for r_idx in leng :
            writer.writerow([results[r_idx]['text'],results[r_idx]['dated']])
            print(f"{results[r_idx]}\n데이터 삽입 완료!\n")

if __name__ == '__main__':
    main()

