/**
 * Copyright 2017 Dunbar Security Solutions, Inc.
 * 
 * This file is part of Cyphon Engine.
 * 
 * Cyphon Engine is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * Cyphon Engine is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
 */

(function($) {
    $(document).ready(function() {

        // save selected bottle to target_field autocomplete widgets,
        // so datacondensers.autocomplete.FilterTargetFieldsByBottle can filter
        // target_field options appropriately
        saveMasterFieldValue('bottle', 'target_field');
        
        // select content_type according to selected target_field
        setDependentField(
            fieldset='.inline-related .grp-module',
            masterField='.target_field',
            masterValue='EmbeddedDocument',
            dependentField='.content_type',
            conditionalValue='condenser',
            defaultValue='parser'
        );

        // save list of selected target_fields to each target_field autocomplete
        // widget, so datacondensers.autocomplete.FilterTargetFieldsByBottle can
        // remove them from available options
        saveSelectedValues('target_field');

    });
} (django.jQuery));