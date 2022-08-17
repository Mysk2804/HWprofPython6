import unittest
from parameterized import parameterized
from YaApi import put_file

new_list = [
    ('testststs', 'Папка testststs создана в директории'),
    ("testststs", 'DiskPathPointsToExistentDirectoryError')
]
token = ''

class Test_yaapi(unittest.TestCase):

    def setUp(self) -> None:
        print("Metod setUP")


    def tearDown(self) -> None:
        print("Metod tearDown")



    @parameterized.expand(new_list)
    def test_putfile(self, a, b):
        result = put_file(a, token)
        self.assertEqual(result, b)

