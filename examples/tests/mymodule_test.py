from unittest import TestCase, mock

from mypackage.mymodule import Greeter, HelloAndBye, greet, greetWithArg


class MyTestWithSetUp(TestCase):
    def setUp(self):
        patcher = mock.patch("mypackage.mymodule.hello", return_value="Hola")
        # In case of exceptions, make sure to stop the patcher.
        # See https://docs.python.org/3/library/unittest.mock-examples.html#applying-the-same-patch-to-every-test-method
        self.addCleanup(patcher.stop)
        self.mock = patcher.start()

    def test_greet(self):
        self.assertEqual(greet("John Doe"), "Hola, John Doe")
        self.mock.assert_called_once()


class MyTestWithDecoratedMethod(TestCase):
    @mock.patch("mypackage.mymodule.hello", return_value="Hej")
    def test_greet(self, hello_mock):
        self.assertEqual(greet("John Doe"), "Hej, John Doe")
        hello_mock.assert_called_once()


class MyTestWithWith(TestCase):
    def get_return_value(self):
        return "Boh ya"

    def test_greet(self):
        with mock.patch(
            "mypackage.mymodule.hello", return_value=self.get_return_value()
        ) as hello_mock:
            self.assertEqual(greet("John Doe"), "Boh ya, John Doe")
            hello_mock.assert_called_once()


@mock.patch("mypackage.mymodule.hello", return_value="Hallo")
class MyTestWithDecoratedClass(TestCase):
    def test_greet(self, hello_mock):
        self.assertEqual(greet("John Doe"), "Hallo, John Doe")
        hello_mock.assert_called_once()


class MyTestWithArg(TestCase):
    @mock.patch("mypackage.mymodule.helloWithArg")
    def test_greet(self, helloWithArg_mock):
        # We dictate what helloWithArg() will return
        helloWithArg_mock.return_value = "Hello, John Doe"

        # Confirm the result is what we expect. It doesn't matter what the input
        # was to helloWithArg().
        self.assertEqual(greetWithArg("Foobar"), "Hello, John Doe")

        # Ensure helloWithArg() was passed the right value
        helloWithArg_mock.assert_called_once_with("Foobar")


# Only mock the hello() method,
# but keep the bye() method intact
class PartiallyMockObjectMethods(TestCase):
    def test_patch_hello(self):
        g = Greeter()

        with mock.patch.object(HelloAndBye, "hello") as m:
            m.return_value = "mocked return value"
            self.assertEqual(g.say_hello("John Doe"), "mocked return value")
            self.assertEqual(g.say_bye("John Doe"), "Bye, John Doe!")
