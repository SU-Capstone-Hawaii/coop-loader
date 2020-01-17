import requests

class Api_Handler:
    KEY = ""

    '''
    Gets Co-Op API key from local txt file. This file contains one line, which is the API key.
    '''
    def get_key(self):
        with open('key.txt', 'r') as file:
            Api_Handler.KEY = file.read().strip()

    '''
    Calls Co-Op API.
    param: offset; offset as viewed by Co-Op. If offset = 0, result = [1,100]. If offset = 100, result = [101, 200]
    return: BeautifulSoup list of locations, number of records if offset = 0, else just locations list.
    '''
    def _call_api(self, offset=0):
        r = requests.get('https://api.co-opfs.org/locator/proximitysearch', params={'zip':'98122', 'offset': str(offset)}, headers={'Accept':'application/json', 'Version':'1', 'Authorization': Api_Handler.KEY})
        print(r)
        response, locations = r['response'], r['locations']
        