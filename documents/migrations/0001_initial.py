# Generated by Django 4.2.6 on 2023-10-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('status', models.CharField(choices=[('processed', 'Processed'), ('non_processed', 'Non Processed'), ('completed', 'Completed')], default='non_processed', max_length=20)),
                ('last_search_date', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
