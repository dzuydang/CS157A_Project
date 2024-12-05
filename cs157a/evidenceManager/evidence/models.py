from django.db import models

# Addresses
class Addresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'Addresses'


# Suspects
class Suspects(models.Model):
    suspect_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    photo = models.BinaryField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)
    hair_color = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'Suspects'


# Cases
class Cases(models.Model):
    case_id = models.AutoField(primary_key=True)
    case_number = models.CharField(max_length=50, unique=True)
    case_status = models.CharField(max_length=50, choices=[
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Pending', 'Pending'),
        ('Archived', 'Archived'),
    ])

    class Meta:
        db_table = 'Cases'


# Evidence
class Evidence(models.Model):
    evidence_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(Cases, on_delete=models.CASCADE)
    evidence_type = models.CharField(max_length=50, choices=[
        ('Physical Evidence', 'Physical Evidence'),
        ('Digital Evidence', 'Digital Evidence'),
    ])
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'Evidence'


# Chain of Custody
class ChainOfCustody(models.Model):
    chain_id = models.AutoField(primary_key=True)
    evidence = models.ForeignKey(Evidence, on_delete=models.CASCADE)
    employee_id = models.IntegerField()  # Update with ForeignKey if you have an Employees model
    time_of_access = models.DateTimeField()
    time_of_return = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'ChainOfCustody'


# Documents
class Documents(models.Model):
    document_id = models.AutoField(primary_key=True)
    document_type = models.CharField(max_length=50, choices=[
        ('Reports', 'Reports'),
        ('Search Warrants', 'Search Warrants'),
        ('Court Orders', 'Court Orders'),
        ('Chain of Custody Forms', 'Chain of Custody Forms'),
    ])

    class Meta:
        db_table = 'Documents'


# Legal Entities
class LegalEntities(models.Model):
    legal_entity_id = models.AutoField(primary_key=True)
    entity_type = models.CharField(max_length=50, choices=[
        ('Case Judge', 'Case Judge'),
        ('Legal Teams', 'Legal Teams'),
        ('Defense', 'Defense'),
        ('Prosecution', 'Prosecution'),
        ('Regulatory Body', 'Regulatory Body'),
    ])
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'LegalEntities'
