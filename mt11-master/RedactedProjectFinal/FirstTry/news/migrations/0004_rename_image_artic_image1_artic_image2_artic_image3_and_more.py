# Generated by Django 4.2.1 on 2023-07-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_artic_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artic",
            old_name="image",
            new_name="image1",
        ),
        migrations.AddField(
            model_name="artic",
            name="image2",
            field=models.ImageField(
                blank=True,
                help_text="150x150px",
                upload_to="media/",
                verbose_name="Ссылка картинки",
            ),
        ),
        migrations.AddField(
            model_name="artic",
            name="image3",
            field=models.ImageField(
                blank=True,
                help_text="150x150px",
                upload_to="media/",
                verbose_name="Ссылка картинки",
            ),
        ),
        migrations.AddField(
            model_name="artic",
            name="image4",
            field=models.ImageField(
                blank=True,
                help_text="150x150px",
                upload_to="media/",
                verbose_name="Ссылка картинки",
            ),
        ),
    ]
