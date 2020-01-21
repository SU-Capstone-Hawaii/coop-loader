class Contacts_Table:
	CREATE_CONTACTS_TABLE = """CREATE TABLE Contacts(
		LocationID varchar(64) NOT NULL PRIMARY KEY,
		Phone varchar(64) NULL,
		Fax varchar(64) NULL,
		WebAddress varchar(64) NULL,
		FOREIGN KEY (LocationID) REFERENCES [Locations] (LocationID) ON UPDATE NO ACTION ON DELETE CASCADE);"""

	api_fields_corresponding_to_column_order = ['phone','fax','webAddress']

	def get_create_table(self):
		return Contacts_Table.CREATE_CONTACTS_TABLE

	'''
	Creates insert statement for contacts table.
	Arg:locationId is the BECU locationId  GUID
	'''
	def get_insert_row(self, location, locationId):
		statement = "INSERT INTO Contacts VALUES ('{}'".format(locationId)
		for api_field in Contacts_Table.api_fields_corresponding_to_column_order:
			if api_field == 'NULL' or location[api_field] == '': 
				statement += ", NULL"
			else:
				statement += ", '{}'".format(location[api_field])
		statement += ");"
		return statement