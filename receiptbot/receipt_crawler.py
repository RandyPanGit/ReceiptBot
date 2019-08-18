import re

import requests
from bs4 import BeautifulSoup

home_url = "https://www.etax.nat.gov.tw"
etax_url = "https://www.etax.nat.gov.tw/etw-main/web/ETW183W1/"


def get_web_page(url):
    resp = requests.get(url=url)
    if resp.status_code != 200:
        return None
    else:
        resp.encoding = "UTF-8"
        return resp.text


def get_hrefs(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    links = soup.find_all(href=re.compile("^/etw-main/web/ETW183W2_*"), limit=3)
    return links


def get_months(resultSet):
    months = []
    for tag in resultSet:
        months.append(tag.text)
    return months


def get_receipt_deatil(resultSet, uri):
    for tag in resultSet:
        if tag.text == uri:
            detail_patge = get_web_page(home_url + tag.get('href'))


current_page = get_web_page(etax_url)


if current_page:
    a_tags = get_hrefs(current_page)
    months = get_months(a_tags)
    get_receipt_deatil(a_tags, months[0])
    # next_url = "https://www.etax.nat.gov.tw" + a_tags[0]['href']
    # new_web = get_web_page(next_url)
    # print(new_web)
