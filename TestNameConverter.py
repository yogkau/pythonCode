import PythonExcerscise as px   
import unittest

class TestNameConveter(unittest.TestCase):

    conv = px.NameConverter()

    def test_varName(self):
        self.assertEqual(self.conv.convertGetterName("getEmpName"),"emp_name")

    def test_instance(self):
        self.assertIsInstance(self.conv,px.NameConverter)

    def test_getterName(self):
        self.assertEqual(self.conv.convertGetterName("getEmpName123"),"emp_name123")

    def test_getterNameWithNumbers(self):
        self.assertEqual(self.conv.convertGetterName("get123"),"123")

if __name__ == "__main__":
    unittest.main()    