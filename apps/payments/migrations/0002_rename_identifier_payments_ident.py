# Generated by Django 5.1.1 on 2024-10-29 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='identifier',
            new_name='ident',
        ),
    ]
