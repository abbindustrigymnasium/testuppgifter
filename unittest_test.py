import unittest


####################några funktioner#################################
def add(a,b):
    return a+b
    
def equal(a,b):
    return a==b

def convertToInt(a):
    return int(a)

#############################test funktioner nedan####################
class TestAddFunction(unittest.TestCase):
    def testAddPos(self):
        self.assertEqual(add(3,5),8) #3+5=8
    
    def testAddNeg(self):
        self.assertEqual(add(-10,5),-5) #-10+5=-5

    def testAddZero(self):
        self.assertEqual(add(0,0),0) #0+0=0


class TestEqualFunction(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(equal(1,1)) #1==1 is true
    
    def testfalse(self):
        self.assertFalse(equal(2,-2)) #2==-2 is false


class TestConvertFunction(unittest.TestCase):
    def testException(self):
        with self.assertRaises(ValueError):
            convertToInt("hej")

########################anrop av testfunktionerna##################
if __name__=='__main__':
    unittest.main()