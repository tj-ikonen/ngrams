import unittest
import n_grams

class test_units(unittest.TestCase):
    
    def wordCounting(self):
        txt = n_grams.Text("simpleText.txt")
        self.assertTrue(txt.word_count() == 2)
        
test_units().wordCounting()