import testslide

class TestHello(testslide.TestCase):
    def test_hello(self):
        self.assertEqual("hello", "hello")
