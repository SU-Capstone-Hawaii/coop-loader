import pyodbc
from NormalizedDB.Locations_Table import Locations_Table
from NormalizedDB.Contacts_Table import Contacts_Table
from NormalizedDB.SpecialQualities_Table import SpecialQualities_Table
from NormalizedDB.HoursPerDayOfTheWeek_Table import HoursPerDayOfTheWeek_Table
from Sql_Enums import Sql_Commands, Sql_Tables
import time

class Maphawks_Db_Handler:

    def __init__(self):
        with open('./NormalizedDb/db_connection_str.txt') as file:
            self.connection_str = file.read().strip()
        self.locations_table = Locations_Table()
        self.contacts_table = Contacts_Table()
        self.special_qualities_table = SpecialQualities_Table()
        self.hours_per_day_of_the_week_table = HoursPerDayOfTheWeek_Table()
    
    def create_tables(self):
        # Create tables in DB
        self.execute_sql_command(Sql_Commands.CREATE, Sql_Tables.Locations)
        self.execute_sql_command(Sql_Commands.CREATE, Sql_Tables.Contacts)
        self.execute_sql_command(Sql_Commands.CREATE, Sql_Tables.SpecialQualities)
        self.execute_sql_command(Sql_Commands.CREATE, Sql_Tables.HoursPerDayOfTheWeek)
    
    def insert_into_db(self, locations):
        for location in locations:
            for table in Sql_Tables:
                self.execute_sql_command(Sql_Commands.INSERT, table, location)
    
    '''
    Determines type of sql command and calls corresponding method.
    In case of SELECT command, table is an array, otherwise, table can be assumed to refer to only 1 table
    '''
    def execute_sql_command(self, cmd_type, table=None, location=None, columns=None):
        if cmd_type is Sql_Commands.CREATE: self.execute_create(table) # Create a new table
        elif cmd_type is Sql_Commands.INSERT: self.execute_insert(location) # Insert new row into table
        elif cmd_type is Sql_Commands.SELECT: self.execute_sql_command(table, columns)
        else: print("SQL Command: {} is not supported".format(str(cmd_type)))

    def execute_create(self, table):
        commit_status = None
        while commit_status is not True:
            if table is Sql_Tables.Locations: cmd = self.locations_table.get_create_table()
            elif table is Sql_Tables.Contacts: cmd = self.contacts_table.get_create_table()
            elif table is Sql_Tables.SpecialQualities: cmd = self.special_qualities_table.get_create_table()
            elif table is Sql_Tables.HoursPerDayOfTheWeek: cmd = self.hours_per_day_of_the_week_table.get_create_table()
            else: 
                print("TABLE {} DOES NOT EXIST".format(str(table)))
                return
            commit_status = self.commit_command([cmd])
    
    '''
    Inserts a row for arg:location into all Sql_Tables
    '''
    def execute_insert(self, location):
        commit_status = None
        while commit_status is not True:
            cmd_locations, locationId = self.locations_table.get_insert_row(location)
            cmd_contacts = self.contacts_table.get_insert_row(location, locationId)
            cmd_special_qualities = self.special_qualities_table.get_insert_row(location, locationId)
            cmd_hours = self.hours_per_day_of_the_week_table.get_insert_row(location, locationId)
            commit_status = self.commit_command([cmd_locations, cmd_contacts, cmd_special_qualities, cmd_hours])

    def commit_command(self, cmds):
        for cmd in cmds:
            print(cmd)
            time.sleep(1)
        return True
        '''
        with pyodbc.connect(self.connection_str) as conn:
            cursor = conn.cursor()
            try:
                for cmd in cmds:
                    cursor.execute(cmd)
                    cursor.commit()
                return True
            # NB : you won't get an IntegrityError when reading
            except (pyodbc.ProgrammingError, pyodbc.Error)  as e:
                    if e[0] == '42S01':
                        print("Object has already been created")
                    return False
        '''