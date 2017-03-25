#!/bin/sh

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

# wait for PSQL server to start
sleep 10

# cd /usr/src/app/cyphon/django

# migrate db, so we have the latest db schema
su -m cyphon -c "python manage.py migrate --verbosity 0"

# collect static files
su -m cyphon -c "python manage.py collectstatic --noinput --verbosity 0"

# create superuser
if [ "$CYPHON_SUPERUSER" = 'YES' ]; then
    echo "from django.contrib.auth import get_user_model; \
          USER_MODEL = get_user_model(); \
          args = ['$CYPHON_USERNAME', '$CYPHON_PASSWORD']; \
          USER_MODEL.objects.create_superuser(*args)" \
          | python manage.py shell
fi

echo "Running Development Server"
exec python manage.py runserver 0.0.0.0:8000 "$@"
