
import gevent.monkey
gevent.monkey.patch_all()

import logging
import sys
from ytb.main import main

logging.basicConfig(level=logging.DEBUG)
ret = main(*sys.argv[1:])
sys.exit(ret)
