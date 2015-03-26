import stoch as st
import unittest
import numpy as np

class TestStoch(unittest.TestCase):

    def setUp(self):
        self.prices = np.array([[1.1194,1.1380,1.1181],
                                [1.1193,1.1245,1.1169],
                                [1.1182,1.1187,1.1179],
                                [1.1179,1.1240,1.1159],
                                [1.1181,1.1217,1.1148],
                                [1.1080,1.1192,1.1056],
                                [1.1030,1.1114,1.0986],
                                [1.0842,1.1032,1.0838],
                                [1.0836,1.0837,1.0823],
                                [1.0847,1.0906,1.0831],
                                [1.0686,1.0848,1.0668],
                                [1.0551,1.0717,1.0509],
                                [1.0622,1.0694,1.0494],
                                [1.0494,1.0630,1.0459],
                                [1.0498,1.0506,1.0470],
                                [1.0569,1.0619,1.0478],
                                [1.0593,1.0651,1.0550],
                                [1.0826,1.1035,1.0577],
                                [1.0668,1.0919,1.0608],
                                [1.0821,1.0882,1.0654],
                                [1.0838,1.0883,1.0833]])
        
        self.prices = self.prices[::-1]

    def test_k_list(self):
        """
        Length of result list equals defined length
        """
        self.assertEqual(len(st.k_list(self.prices, 5)), 5)     

    def test_highest_high(self):
        """
        // Depends on test setup
        """
        self.assertEqual(st.highest_high(st.highs(self.prices)), 1.138)
    
    def test_lowest_low(self):
        """
        // Depends on test setup
        """
        self.assertEqual(st.lowest_low(st.lows(self.prices)), 1.0459)    

    def test_k(self):
        """
        Check k-value for %k-period of 14
        """
        self.assertTrue(st.k(self.prices, 14) != False)    
        self.assertTrue(st.k(self.prices, 14) > 0)    
        self.assertEqual((1.0838 - 1.0459)/(1.1035 - 1.0459) * 100, st.k(self.prices, 14))

    def test_stoch(self):
        """
        Result is dict type with keys "k" & "d"
        """
        self.assertTrue("k" in st.stoch(self.prices))
        self.assertTrue("d" in st.stoch(self.prices))
        """
        Result values are of type => float
        """
        self.assertTrue(isinstance(st.stoch(self.prices)["k"], (float)))
        self.assertTrue(isinstance(st.stoch(self.prices)["d"], (float)))

        """
        Test prices would lead to a bullish k-d-configuration
        """
        self.assertTrue(st.stoch(self.prices)["k"] > st.stoch(self.prices)["d"])
        
        print st.stoch(self.prices)

    def test_is_bullish(self):
        self.assertTrue(st.is_bullish(self.prices)) 


"""
MAIN
"""
if __name__ == '__main__':
    unittest.main()