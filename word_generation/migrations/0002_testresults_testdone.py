# Generated by Django 3.2.4 on 2021-07-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_generation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresults',
            name='testDone',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
