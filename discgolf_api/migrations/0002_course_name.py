# Generated by Django 2.1.3 on 2018-12-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discgolf_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='test', max_length=250),
            preserve_default=False,
        ),
    ]
