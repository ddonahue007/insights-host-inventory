# Generated by Django 2.0.7 on 2018-10-04 21:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20180719_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=10)),
                ('display_name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('facts', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('tags', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('canonical_facts', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='entity',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddIndex(
            model_name='host',
            index=models.Index(fields=['account'], name='inventory_h_account_529aeb_idx'),
        ),
    ]
