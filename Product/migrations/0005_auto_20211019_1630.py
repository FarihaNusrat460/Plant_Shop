# Generated by Django 3.1.1 on 2021-10-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20211010_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(blank=True, to='Product.Product'),
        ),
    ]
