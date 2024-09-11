# Generated by Django 5.1.1 on 2024-09-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('course_number', models.IntegerField(blank=True, default=0)),
                ('instructor_name', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.FloatField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'University Classes',
            },
        ),
    ]
