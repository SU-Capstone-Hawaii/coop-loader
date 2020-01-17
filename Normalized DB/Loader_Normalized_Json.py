from Api_Handler import Api_Handler
from Maphawks_Db_Handler import Maphawks_Db_Handler

'''
Checks if field is empty
param: field (string)
return: True or False
'''
def _is_empty(field):
    if len(field) == 0: return True
    return False

if __name__ == "__main__":
    maphawks_db = Maphawks_Db_Handler()
    maphawks_db.run()
    #api_handler = Api_Handler()
    #api_handler.get_key()
