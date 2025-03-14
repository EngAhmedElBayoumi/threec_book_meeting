# Generated by Django 5.1.7 on 2025-03-10 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_accreditationsection_accreditationlogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculumSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_subtitle', models.CharField(max_length=200, verbose_name='Section Subtitle')),
                ('section_subtitle_en', models.CharField(max_length=200, null=True, verbose_name='Section Subtitle')),
                ('section_subtitle_ar', models.CharField(max_length=200, null=True, verbose_name='Section Subtitle')),
                ('main_title_part1', models.CharField(max_length=100, verbose_name='Main Title Part 1')),
                ('main_title_part1_en', models.CharField(max_length=100, null=True, verbose_name='Main Title Part 1')),
                ('main_title_part1_ar', models.CharField(max_length=100, null=True, verbose_name='Main Title Part 1')),
                ('highlighted_word', models.CharField(max_length=50, verbose_name='Highlighted Word')),
                ('highlighted_word_en', models.CharField(max_length=50, null=True, verbose_name='Highlighted Word')),
                ('highlighted_word_ar', models.CharField(max_length=50, null=True, verbose_name='Highlighted Word')),
                ('main_title_part2', models.CharField(max_length=200, verbose_name='Main Title Part 2')),
                ('main_title_part2_en', models.CharField(max_length=200, null=True, verbose_name='Main Title Part 2')),
                ('main_title_part2_ar', models.CharField(max_length=200, null=True, verbose_name='Main Title Part 2')),
            ],
            options={
                'verbose_name': 'Curriculum Section',
                'verbose_name_plural': 'Curriculum Sections',
            },
        ),
        migrations.AlterField(
            model_name='accreditationlogo',
            name='logo_image',
            field=models.FileField(upload_to='accreditations/', verbose_name='Logo Image'),
        ),
        migrations.AlterField(
            model_name='accreditationlogo',
            name='logo_url',
            field=models.URLField(blank=True, null=True, verbose_name='Logo URL'),
        ),
        migrations.AlterField(
            model_name='homestatisticitem',
            name='stat_icon',
            field=models.FileField(upload_to='stats/', verbose_name='Statistic Icon'),
        ),
    ]
