import unittest

from tools.mock_tools import (
    calculator_add,
    calculator_multiply,
    get_policy,
    get_product_info,
    get_weather,
)

class MockToolTest(unittest.TestCase):
    def test_product(self):
        result = get_product_info.invoke({"name": "노트북"})
        self.assertIn("재고 4개", result)

    def test_policy(self):
        result = get_policy.invoke({"keyword": "환불"})
        self.assertIn("7일", result)

    def test_weather(self):
        result = get_weather.invoke({"city": "광주"})
        self.assertIn("25도", result)

    def test_calculator(self):
        self.assertEqual(calculator_add.invoke({"a": 2, "b": 3}), 5)
        self.assertEqual(calculator_multiply.invoke({"a": 6, "b": 7}), 42)

if __name__ == "__main__":
    unittest.main()
