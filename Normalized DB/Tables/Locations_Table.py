class Locations_Table:
    CREATE_LOCATIONS_TABLE = """CREATE TABLE Locations(
	LocationID varchar(64) NOT NULL PRIMARY KEY,
	CoopLocationId varchar(64) NULL,
	TakeCoopData bit NULL,
	SoftDelete bit NULL,
	Name varchar(64) NULL,
	Address varchar(64) NOT NULL,
	City varchar(64) NOT NULL,
	County varchar(64) NULL,
	State varchar(64) NOT NULL,
	PostalCode varchar(64) NULL,
	Country varchar(64) NULL,
	Latitude decimal(9, 6) NULL,
	Longitude decimal(9, 6) NULL,
	Hours varchar(64) NULL,
	RetailOutlet varchar(64) NULL,
	LocationType varchar(64) NULL);"""

    def get_create_table(self):
        return Locations_Table.CREATE_LOCATIONS_TABLE