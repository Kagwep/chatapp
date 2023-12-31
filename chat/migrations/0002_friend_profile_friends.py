# Generated by Django 4.2.1 on 2023-08-06 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Friend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="chat.profile"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="friends",
            field=models.ManyToManyField(
                related_name="profile_friend", to="chat.friend"
            ),
        ),
    ]
