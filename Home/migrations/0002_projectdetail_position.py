# Generated by Django 2.1.3 on 2019-08-15 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
