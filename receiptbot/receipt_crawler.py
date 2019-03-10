import requests

etax_url = "https://www.etax.nat.gov.tw/etw-main/web/ETW183W1/"


def get_web_page(url):
    resp = requests.get(url=url)
    if resp.status_code != 200:
        print('invalid url', resp.url)
        return None
    else:
        resp.encoding = "UTF-8"
        return resp.text


current_page = get_web_page(etax_url)


print(current_page)
