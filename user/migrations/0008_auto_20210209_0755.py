# Generated by Django 3.1.5 on 2021-02-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210209_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='76105b3f', max_length=100),
        ),
    ]
