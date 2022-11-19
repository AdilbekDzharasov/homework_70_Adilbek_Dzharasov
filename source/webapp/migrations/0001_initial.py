# Generated by Django 4.1.1 on 2022-10-11 11:25

from django.db import migrations, models
import django.db.models.deletion
import webapp.models.tasks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_title', models.CharField(max_length=100, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_title', models.CharField(max_length=100, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=300, validators=[webapp.models.tasks.at_summary_capitalize], verbose_name='Summary')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.status', verbose_name='Status')),
                ('type', models.ManyToManyField(related_name='type', to='webapp.type')),
            ],
        ),
    ]