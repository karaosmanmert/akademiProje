import unittest

# Test edeceğimiz fonksiyonlar
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "0'a bolme islemi yapilamaz!"
    else:
        return a / b

# Test sınıfı
class TestCalculator(unittest.TestCase):
    def test_topla(self):
        self.assertEqual(topla(3, 5), 8)
        self.assertEqual(topla(-1, 1), 0)

    def test_cikar(self):
        self.assertEqual(cikar(10, 5), 5)
        self.assertEqual(cikar(0, 7), -7)

    def test_carp(self):
        self.assertEqual(carp(4, 5), 20)
        self.assertEqual(carp(-2, 3), -6)

    def test_bol(self):
        self.assertEqual(bol(10, 2), 5)
        self.assertEqual(bol(10, 0), "0'a bolme islemi yapilamaz!")
        self.assertAlmostEqual(bol(7, 3), 7/3)

if __name__ == "__main__":
    unittest.main()
