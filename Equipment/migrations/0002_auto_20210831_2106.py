# Generated by Django 3.1.7 on 2021-08-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/equipments/'),
        ),
    ]
