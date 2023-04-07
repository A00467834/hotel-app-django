from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='available',
            field=models.BooleanField(null=True),
        ),
    ]
