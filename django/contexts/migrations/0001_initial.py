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


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distilleries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('before_time_interval', models.PositiveIntegerField(default=0, null=True)),
                ('before_time_unit', models.CharField(choices=[('s', 'Seconds'), ('m', 'Minutes'), ('h', 'Hours'), ('d', 'Days')], default='m', max_length=3, null=True)),
                ('after_time_interval', models.PositiveIntegerField(default=0, null=True)),
                ('after_time_unit', models.CharField(choices=[('s', 'Seconds'), ('m', 'Minutes'), ('h', 'Hours'), ('d', 'Days')], default='m', max_length=3, null=True)),
                ('filter_logic', models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], default='AND', max_length=40)),
                ('primary_distillery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contexts', related_query_name='context', to='distilleries.Distillery')),
                ('related_distillery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distilleries.Distillery')),
            ],
        ),
        migrations.CreateModel(
            name='ContextFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_field', models.CharField(help_text='The Container field whose value should be used to search the field of the Related Distillery.', max_length=255, verbose_name='value field in Distillery')),
                ('search_field', models.CharField(help_text="The field of the Related Distillery's Container that should be used to filter results.", max_length=255, verbose_name='search field in Related Distillery')),
                ('operator', models.CharField(choices=[('eq', 'equals'), ('in', 'contains'), ('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'), ('regex', 'contains'), ('not:eq', 'does not equal'), ('not:in', 'does not contain'), ('not:regex', 'does not contain'), ('not:missing', 'is not null'), ('within', 'within')], max_length=40)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', related_query_name='filter', to='contexts.Context')),
            ],
            options={
                'ordering': ['search_field', 'value_field'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='contextfilter',
            unique_together=set([('context', 'value_field', 'search_field')]),
        ),
        migrations.AlterUniqueTogether(
            name='context',
            unique_together=set([('name', 'primary_distillery')]),
        ),
    ]
