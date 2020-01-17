import pyodbc
from NormalizedDB.Locations_Table import Locations_Table
from NormalizedDB.Contacts_Table import Contacts_Table
from NormalizedDB.SpecialQualities_Table import SpecialQualities_Table
from NormalizedDB.HoursPerDayOfTheWeek_Table import HoursPerDayOfTheWeek_Table
from Sql_Enums import Sql_Commands, Sql_Tables

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

    def execute_sql_command(self, cmd_type, table=None, location=None):
        if table is Sql_Tables.Locations: self.execute_locations_sql(cmd_type, location)
        elif table is Sql_Tables.Contacts: self.execute_contacts_sql(cmd_type, location)
        elif table is Sql_Tables.SpecialQualities: self.execute_special_qualities_sql(cmd_type, location)
        elif table is Sql_Tables.HoursPerDayOfTheWeek: self.execute_hours_per_day_of_the_week(cmd_type, location)
        elif table is None: return
        else:
            print("TABLE DOES NOT EXIST".format())

    def execute_locations_sql(self, cmd_type, location):
        cmd = None
        if cmd_type is Sql_Commands.CREATE:
            cmd = self.locations_table.get_create_table()
        elif cmd_type is Sql_Commands.INSERT:
            cmd = self.locations_table.get_insert_row(location)
        else: return
        self.commit_command(cmd)

    def execute_contacts_sql(self, cmd_type, location):
        cmd = None
        if cmd_type is Sql_Commands.CREATE:
            cmd = self.contacts_table.get_create_table()
        else: return
        self.commit_command(cmd)

    def execute_special_qualities_sql(self, cmd_type, location):
        cmd = None
        if cmd_type is Sql_Commands.CREATE:
            cmd = self.special_qualities_table.get_create_table()
        else: return
        self.commit_command(cmd)

    def execute_hours_per_day_of_the_week(self, cmd_type, location):
        cmd = None
        if cmd_type is Sql_Commands.CREATE:
            cmd = self.hours_per_day_of_the_week_table.get_create_table()
        else: return
        self.commit_command(cmd)

    def commit_command(self, cmd):
        with pyodbc.connect(self.connection_str) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(cmd)
                cursor.commit()
            # NB : you won't get an IntegrityError when reading
            except (pyodbc.ProgrammingError, pyodbc.Error)  as e:
                    if e[0] == '42S01':
                        print("Object has already been created")
                    pass