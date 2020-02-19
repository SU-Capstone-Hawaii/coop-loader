import sys
import os

sys.path.append(os.path.join(os.getcwd(), "NormalizedDB"))
sys.path.append("Lib\site-packages")
sys.path.append(os.getcwd())
#sys.path.append(".")

import requests
import pypyodbc as pyodbc
from Api_Handler import Api_Handler
from NormalizedDB import *
import Locations_Table
import Contacts_Table
import SpecialQualities_Table
import DailyHours_Table
from aenum import Enum, auto
from Sql_Enums import Sql_Commands, Sql_Tables
import uuid


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