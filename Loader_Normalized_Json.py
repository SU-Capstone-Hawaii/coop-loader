from Api_Handler import Api_Handler
from NormalizedDB.Maphawks_Db_Handler import Maphawks_Db_Handler

'''
Checks if field is empty
param: field (string)
return: True or False
'''
def _is_empty(field):
    if len(field) == 0: return True
    return False

if __name__ == "__main__":
    # Create Tables
    maphawks_db = Maphawks_Db_Handler()
    maphawks_db.create_tables()
    
    # Call Co-Op API
    api_handler = Api_Handler()
    locations = api_handler.run()

    # Insert records
    maphawks_db.insert_into_db(locations)