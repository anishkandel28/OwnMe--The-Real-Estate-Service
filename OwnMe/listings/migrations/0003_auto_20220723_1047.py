# Generated by Django 3.1.14 on 2022-07-23 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20220723_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_for',
            field=models.CharField(choices=[('S', 'Sell'), ('R', 'Rent')], default='S', max_length=5, verbose_name='Listing for'),
        ),
    ]
