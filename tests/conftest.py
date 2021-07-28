from NodeGraphQt import BaseNode
import pytest


class TestNode(BaseNode):
    __identifier__ = "UnitTest"
    NODE_NAME = "Test Node"


@pytest.fixture
def tnode():
    return TestNode()
