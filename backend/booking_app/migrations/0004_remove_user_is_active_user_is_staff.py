# Generated by Django 4.1 on 2023-10-15 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking_app", "0003_remove_user_is_staff_alter_user_is_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]