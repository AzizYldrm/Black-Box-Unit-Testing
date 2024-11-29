import unittest
import primeNeighbor as pn

class PrimeNeighborTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test010(self):
        actualResult = pn.primeNeighbor(upperBound=0 )
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)





