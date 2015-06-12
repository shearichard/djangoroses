#!/usr/bin/env python
import os
import sys
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roses.settings")

    from django.core.management import execute_from_command_line

    logger.info('STARTING SERVER')

    execute_from_command_line(sys.argv)
