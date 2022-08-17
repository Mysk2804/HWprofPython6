import unittest
from parameterized import parameterized
from main import command_people, command_add, command_delete, documents, directories

add_list = [
    ("10006"),
    ("11-2")
]

del_list = [
    ("2207 876234", f'Документ 2207 876234 был удален с базы'),
    ("10006", f'Документ 1006 был удален с базы')
]

get_list = [
    ("pasport", "10006", "Oleg Olegovski", "3")

]

class Test_command(unittest.TestCase):

    @parameterized.expand(del_list)
    def test_command_delete(self, a, b):
        result = command_delete(documents, directories, a)
        self.assertEqual(result, b)

    @parameterized.expand(add_list)
    def test_command_people(self, a):
        self.assertTrue(command_people(documents, a))

    @parameterized.expand(get_list)
    def test_command_add(self, a, b, c, d):
        self.assertTrue(command_add(documents, directories, a, b, c, d))

