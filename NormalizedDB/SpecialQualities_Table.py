class SpecialQualities_Table:
	CREATE_LOCATIONS_TABLE = """CREATE TABLE SpecialQualities(
		LocationID varchar(64) NOT NULL PRIMARY KEY,
		RestrictedAccess varchar(64) NULL,
		AcceptDeposit varchar(64) NULL,
		AcceptCash varchar(64) NULL,
		EnvelopeRequired varchar(64) NULL,
		OnMilitaryBase varchar(64) NULL,
		OnPremise varchar(64) NULL,
		Surcharge varchar(64) NULL,
		Access varchar(64) NULL,
		AccessNotes varchar(64) NULL,
		InstallationType varchar(64) NULL,
		HandicapAccess varchar(64) NULL,
		Cashless varchar(64) NULL,
		DriveThruOnly varchar(64) NULL,
		LimitedTransactions varchar(64) NULL,
		MilitaryIdRequired varchar(64) NULL,
		SelfServiceDevice varchar(64) NULL,
		SelfServiceOnly varchar(64) NULL,
		FOREIGN KEY (LocationID) REFERENCES [Locations] (LocationID) ON UPDATE NO ACTION ON DELETE CASCADE);"""
	
	api_fields_corresponding_to_column_order = ['restrictedAccess',
		'acceptDeposit',
		'acceptCash',
		'envelopeRequired',
		'onMilitaryBase',
		'onPremise',
		'surcharge',
		'access',
		'accessNote',
		'installationType',
		'handicapAccess',
		'cashless',
		'driveThruOnly',
		'limitedTransactions',
		'militaryIdRequired',
		'selfServiceDevice',
		'selfServiceOnly']

	def __init(self):
		self.lowkey = 'lowkey'

	def get_create_table(self):
		return SpecialQualities_Table.CREATE_LOCATIONS_TABLE
	
	def get_insert_row(self, location, locationId):
		statement = "INSERT INTO SpecialQualities VALUES ('{}'".format(locationId)
		for api_field in SpecialQualities_Table.api_fields_corresponding_to_column_order:
			if api_field == 'NULL' or location[api_field] == '': 
				statement += ", NULL"
			else:
				statement += ", '{}'".format(location[api_field])
		statement += ");"
		return statement