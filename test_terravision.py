# test_terravision.py
"""
Tests for TerraVision module.
"""

import unittest
from terravision import TerraVision

class TestTerraVision(unittest.TestCase):
    """Test cases for TerraVision class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TerraVision()
        self.assertIsInstance(instance, TerraVision)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TerraVision()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
