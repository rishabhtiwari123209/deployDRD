# Generated by Django 4.2.13 on 2024-07-05 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mediccal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthy', models.FloatField()),
                ('mild', models.FloatField()),
                ('moderate', models.FloatField()),
                ('poliferate', models.FloatField()),
                ('severe', models.FloatField()),
                ('image', models.ImageField(upload_to='medical')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Medical',
        ),
    ]
