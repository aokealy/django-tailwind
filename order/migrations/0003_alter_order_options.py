# Generated by Django 4.0 on 2023-04-24 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_qauntity_orderitem_quantity_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
    ]