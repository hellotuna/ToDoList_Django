# Generated by Django 3.1.4 on 2020-12-10 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0002_todo_isdone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='isDOne',
            new_name='isDone',
        ),
    ]