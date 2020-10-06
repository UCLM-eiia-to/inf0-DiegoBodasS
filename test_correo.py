# Ésto son las pruebas, déjalas donde están, no las toques
# pero léelas. Aunque no las entiendas hay información útil
# para saber lo que tienes que hacer

import unittest
class Test(unittest.TestCase):

    def test_01_devuelve_una_cadena(self):
        from correo import  my_email
        self.assertEqual(str,type(my_email()))

    def test_02_contiene_una_arroba(self):
        from correo import  my_email
        self.assertEqual(1,my_email().count('@'))

    def test_03_es_direccion_de_alumno(self):
        from correo import  my_email
        self.assertTrue(my_email().endswith('@alu.uclm.es'))

    def test_04_no_contiene_espacios(self):
        from correo import  my_email
        email = my_email()
        self.assertFalse(' ' in email)
        self.assertFalse('\t' in email)
        self.assertFalse('\n' in email)
        self.assertFalse('\r' in email)

if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
