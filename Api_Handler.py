import requests
import json

class Api_Handler:
    KEY = ""
    MAX_NUMBER_RECORDS_RETURNED = 100

    def __init__(self):
        with open('key.txt', 'r') as file:
            Api_Handler.KEY = file.read().strip()

    def run(self):
        response, locations = self._call_api()
        records_available = int(response['recordsAvailable'])

        # If we need to loop for this zipcode
        if records_available > Api_Handler.MAX_NUMBER_RECORDS_RETURNED:
            offset = Api_Handler.MAX_NUMBER_RECORDS_RETURNED
            while offset < records_available:
                _, temp_locations = self._call_api(offset)
                locations.append(temp_locations)
                offset += Api_Handler.MAX_NUMBER_RECORDS_RETURNED
        return locations

    '''
    Calls Co-Op API.
    param: offset; offset as viewed by Co-Op. If offset = 0, result = [1,100]. If offset = 100, result = [101, 200]
    return: BeautifulSoup list of locations, number of records if offset = 0, else just locations list.
    '''
    def _call_api(self, offset=0):
        r = requests.get('https://api.co-opfs.org/locator/proximitysearch', params={'zip':'98122', 'offset': str(offset)}, headers={'Accept':'application/json', 'Version':'1', 'Authorization': Api_Handler.KEY})
        r_json = json.loads(r.text)
        result_info, locations = r_json['response']['resultInfo'], r_json['response']['locations']
        return result_info, locations
        