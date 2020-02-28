# Generated by Django 3.0.3 on 2020-02-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_integer_choice_field', models.IntegerField(choices=[(1, 'One'), (2, 'Two')])),
                ('a1', models.CharField(max_length=255)),
                ('a2', models.CharField(max_length=255)),
                ('a3', models.CharField(max_length=255)),
                ('a4', models.CharField(max_length=255)),
                ('some_boolean_field', models.BooleanField()),
                ('b1', models.CharField(max_length=255)),
                ('b2', models.CharField(max_length=255)),
                ('b3', models.CharField(max_length=255)),
            ],
        ),
    ]
