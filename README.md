This repository exists to document working examples for Python's `unittest.mock`.

# Usage

Explore `examples/` directory, modify tests and run `pytest` in the root directory to use this repository.

```console
$ git clone https://github.com/kwk/python-mock-examples.git
$ cd python-mock-examples
$ pytest
============================================ test session starts =============================================
platform linux -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/kkleine/src/python-mock-examples
configfile: pytest.ini
testpaths: examples/tests
plugins: darkgraylib-1.2.1, anyio-3.7.1
collected 4 items                                                                                            

examples/tests/mymodule_test.py::MyTestWithSetUp::test_greet PASSED
examples/tests/mymodule_test.py::MyTestWithDecoratedMethod::test_greet PASSED
examples/tests/mymodule_test.py::MyTestWithDecoratedClass::test_greet PASSED
examples/tests/mymodule_test.py::MyTestWithArg::test_greet PASSED

============================================= slowest durations ==============================================

(12 durations < 0.005s hidden.  Use -vv to show these durations.)
============================================= 4 passed in 0.02s ==============================================
```

