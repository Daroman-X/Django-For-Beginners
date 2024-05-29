from django.test import TestCase
from django.test import SimpleTestCase

class PruebasEstado(SimpleTestCase):
    def test_inicio(self):
        respuesta=self.client.get("/")
        self.assertEqual(respuesta.status_code,200)
    
    def test_acerca_de(self):
        respuesta=self.client.get("/about/")
        self.assertEqual(respuesta.status_code,200)
        
