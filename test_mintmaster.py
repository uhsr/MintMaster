# test_mintmaster.py
"""
Tests for MintMaster module.
"""

import unittest
from mintmaster import MintMaster

class TestMintMaster(unittest.TestCase):
    """Test cases for MintMaster class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintMaster()
        self.assertIsInstance(instance, MintMaster)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintMaster()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
