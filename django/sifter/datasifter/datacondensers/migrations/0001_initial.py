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
        ('bottles', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCondenser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='It\'s a good idea to name condensers after the type of data they are condensing, e.g., "email," "tweet," etc.', max_length=40, unique=True)),
                ('bottle', models.ForeignKey(help_text='The bottle (custom data  model) into which the raw data will be distilled and stored.', on_delete=django.db.models.deletion.CASCADE, to='bottles.Bottle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataFitting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(help_text='The id of the object that will parse the data.', verbose_name='parser id')),
                ('condenser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fittings', related_query_name='fitting', to='datacondensers.DataCondenser')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='parser type')),
                ('target_field', models.ForeignKey(help_text="The name of the field in the condenser's bottle, where the parsed data will be stored.", on_delete=django.db.models.deletion.CASCADE, to='bottles.BottleField')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataParser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='It\'s a good idea to name parsers after the source field(s) they are parsing and the method they use, e.g., "screen_name__COPY."', max_length=255, unique=True)),
                ('method', models.CharField(choices=[('COPY', 'Copy'), ('COUNT', 'Number of Occurrences'), ('DATE', 'Date from string'), ('P/A', 'Presence/Absence'), ('SUBSTRING', 'Substring')], default='COPY', help_text='The method used to extract data. "Copy" will return the entire contents of the source field(s). "Number of Occurrences" will return the number of times a match for the regex is found in the source field(s). "Presence/Absence" will return a Boolean indicating whether a regex match is found. "Substring" will return the first substring group defined in the Parser\'s regex.', max_length=40)),
                ('regex', models.CharField(blank=True, default=None, help_text='A regular expression used to match substrings in the text of the source field(s). Not required if the method is "Copy."', max_length=255, null=True, validators=[utils.validators.validators.regex_validator])),
                ('formatter', models.CharField(blank=True, default=None, help_text='A Python format string that will be used to format the parsed value. For example, "https://twitter.com/{}/" may be used to construct a link to a Twitter profile. ', max_length=255, null=True)),
                ('source_fields', models.CharField(help_text='One or more fields in a raw data document from which data will be extracted. Multiple field names should be separated by commas. Nested fields should be denoted using dot notation. For example, "user.first_name,user.last_name" will parse the fields {user: {first_name: "Jane", last_name: "Smith"}}.', max_length=255, verbose_name='source field(s)')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
