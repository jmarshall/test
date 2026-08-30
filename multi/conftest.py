import multiprocessing
from datetime import datetime

import pytest

def foo(wconn):
    wconn.send(37)

@pytest.fixture
def mkprocess():
    print(f"S0 {datetime.now()}")
    rconn, wconn = multiprocessing.Pipe(duplex=False)
    print(f"S1 {datetime.now()}")
    process = multiprocessing.Process(target=foo, args=[wconn], daemon=True)
    print(f"S2 {datetime.now()}")
    process.start()
    print(f"S3 {datetime.now()}")
    bar = rconn.recv()
    print(f"S4 {datetime.now()}")

    yield bar

    print(f"S5 {datetime.now()}")
    process.terminate()
    print(f"S6 {datetime.now()}")
    process.join()
    print(f"S7 {datetime.now()}")

