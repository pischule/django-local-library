# Generated by Django 3.0.8 on 2020-07-31 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
