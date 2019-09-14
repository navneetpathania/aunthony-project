# -*- coding: utf-8 -*-
from django.db import migrations, models
import datetime
from django.utils.timezone import utc
class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stellar', '0002_auto_20160917_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user_name',
            field=models.CharField(default=datetime.datetime(2016, 9, 17, 20, 45, 3, 729491, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
