# Generated by Django 3.0.8 on 2020-07-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(help_text='Enter a language of the book', max_length=100, null=True),
        ),
    ]
