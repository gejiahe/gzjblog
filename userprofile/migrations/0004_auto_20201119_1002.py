# Generated by Django 2.2 on 2020-11-19 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20201119_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userprofile.Org'),
        ),
    ]