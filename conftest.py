import pytest
import os

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="production", help="my option: type1 or type2"
    )

@pytest.fixture(scope="session")
def env(request):
    """Fixture to get environment from command line"""
    return request.config.getoption("--env")