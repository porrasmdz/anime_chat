# Generated by Django 5.0.3 on 2024-03-25 04:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_chatmessage_receiver_alter_chatmessage_sender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="full_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to="user_images"
            ),
        ),
    ]
