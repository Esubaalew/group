# Generated by Django 4.2.7 on 2023-11-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FocusField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='FocusField')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('about', models.TextField(help_text='A brief summary about this person')),
                ('focus_fields', models.ManyToManyField(help_text='Fields a member is focusing on', to='group.focusfield', verbose_name='Focus Fields')),
            ],
        ),
    ]
