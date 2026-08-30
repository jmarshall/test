import http.server
import multiprocessing
import sys
from datetime import datetime

import pytest

def _httpd(wconn, directory):
    class QuietHTTPServer(http.server.HTTPServer):
        def handle_error(self, request, client_address):
            if isinstance(sys.exc_info()[1], (BrokenPipeError, ConnectionResetError)):
                pass
            else:
                super().handle_error(request, client_address)

    class QuietRequestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

        def log_message(self, format, *args):
            pass

    server = QuietHTTPServer(("localhost", 0), QuietRequestHandler)
    wconn.send(server.server_address)
    server.serve_forever()

@pytest.fixture
def mkprocess():
    print(f"\nS0 {datetime.now()}")
    rconn, wconn = multiprocessing.Pipe(duplex=False)
    print(f"S1 {datetime.now()}")
    process = multiprocessing.Process(target=_httpd, args=[wconn, "/tmp"], daemon=True)
    print(f"S2 {datetime.now()}")
    process.start()
    print(f"S3 {datetime.now()}")
    bar = rconn.recv()
    print(f"S4 {datetime.now()}")

    yield bar

    print(f"\nS5 {datetime.now()}")
    process.terminate()
    print(f"S6 {datetime.now()}")
    process.join()
    print(f"S7 {datetime.now()}")

