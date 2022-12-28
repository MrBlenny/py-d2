# -*- coding: utf-8 -*-
import time

import pytest


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


@pytest.fixture(scope="session", autouse=True)
def timer_session_scope():
    start = time.time()
    print("\nstart: {}".format(time.strftime(DATE_FORMAT, time.localtime(start))))

    yield

    finished = time.time()
    print("\nfinished: {}".format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    print("Total time cost: {:.3f}s".format(finished - start))


@pytest.fixture(autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print("\nTime cost: {:.3f}s".format(time.time() - start))
