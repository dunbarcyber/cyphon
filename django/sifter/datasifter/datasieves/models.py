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
"""

"""

# third party
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

# local
from cyphon.models import GetByNameManager
from sifter.sieves.models import FieldRule, Sieve, SieveManager, SieveNode


class DataRule(FieldRule):
    """

    """
    objects = GetByNameManager()


class DataSieve(Sieve):
    """
    A RuleSet subclass for examining bottled data.
    """
    objects = SieveManager()


class DataSieveNode(SieveNode):
    """
    A RuleSetNode subclass for examining data dictionaries.
    """
    RULE = models.Q(app_label='datasieves', model='datarule')
    RULESET = models.Q(app_label='datasieves', model='datasieve')
    CONTENT_TYPES = RULE | RULESET

    sieve = models.ForeignKey(
        DataSieve,
        related_name='nodes',
        related_query_name='node',
        help_text=_('A rule or rule set to assign to the node.')
    )
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to=CONTENT_TYPES,
                                     verbose_name=_('node type'))

