# Generated by Django 3.1.14 on 2022-07-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20220724_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addlisting',
            old_name='images',
            new_name='listing_image_first',
        ),
        migrations.AddField(
            model_name='addlisting',
            name='bathroom',
            field=models.IntegerField(default=0, verbose_name='Bathroom'),
        ),
        migrations.AddField(
            model_name='addlisting',
            name='bedroom',
            field=models.IntegerField(default=0, verbose_name='Bedroom'),
        ),
        migrations.AddField(
            model_name='addlisting',
            name='condition',
            field=models.CharField(choices=[('1', 'Used'), ('2', 'New')], max_length=1, null=True, verbose_name='Condition'),
        ),
        migrations.AddField(
            model_name='addlisting',
            name='kitchen',
            field=models.IntegerField(default=0, verbose_name='Kitchen'),
        ),
        migrations.AddField(
            model_name='addlisting',
            name='listing_image_second',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='addlisting',
            name='listing_image_third',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='addlisting',
            name='owner_docs',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
