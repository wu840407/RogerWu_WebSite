# Generated by Django 5.1.6 on 2025-03-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created_at',
            new_name='published_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='published',
        ),
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
