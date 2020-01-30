import requests
import json

class Api_Handler:
    KEY = ""
    MAX_NUMBER_RECORDS_RETURNED = 100

    '''
    Constructor
    SUMMARY:
    Reads CO-OP API key from key.txt (contained in root directory). key.txt contains 1 line: the API key
    '''
    def __init__(self):
        with open('key.txt', 'r') as file:
            Api_Handler.KEY = file.read().strip()

    '''
    SUMMARY:
    Run driver. This calls _call_api() helper function. 
        Step 1: Initial call to helper function returns the API response and list of locations as a list 
                of JSON objects. 
        Step 2: Check how many records are available (in this case checking for locations in zipcode 98122)
        Step 3a: If more locations in zipcode than were returned, continue calling _call_api() helper 
                function with offset parameter set. API returns **MAX** 100 records at a time, so to get
                records 101-200, the method call is _call_api(100)
        Step 3b: Add new records to locations list and increment offset. Loop again as necessary.
        Step 4: Return locations list.
    RETURN:
    List of locations. Each location in list is a Python Dictionary (like C# key,value pair). Keys are as
    documented in the CO-OP API documentation.
    '''
    def run(self):
        response, locations = self._call_api()
        records_available = int(response['recordsAvailable'])

        # If we need to loop for this zipcode
        if records_available > Api_Handler.MAX_NUMBER_RECORDS_RETURNED:
            offset = Api_Handler.MAX_NUMBER_RECORDS_RETURNED
            while offset < records_available:
                _, temp_locations = self._call_api(offset)
                locations += temp_locations
                offset += Api_Handler.MAX_NUMBER_RECORDS_RETURNED
        return locations

    '''
    SUMMARY:
    Helper function. Calls Co-Op API.
    param: offset; offset as viewed by Co-Op. If offset = 0, result = [1,100]. If offset = 100, result = [101, 200]
    return: List of locations, number of records if offset = 0, else just locations list.
    '''
    def _call_api(self, offset=0):
        r = requests.get('https://api.co-opfs.org/locator/proximitysearch', params={'zip':'98122', 'offset': str(offset)}, headers={'Accept':'application/json', 'Version':'1', 'Authorization': Api_Handler.KEY})
        r_json = json.loads(r.text)
        result_info, locations = r_json['response']['resultInfo'], r_json['response']['locations']
        return result_info, locations
        