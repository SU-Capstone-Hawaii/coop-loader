import uuid

class Locations_Table:
	CREATE_LOCATIONS_TABLE = """CREATE TABLE Locations(
		LocationID varchar(64) NOT NULL PRIMARY KEY, 
		CoopLocationId varchar(64) NULL, 
		TakeCoopData bit NOT NULL, 
		SoftDelete bit NOT NULL, 
		Name varchar(64) NOT NULL, 
		Address varchar(64) NOT NULL, 
		City varchar(64) NOT NULL, 
		County varchar(64) NULL, 
		State varchar(64) NOT NULL, 
		PostalCode varchar(64) NOT NULL, 
		Country varchar(64) NULL, 
		Latitude decimal(9, 6) NOT NULL, 
		Longitude decimal(9, 6) NOT NULL, 
		Hours varchar(64) NULL, 
		RetailOutlet varchar(64) NULL, 
		LocationType varchar(64) NOT NULL);"""
		
	# combination of terminalId and institutionRtn creates the CoopLocationId field
	# example: 'terminalId-institutionRtn'
	api_fields_corresponding_to_column_order = ['terminalId', 
		'NULL', # Corresponds to bit value TakeCoopData and SoftDelete
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
		error = None
		try:
			locationId = str(uuid.uuid4()) # BECU LocationId
			statement = "INSERT INTO Locations VALUES ('{}' ".format(locationId)
			for api_field in Locations_Table.api_fields_corresponding_to_column_order:
				error = api_field
				if api_field == 'NULL':
						statement += ', 1, 0' # Sets TakeCoopData to TRUE and SoftDelete to FALSE
				elif location[api_field] == '': 
					statement += ", NULL"
				else: # if data present for column
					if api_field ==  'latitude' or api_field == 'longitude': # these are decimal values
						statement += ", {}".format(location[api_field])
						continue
					elif api_field == 'terminalId': # LocationId
						statement += ", '{}-{}'".format(location[api_field], location['institutionRtn'])
					elif api_field == 'state': # All locations are in Washington and we store the state code
						statement += ", 'WA'"
					else:
						statement += ", '{}'".format(location[api_field])
			statement += ");"
			return statement, locationId
		except Exception as e:
			print("error: {}\nApi Field: {}".format(e, error))
		

