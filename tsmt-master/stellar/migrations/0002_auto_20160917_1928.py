from django.db import migrations, models
import datetime
from django.utils.timezone import utc
class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stellar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('memo', models.CharField(max_length=28)),
            ],
        ),
        migrations.AddField(
            model_name='accounts',
            name='user_name',
            field=models.CharField(default=datetime.datetime(2016, 9, 17, 19, 28, 52, 92749, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
