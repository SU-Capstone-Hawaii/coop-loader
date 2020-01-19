import uuid

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
	api_fields_corresponding_to_column_order = ['terminalId', 
		'NULL', 
		'NULL', 
		'institutionName', 
		'address', 
		'city', 
		'county', 
		'state', 
		'zip', 
		'country', 
		'latitude', 
		'longitude', 
		'hours_open_value', 
		'retailOutlet', 
		'locatorType']


	def get_create_table(self):
		return Locations_Table.CREATE_LOCATIONS_TABLE

	def get_insert_row(self, location):
		locationId = str(uuid.uuid4()) # BECU LocationId
		statement = "INSERT INTO Locations VALUES ({}, ".format(locationId)
		for api_field in Locations_Table.api_fields_corresponding_to_column_order:
			if api_field == 'NULL' or location[api_field] == '': statement += ', NULL'
			else:
				statement += ", {}".format(location[api_field])
		statement += ");"
		return statement, locationId

