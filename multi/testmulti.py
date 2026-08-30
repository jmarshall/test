#import pysam

import http.server
#import multiprocessing
#import sys
from datetime import datetime

#import pytest


def test_foo():
    print(f"\nS0 {datetime.now()}")
    server = http.server.HTTPServer(("127.0.0.1", 0), http.server.SimpleHTTPRequestHandler)
    print(f"S1 {datetime.now()}")
    #server.serve_forever()
