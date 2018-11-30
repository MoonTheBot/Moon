__title__ = 'mapi'
__author__ = 'Lizcrave'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Lizcrave'
__version__ = '1.0.0'

from collections import namedtuple
from .client import Client, CooldownActive, LoginError, ClientError
from .exceptions import *
from .enum import *

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=1, minor=3, micro=5, releaselevel='stable', serial=0)
