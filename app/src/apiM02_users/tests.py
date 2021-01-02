from django.test import SimpleTestCase
from decouple import config
config.encoding = 'cp1251'


# Create your tests here.
class DEV_1(SimpleTestCase):
    def test_env_file(self):
        print(config('LANGUAGE_CODE'))
        # Verifica si existe LANGUAGE_CODE en el archivo env
        assert config('LANGUAGE_CODE') == "es-gt"