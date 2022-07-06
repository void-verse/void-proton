from proton.handler import Response, Request
from .models import TestModel_A


def test_controller_1(req: Request):
    print(req.params, req.queries)
    model_data = TestModel_A.update(id=req.params["id"], data=req.data)
    return Response(status=200, data={"updated": model_data})


def test_controller_2(req: Request):
    print(req.params, req.queries)
    model_data = TestModel_A.find(id=req.params["id"])
    return Response(status=201, data={"found": model_data})


def test_controller_3(req: Request):
    print(req.data)
    model_data = TestModel_A.create(req.data)
    return Response(status=200, data={"created": model_data})


def test_controller_4(req: Request):
    print(req.params, req.queries)
    TestModel_A.delete(id=req.params["id"])
    return Response(status=201, data={"deleted": "!"})
