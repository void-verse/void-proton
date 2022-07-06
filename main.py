# main.py for test

from proton import Proton, run
from test.routes import test_router
from test.models import TestModel_A, TestModel_B, TestModel_C

test_api = Proton()
test_api.port = 6060
test_api.debug = True

test_api.set_router("/proton", test_router)
test_api.set_models(TestModel_A, TestModel_B, TestModel_C)

run(test_api)

# python3 main.py run:test_api
