# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import os

if os.environ.get('DEBUG') == 'True':
    print('Debug mode is on')
else:
    print('Debug mode is off')
