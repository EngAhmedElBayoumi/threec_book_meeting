# Generated by Django 5.1.7 on 2025-03-09 01:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_remove_coursecategory_name_en_remove_faq_answer_en_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="social",
            name="image",
        ),
        migrations.AddField(
            model_name="social",
            name="icon_class",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
