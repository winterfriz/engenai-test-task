# Generated by Django 4.2.6 on 2023-10-19 07:25

from django.db import migrations, models
import pgvector.django


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_document_embedding'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=1000)),
                ('embedding', pgvector.django.VectorField(dimensions=1536, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
