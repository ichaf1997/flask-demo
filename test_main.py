from main import app
import unittest

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    
    def test_page_context(self):
        """测试页面返回内容是否正确"""
        response = self.client.get("/")
        self.assertEqual(response.data, b"This A Flask Demo !")


    def test_page_code(self):
        """测试页面返回状态码是否正确"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
