# Generated by Django 3.2.4 on 2021-07-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_generation', '0002_testresults_testdone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresults',
            name='testDone',
            field=models.DateTimeField(),
        ),
    ]
