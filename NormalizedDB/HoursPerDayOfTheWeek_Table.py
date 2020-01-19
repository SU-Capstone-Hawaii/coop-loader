class HoursPerDayOfTheWeek_Table:
	CREATE_HOURS_TABLE = """CREATE TABLE HoursPerDayOfTheWeek(
		LocationID varchar(64) NOT NULL PRIMARY KEY,
		HoursMonOpen varchar(10) NULL,
		HoursMonClose varchar(10) NULL,
		HoursTueOpen varchar(10) NULL,
		HoursTueClose varchar(10) NULL,
		HoursWedOpen varchar(10) NULL,
		HoursWedClose varchar(10) NULL,
		HoursThuOpen varchar(10) NULL,
		HoursThuClose varchar(10) NULL,
		HoursFriOpen varchar(10) NULL,
		HoursFriClose varchar(10) NULL,
		HoursSatOpen varchar(10) NULL,
		HoursSatClose varchar(10) NULL,
		HoursSunOpen varchar(10) NULL,
		HoursSunClose varchar(10) NULL,
		HoursDTMonOpen varchar(10) NULL,
		HoursDTMonClose varchar(10) NULL,
		HoursDTTueOpen varchar(10) NULL,
		HoursDTTueClose varchar(10) NULL,
		HoursDTWedOpen varchar(10) NULL,
		HoursDTWedClose varchar(10) NULL,
		HoursDTThuOpen varchar(10) NULL,
		HoursDTThuClose varchar(10) NULL,
		HoursDTFriOpen varchar(10) NULL,
		HoursDTFriClose varchar(10) NULL,
		HoursDTSatOpen varchar(10) NULL,
		HoursDTSatClose varchar(10) NULL,
		HoursDTSunOpen varchar(10) NULL,
		HoursDTSunClose varchar(10) NULL,
		FOREIGN KEY (LocationID) REFERENCES [Locations] (LocationID) ON UPDATE NO ACTION ON DELETE CASCADE);"""
	
	api_fields_corresponding_to_column_order = ['mondayOpen',
		'mondayClose',
		'tuesdayOpen',
		'tuesdayClose',
		'wednesdayOpen',
		'wednesdayClose',
		'thursdayOpen',
		'thursdayClose',
		'fridayOpen',
		'fridayClose',
		'saturdayOpen',
		'saturdayClose',
		'sundayOpen',
		'sundayClose',
		'mondayDriveThruOpen',
		'mondayDriveThruClose',
		'tuesdayDriveThruOpen',
		'tuesdayDriveThruClose',
		'wednesdayDriveThruOpen',
		'wednesdayDriveThruClose',
		'thursdayDriveThruOpen',
		'thursdayDriveThruClose',
		'fridayDriveThruOpen',
		'fridayDriveThruClose',
		'saturdayDriveThruOpen',
		'saturdayDriveThruClose',
		'sundayDriveThruOpen',
		'sundayDriveThruClose']

	def get_create_table(self):
		return HoursPerDayOfTheWeek_Table.CREATE_HOURS_TABLE

	def get_insert_row(self, location, locationId):
		all_null = True # if true after looping, return an empty string
		statement = "INSERT INTO HoursPerDayOfTheWeek VALUES ({}, ".format(locationId)
		for api_field in HoursPerDayOfTheWeek_Table.api_fields_corresponding_to_column_order:
			if api_field == 'NULL' or location[api_field] == '': statement += ', NULL'
			else:
				statement += ", {}".format(location[api_field])
				if all_null: all_null = False
		statement += ");"

		if all_null:
			return ''
		return statement