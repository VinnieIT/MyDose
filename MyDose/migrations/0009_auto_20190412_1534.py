# Generated by Django 2.1.7 on 2019-04-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDose', '0008_auto_20190412_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication_drugs',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]