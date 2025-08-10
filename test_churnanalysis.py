# test_churnanalysis.py
"""
Tests for ChurnAnalysis module.
"""

import unittest
from churnanalysis import ChurnAnalysis

class TestChurnAnalysis(unittest.TestCase):
    """Test cases for ChurnAnalysis class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChurnAnalysis()
        self.assertIsInstance(instance, ChurnAnalysis)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChurnAnalysis()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
