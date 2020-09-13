
import unittest
import prime_number

class testPrimeNumber(unittest.TestCase):
    def testPrime(self):
        res = prime_number.prime(3)
        self.assertEqual(res,True)
    
    def testNotPrime(self):
        res = prime_number.prime(9)
        self.assertEqual(res,False)

if __name__ == "__main__":
    unittest.main()
