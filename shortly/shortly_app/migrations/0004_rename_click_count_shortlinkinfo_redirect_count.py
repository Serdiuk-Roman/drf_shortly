# Generated by Django 3.2.7 on 2021-09-12 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortly_app', '0003_rename_last_datetime_shortlinkinfo_last_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortlinkinfo',
            old_name='click_count',
            new_name='redirect_count',
        ),
    ]