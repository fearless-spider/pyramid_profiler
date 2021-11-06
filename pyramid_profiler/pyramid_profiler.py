# -*- coding: utf8 -*-

import functools
import re
import time

from pprint import pprint as pp

import logging

from . import storage

logger = logging.getLogger("pyramid-profiler")
