# Generated by Django 2.2.8 on 2021-02-19 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0002_auto_20210219_2215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
    ]
