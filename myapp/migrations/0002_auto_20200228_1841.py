# Generated by Django 3.0.3 on 2020-02-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='some_integer_choice_field',
            field=models.IntegerField(choices=[(0, 'One'), (1, 'Two')]),
        ),
    ]
