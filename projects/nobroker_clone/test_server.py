import unittest
import server


class TaxServer(unittest.TestCase):
    def test_admin_registration(self):
        
        with self.assertRaises(TypeError):
            server.admin_registration()
            server.owner_registration()
            server.user_registration()
            

if __name__ == '__main__':
    unittest.main()
