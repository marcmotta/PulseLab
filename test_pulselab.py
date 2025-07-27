# test_pulselab.py
"""
Tests for PulseLab module.
"""

import unittest
from pulselab import PulseLab

class TestPulseLab(unittest.TestCase):
    """Test cases for PulseLab class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PulseLab()
        self.assertIsInstance(instance, PulseLab)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PulseLab()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
