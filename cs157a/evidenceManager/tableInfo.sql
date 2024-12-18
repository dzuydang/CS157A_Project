USE CS157A_ProjectDB;
INSERT INTO Employees (Username, PasswordHash, EmployeeType)
VALUES
	('admin1', 'hash_admin1', 'Admins'),
	('analyst1', 'hash_analyst1', 'Evidence Analyst'),
	('viewer1', 'hash_viewer1', 'View-only Users'),
	('investigator1', 'hash_investigator1', 'Investigators');

INSERT INTO Cases (CaseNumber, CaseStatus)
VALUES
	('2024-CR-001', 'Open'),
	('2024-CR-002', 'Pending'),
	('2024-CR-003', 'Closed');

INSERT INTO Evidence (CaseID, EvidenceType, Metadata)
VALUES
	(1, 'Physical Evidence', '{"description": "Fingerprint sample", "location": "Locker A"}'),
	(1, 'Digital Evidence', '{"description": "Phone screenshot", "location": "Digital Vault"}'),
	(2, 'Physical Evidence', '{"description": "Blood sample", "location": "Locker B"}');

INSERT INTO ChainOfCustody (EvidenceID, EmployeeID, TimeOfAccess, TimeOfReturn)
VALUES
	(1, 2, '2024-11-01 10:00:00', '2024-11-01 11:00:00'),
	(2, 3, '2024-11-02 14:00:00', NULL),
	(3, 4, '2024-11-03 09:30:00', '2024-11-03 10:15:00');

INSERT INTO Addresses (Street, City, State, Zipcode)
VALUES
	('123 Elm St', 'San Jose', 'CA', '95123'),
	('456 Oak Rd', 'Santa Clara', 'CA', '95050'),
	('789 Pine Ave', 'Sunnyvale', 'CA', '94085');

INSERT INTO Suspects (Name, Photo, Age, AddressID, Height, EyeColor, HairColor)
VALUES
	('John Doe', NULL, 35, 1, 5.9, 'Brown', 'Black'),
	('Jane Smith', NULL, 28, 2, 5.6, 'Blue', 'Blonde'),
	('Bob Johnson', NULL, 40, 3, 6.1, 'Green', 'Brown');

INSERT INTO Security (EmployeeID, EncryptedInformation, PasswordHash)
VALUES
	(1, 'Admin encryption data', 'hash_admin'),
	(2, 'Analyst encryption data', 'hash_analyst'),
	(3, 'Viewer encryption data', 'hash_viewer');

INSERT INTO AccessPermissions (SecurityID, Permission)
VALUES
	(1, 'ViewAll'),
	(1, 'EditAll'),
	(2, 'ViewEvidence'),
	(3, 'ViewOnly');

INSERT INTO Locations (LocationType, AddressID, Coordinates)
VALUES
	('Crime Scenes', 1, '37.3382,-121.8863'),
	('Evidence Storage', 2, '37.3541,-121.9552'),
	('Offices', 3, '37.3688,-122.0363');

INSERT INTO Documents (DocumentType)
VALUES
	('Reports'),
	('Search Warrants'),
	('Court Orders'),
	('Chain of Custody Forms');

INSERT INTO LegalEntities (EntityType, State, City)
VALUES
	('Case Judge', 'CA', 'San Jose'),
	('Prosecution', 'CA', 'Santa Clara'),
	('Defense', 'CA', 'Sunnyvale');
