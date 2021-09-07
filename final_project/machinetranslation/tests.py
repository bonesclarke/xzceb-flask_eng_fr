import unittest

from translator import englishToFrench, frenchToEnglish

class Test_e2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(0),0) # test if null
        
unittest.main()