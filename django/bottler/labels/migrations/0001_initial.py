# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.10.1 on 2017-03-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import utils.validators.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LabelField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=40, unique=True, validators=[utils.validators.validators.field_name_validator])),
                ('field_type', models.CharField(choices=[('BooleanField', 'BooleanField'), ('CharField', 'CharField'), ('ChoiceField', 'ChoiceField'), ('DateTimeField', 'DateTimeField'), ('EmailField', 'EmailField'), ('FileField', 'FileField'), ('FloatField', 'FloatField'), ('IntegerField', 'IntegerField'), ('GenericIPAddressField', 'IPAddressField'), ('ListField', 'ListField'), ('PointField', 'PointField'), ('TextField', 'TextField'), ('URLField', 'URLField'), ('EmbeddedDocument', 'EmbeddedDocument')], max_length=40)),
                ('target_type', models.CharField(blank=True, choices=[('Account', 'Account'), ('DateTime', 'DateTime'), ('IPAddress', 'IPAddress'), ('Keyword', 'Keyword'), ('Location', 'Location')], max_length=40, null=True)),
                ('object_id', models.PositiveIntegerField(help_text='The id of the inspection or procedure that will analyze the data.', verbose_name='analyzer id')),
                ('content_type', models.ForeignKey(help_text='Inspections determine whether data match a set of rules, defined by regular expressions. <br>Procedures perform more complex analyses, such as sentiment analysis or geolocation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='analyzer type')),
            ],
        ),
        migrations.AddField(
            model_name='label',
            name='fields',
            field=models.ManyToManyField(to='labels.LabelField'),
        ),
        migrations.AlterUniqueTogether(
            name='labelfield',
            unique_together=set([('field_name', 'content_type', 'object_id')]),
        ),
    ]
