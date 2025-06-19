import pytest


@pytest.fixture
def data():
    return {
        "rating": ["0.000", "-0.4", "1.0", "2", "2.1", "2.11", "-0.09"],
        "brand": ["nokia", "siemens", "samsung", "apple", "xiaomi", "lg", "huawei"],
    }
