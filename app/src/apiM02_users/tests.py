from django.test import SimpleTestCase


class TestUrls(SimpleTestCase):
    def test_env_file(self):
        assert 1 == 2