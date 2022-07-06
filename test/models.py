from proton.db import model


class TestModel_A(model.Model):
    test_field_1 = model.StringType(
        "test_field_1", max_length=50, min_length=4, unique=True, required=True
    )
    test_field_2 = model.IntegerType("test_field_2", max=1000, min=10)
    test_field_3 = model.BooleanType("test_field_3", default=False)


class TestModel_B(model.Model):
    test_field_1 = model.StringType(
        "test_field_1", max_length=50, min_length=4, unique=True, required=True
    )
    test_field_2 = model.IntegerType("test_field_2", max=1000, min=10)
    test_field_3 = model.BooleanType("test_field_3", default=False)


class TestModel_C(model.Model):
    test_field_1 = model.StringType(
        "test_field_1", max_length=50, min_length=4, unique=True, required=True
    )
    test_field_2 = model.IntegerType("test_field_2", max=1000, min=10)
    test_field_3 = model.BooleanType("test_field_3", default=False)
