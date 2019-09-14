from django.db import migrations, models
import datetime
from django.utils.timezone import utc
class Migration(migrations.Migration):

    initial = True


    dependencies = [
        ('stellar', '0003_contact_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='memo',
            field=models.CharField(blank=True, max_length=28),
        ),
    ]
