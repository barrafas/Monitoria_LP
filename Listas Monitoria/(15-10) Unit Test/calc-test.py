import calc
import unittest

def SetUpModule():
    print("SetUpModule")
    
def TearDownModule():
    print("TearDownModule")
    
class TestCalc(unittest.TestCase):
    def SetUpClass(cls):
        print("SetUpClass")
        
    def TearDownClass(cls):
        print("TearDownClass")
        
    def SetUp(self):
        print("SetUp")
        
    def TearDown(self):
        print("TearDown")
        
    def test_add_int_positivos(self):
        self.assertEqual(calc.add(10,20),30)
        
    def test_add_int_negativos(self):
        self.assertEqual(calc.add(-10,-20),-30)
    
    def test_add_float_grandes(self):
        self.assertAlmostEqual(calc.add(1.99999999999999999999999999999999,0.00000000000000000000000000000001),2)
        
    def test_subtract_int_positivos(self):
        self.assertEqual(calc.subtract(10,20),-10)
        
    def test_subtract_int_negativos(self):
        self.assertEqual(calc.subtract(-10,-20),10)
    
    def test_subtract_zero_e_float_positivo(self):
        self.assertEqual(calc.subtract(0,4.6),-4.6)
        
    def test_multiply_int_positivos(self):
        self.assertEqual(calc.multiply(10,20),200)
        
    def test_multiply_floats_negativos(self):
        self.assertAlmostEqual(calc.multiply(-1.589467,-4.336454),6.892650530018)
    
    def test_multiply_zero_e_int_positivo(self):
        self.assertEqual(calc.multiply(0,47890),0)
    
    def test_divide_dizima_periodica(self):
        self.assertAlmostEqual(calc.divide(10,3),3.3333,4)
        
    def test_divide_floats_negativos(self):
        self.assertAlmostEqual(calc.divide(-6.2,-0.5),12.4)
    
    def test_divide_int_positivo_por_zero(self):
        self.assertRaises(ValueError, calc.divide, 50, 0)
        
    def test_exp_int_positivo_com_expoente_zero(self):
        self.assertEqual(calc.exp(0,68),1)
        
    def test_exp_int_positivo_com_expoente_negativo(self):
        self.assertEqual(calc.exp(-2,19),1/361)
    
    def test_exp_int_positivo_com_expoente_decimal(self):
        self.assertAlmostEqual(calc.exp(0.5,58),7.62,2)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
    
    