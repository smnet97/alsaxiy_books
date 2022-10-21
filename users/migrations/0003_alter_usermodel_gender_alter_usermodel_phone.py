# Generated by Django 4.1.2 on 2022-10-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_usermodel_birth_day_alter_usermodel_id_card_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="gender",
            field=models.SmallIntegerField(
                blank=True, choices=[(0, "Male"), (1, "Female")], null=True
            ),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="phone",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
