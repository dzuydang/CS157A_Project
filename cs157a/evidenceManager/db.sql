-- Employees
CREATE TABLE Employees (
	EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
	Username VARCHAR(50) NOT NULL UNIQUE,
	PasswordHash VARCHAR(255) NOT NULL,
	EmployeeType ENUM('Admins', 'Evidence Analyst', 'View-only Users', 'Investigators', 'IT') NOT NULL
);

-- Cases
CREATE TABLE Cases (
	CaseID INT AUTO_INCREMENT PRIMARY KEY,
	CaseNumber VARCHAR(50) NOT NULL UNIQUE,
	CaseStatus ENUM('Open', 'Closed', 'Pending', 'Archived') NOT NULL
);

-- Evidence
CREATE TABLE Evidence (
	EvidenceID INT AUTO_INCREMENT PRIMARY KEY,
	CaseID INT NOT NULL,
	EvidenceType ENUM('Physical Evidence', 'Digital Evidence') NOT NULL,
	Metadata JSON,
	FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE
);

-- Chain of Custody
CREATE TABLE ChainOfCustody (
	ChainID INT AUTO_INCREMENT PRIMARY KEY,
	EvidenceID INT NOT NULL,
	EmployeeID INT NOT NULL,
	TimeOfAccess DATETIME NOT NULL,
	TimeOfReturn DATETIME,
	FOREIGN KEY (EvidenceID) REFERENCES Evidence(EvidenceID) ON DELETE CASCADE,
	FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Addresses
CREATE TABLE Addresses (
	AddressID INT AUTO_INCREMENT PRIMARY KEY,
	Street VARCHAR(255),
	City VARCHAR(50),
	State VARCHAR(50),
	Zipcode VARCHAR(20)
);

-- Suspects
CREATE TABLE Suspects (
	SuspectID INT AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL,
	Photo BLOB,
	Age INT,
	AddressID INT NOT NULL,
	Height DECIMAL(5, 2),
	EyeColor VARCHAR(20),
	HairColor VARCHAR(20),
	FOREIGN KEY (AddressID) REFERENCES Addresses(AddressID) ON DELETE CASCADE
);

-- Security
CREATE TABLE Security (
	SecurityID INT AUTO_INCREMENT PRIMARY KEY,
	EmployeeID INT NOT NULL,
	EncryptedInformation TEXT,
	PasswordHash VARCHAR(255) NOT NULL,
	FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Access Permissions
CREATE TABLE AccessPermissions (
	SecurityID INT NOT NULL,
	Permission VARCHAR(50),
	FOREIGN KEY (SecurityID) REFERENCES Security(SecurityID) ON DELETE CASCADE
);

-- Logs
CREATE TABLE Logs (
	LogID INT AUTO_INCREMENT PRIMARY KEY,
	EmployeeID INT NOT NULL,
	Action VARCHAR(255) NOT NULL,
	Timestamp DATETIME NOT NULL,
	FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Locations
CREATE TABLE Locations (
	LocationID INT AUTO_INCREMENT PRIMARY KEY,
	LocationType ENUM('Crime Scenes', 'Evidence Storage', 'Offices') NOT NULL,
	AddressID INT NOT NULL,
	Coordinates VARCHAR(255),
	FOREIGN KEY (AddressID) REFERENCES Addresses(AddressID) ON DELETE CASCADE
);

-- Devices
CREATE TABLE Devices (
	DeviceID INT AUTO_INCREMENT PRIMARY KEY,
	DeviceType ENUM('Computers', 'Phones', 'Storage Media', 'Hard Drives', 'USB Devices') NOT NULL,
	SourceDevice VARCHAR(255)
);

-- Documents
CREATE TABLE Documents (
	DocumentID INT AUTO_INCREMENT PRIMARY KEY,
	DocumentType ENUM('Reports', 'Search Warrants', 'Court Orders', 'Chain of Custody Forms') NOT NULL
);

-- Legal Entities
CREATE TABLE LegalEntities (
	LegalEntityID INT AUTO_INCREMENT PRIMARY KEY,
	EntityType ENUM('Case Judge', 'Legal Teams', 'Defense', 'Prosecution', 'Regulatory Body') NOT NULL,
	State VARCHAR(50),
	City VARCHAR(50)
);



