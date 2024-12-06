from django.db import models


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True, db_column='EmployeeID')
    username = models.CharField(max_length=50, unique=True, db_column='Username')
    password_hash = models.CharField(max_length=255, db_column='PasswordHash')
    employee_type = models.CharField(max_length=20, db_column='EmployeeType', choices=[
        ('Admins', 'Admins'),
        ('Evidence Analyst', 'Evidence Analyst'),
        ('View-only Users', 'View-only Users'),
        ('Investigators', 'Investigators'),
        ('IT', 'IT'),
    ])

    class Meta:
        db_table = 'Employees'


class Cases(models.Model):
    case_id = models.AutoField(primary_key=True, db_column='CaseID')
    case_number = models.CharField(max_length=50, unique=True, db_column='CaseNumber')
    case_status = models.CharField(max_length=10, db_column='CaseStatus', choices=[
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Pending', 'Pending'),
        ('Archived', 'Archived'),
    ])

    class Meta:
        db_table = 'Cases'


class Evidence(models.Model):
    evidence_id = models.AutoField(primary_key=True, db_column='EvidenceID')
    case = models.ForeignKey(Cases, on_delete=models.CASCADE, db_column='CaseID')
    evidence_type = models.CharField(max_length=20, db_column='EvidenceType', choices=[
        ('Physical Evidence', 'Physical Evidence'),
        ('Digital Evidence', 'Digital Evidence'),
    ])
    metadata = models.JSONField(null=True, blank=True, db_column='Metadata')

    class Meta:
        db_table = 'Evidence'


class ChainOfCustody(models.Model):
    chain_id = models.AutoField(primary_key=True, db_column='ChainID')
    evidence = models.ForeignKey(Evidence, on_delete=models.CASCADE, db_column='EvidenceID')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, db_column='EmployeeID')
    time_of_access = models.DateTimeField(db_column='TimeOfAccess')
    time_of_return = models.DateTimeField(null=True, blank=True, db_column='TimeOfReturn')

    class Meta:
        db_table = 'ChainOfCustody'


class Addresses(models.Model):
    address_id = models.AutoField(primary_key=True, db_column='AddressID')
    street = models.CharField(max_length=255, null=True, blank=True, db_column='Street')
    city = models.CharField(max_length=50, null=True, blank=True, db_column='City')
    state = models.CharField(max_length=50, null=True, blank=True, db_column='State')
    zipcode = models.CharField(max_length=20, null=True, blank=True, db_column='Zipcode')

    class Meta:
        db_table = 'Addresses'


class Suspects(models.Model):
    suspect_id = models.AutoField(primary_key=True, db_column='SuspectID')
    name = models.CharField(max_length=100, db_column='Name')
    photo = models.BinaryField(null=True, blank=True, db_column='Photo')
    age = models.IntegerField(null=True, blank=True, db_column='Age')
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE, db_column='AddressID')
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Height')
    eye_color = models.CharField(max_length=20, null=True, blank=True, db_column='EyeColor')
    hair_color = models.CharField(max_length=20, null=True, blank=True, db_column='HairColor')

    class Meta:
        db_table = 'Suspects'


class Security(models.Model):
    security_id = models.AutoField(primary_key=True, db_column='SecurityID')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, db_column='EmployeeID')
    encrypted_information = models.TextField(db_column='EncryptedInformation')
    password_hash = models.CharField(max_length=255, db_column='PasswordHash')

    class Meta:
        db_table = 'Security'


class AccessPermissions(models.Model):
    security = models.ForeignKey(Security, on_delete=models.CASCADE, db_column='SecurityID')
    permission = models.CharField(max_length=50, db_column='Permission')

    class Meta:
        db_table = 'AccessPermissions'


class Logs(models.Model):
    log_id = models.AutoField(primary_key=True, db_column='LogID')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, db_column='EmployeeID')
    action = models.CharField(max_length=255, db_column='Action')
    timestamp = models.DateTimeField(db_column='Timestamp')

    class Meta:
        db_table = 'Logs'


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True, db_column='LocationID')
    location_type = models.CharField(max_length=20, db_column='LocationType', choices=[
        ('Crime Scenes', 'Crime Scenes'),
        ('Evidence Storage', 'Evidence Storage'),
        ('Offices', 'Offices'),
    ])
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE, db_column='AddressID')
    coordinates = models.CharField(max_length=255, null=True, blank=True, db_column='Coordinates')

    class Meta:
        db_table = 'Locations'


class Devices(models.Model):
    device_id = models.AutoField(primary_key=True, db_column='DeviceID')
    device_type = models.CharField(max_length=20, db_column='DeviceType', choices=[
        ('Computers', 'Computers'),
        ('Phones', 'Phones'),
        ('Storage Media', 'Storage Media'),
        ('Hard Drives', 'Hard Drives'),
        ('USB Devices', 'USB Devices'),
    ])
    source_device = models.CharField(max_length=255, null=True, blank=True, db_column='SourceDevice')

    class Meta:
        db_table = 'Devices'


class Documents(models.Model):
    document_id = models.AutoField(primary_key=True, db_column='DocumentID')
    document_type = models.CharField(max_length=50, db_column='DocumentType', choices=[
        ('Reports', 'Reports'),
        ('Search Warrants', 'Search Warrants'),
        ('Court Orders', 'Court Orders'),
        ('Chain of Custody Forms', 'Chain of Custody Forms'),
    ])

    class Meta:
        db_table = 'Documents'


class LegalEntities(models.Model):
    legal_entity_id = models.AutoField(primary_key=True, db_column='LegalEntityID')
    entity_type = models.CharField(max_length=50, db_column='EntityType', choices=[
        ('Case Judge', 'Case Judge'),
        ('Legal Teams', 'Legal Teams'),
        ('Defense', 'Defense'),
        ('Prosecution', 'Prosecution'),
        ('Regulatory Body', 'Regulatory Body'),
    ])
    state = models.CharField(max_length=50, null=True, blank=True, db_column='State')
    city = models.CharField(max_length=50, null=True, blank=True, db_column='City')

    class Meta:
        db_table = 'LegalEntities'
