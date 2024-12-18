# Generated by Django 5.1.4 on 2024-12-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_number', models.CharField(max_length=50, unique=True)),
                ('case_status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Pending', 'Pending'), ('Archived', 'Archived')], max_length=50)),
            ],
            options={
                'db_table': 'Cases',
            },
        ),
        migrations.CreateModel(
            name='ChainOfCustody',
            fields=[
                ('chain_id', models.AutoField(primary_key=True, serialize=False)),
                ('evidence_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('time_of_access', models.DateTimeField()),
                ('time_of_return', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ChainOfCustody',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('document_type', models.CharField(choices=[('Reports', 'Reports'), ('Search Warrants', 'Search Warrants'), ('Court Orders', 'Court Orders'), ('Chain of Custody Forms', 'Chain of Custody Forms')], max_length=50)),
            ],
            options={
                'db_table': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('evidence_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_id', models.IntegerField()),
                ('evidence_type', models.CharField(choices=[('Physical Evidence', 'Physical Evidence'), ('Digital Evidence', 'Digital Evidence')], max_length=50)),
                ('metadata', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Evidence',
            },
        ),
        migrations.CreateModel(
            name='LegalEntities',
            fields=[
                ('legal_entity_id', models.AutoField(primary_key=True, serialize=False)),
                ('entity_type', models.CharField(choices=[('Case Judge', 'Case Judge'), ('Legal Teams', 'Legal Teams'), ('Defense', 'Defense'), ('Prosecution', 'Prosecution'), ('Regulatory Body', 'Regulatory Body')], max_length=50)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'LegalEntities',
            },
        ),
        migrations.CreateModel(
            name='Suspects',
            fields=[
                ('suspect_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.BinaryField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address_id', models.IntegerField(blank=True, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('eye_color', models.CharField(blank=True, max_length=20, null=True)),
                ('hair_color', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'Suspects',
            },
        ),
    ]
