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

    def get_create_table(self):
        return SpecialQualities_Table.CREATE_LOCATIONS_TABLE