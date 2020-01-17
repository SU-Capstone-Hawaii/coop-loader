class Contacts_Table:
    CREATE_LOCATIONS_TABLE = """CREATE TABLE Contacts(
	LocationID varchar(64) NOT NULL PRIMARY KEY,
	Phone varchar(64) NULL,
	Fax varchar(64) NULL,
	WebAddress varchar(64) NULL,
	FOREIGN KEY (LocationID) REFERENCES [Locations] (LocationID) ON UPDATE NO ACTION ON DELETE CASCADE);"""

    def get_create_table(self):
        return Contacts_Table.CREATE_LOCATIONS_TABLE