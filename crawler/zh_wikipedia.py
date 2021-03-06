import numpy as np
import pandas as pd
import os
import json


def _get(url):
    try:
        import requests
        proxies = {"http": "http://68.183.34.61"}

        return requests.get(url, proxies=proxies)
    except ImportError:
        pass
    except Exception as e:
        print(e, 'from', url)


def _parse(r):
    if r is None:
        return
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, 'lxml')
    [c.extract() for c in soup('sup')]

    s = ''
    metadata = []
    for content in soup.select("[class~=mw-parser-output]"):
        s += content.p.get_text()
        for card in content.select(".vcard"):

            for tr in card.select("tr"):
                t = []
                for th in tr.select("th[scope='row']"):
                    t.append(th.get_text())
                for td in tr.select("td"):
                    td_list = []
                    for con in td.contents:
                        if con.string is None:
                            continue
                        td_list.append(con.string)
                    td_str = " ".join(td_list)
                    td_str = td_str.replace("  ", " ")
                    t.append(td_str)
                metadata.append(t)

        return s.strip(), pd.DataFrame(metadata).replace(to_replace=r'^\s*$', value=np.nan, regex=True).dropna(axis=0)


def get_companies_info(url_list=None):
    if url_list is None:
        raise ValueError('The url list should not be empty.')
    os.mkdir("./companies_wikipedia/json_folder_zh")
    os.chdir("./companies_wikipedia/json_folder_zh")
    for url in url_list:
        par = _parse(_get(url))
        data = {
            'url': url,
            'name': url.split('/')[-1],
            'description': par[0],
            'metadata': par[1].to_dict()
        }
        print(data)
        with open(url.split('/')[-1] + '.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)


get_companies_info(["https://zh.wikipedia.org/wiki/蚂蚁金服", "https://zh.wikipedia.org/wiki/众安保险", "https://zh.wikipedia.org/wiki/%E6%BD%AE%E6%B1%90", "https://zh.wikipedia.org/wiki/%E8%85%BE%E8%AE%AF"])
