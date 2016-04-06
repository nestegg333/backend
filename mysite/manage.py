#!/usr/bin/env python
import os
import sys
import sqlite3

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line
    from django.db import connection

    execute_from_command_line(sys.argv)
