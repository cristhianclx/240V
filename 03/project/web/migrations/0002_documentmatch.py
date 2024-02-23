# Generated by Django 4.2 on 2024-02-23 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('ranking', models.DecimalField(decimal_places=30, max_digits=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.document')),
            ],
        ),
    ]
