# Generated by Django 2.0.6 on 2018-07-20 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180720_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpost',
            name='on_going_project',
            field=models.CharField(choices=[('INC', 'Incomplete'), ('CPLT', 'Complete'), ('DROP', 'Dropped')], default='INC', max_length=4),
        ),
    ]