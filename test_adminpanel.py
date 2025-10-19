# test_adminpanel.py
"""
Tests for AdminPanel module.
"""

import unittest
from adminpanel import AdminPanel

class TestAdminPanel(unittest.TestCase):
    """Test cases for AdminPanel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AdminPanel()
        self.assertIsInstance(instance, AdminPanel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AdminPanel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
