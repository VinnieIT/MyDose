# Generated by Django 2.1.7 on 2019-04-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDose', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug_period',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medication_drugs',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='medication_drugs',
            name='frequency',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='medication_drugs',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]