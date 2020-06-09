# Generated by Django 3.0.5 on 2020-05-20 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_system', '0002_visitor_parking_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='parking_slot',
            field=models.CharField(blank=True, choices=[('1', 'Parking Slot 1'), ('2', 'Parking Slot 2'), ('3', 'Parking Slot 3'), ('4', 'Parking Slot 4'), ('5', 'Parking Slot 5'), ('6', 'Parking Slot 6'), ('7', 'Parking Slot 7'), ('8', 'Parking Slot 8'), ('9', 'Parking Slot 9'), ('10', 'Parking Slot 10')], default='1', max_length=255),
        ),
    ]
