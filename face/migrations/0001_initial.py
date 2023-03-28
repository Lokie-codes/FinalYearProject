# Generated by Django 3.2.18 on 2023-03-26 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0007_alter_student_faceimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faceImg', models.ImageField(blank=True, null=True, upload_to='database/')),
                ('embedding', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student', verbose_name='studentId')),
            ],
        ),
    ]
