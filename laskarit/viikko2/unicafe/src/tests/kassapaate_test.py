import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.rahamaara = Kassapaate(100000)

    def test_kateisosto_toimii_edullisella(self):
        self.rahamaara.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.rahamaara), "Kassassa on rahaa 100240 euroa")

    def test_kateisosto_toimii_maukkaalla(self):
        self.rahamaara.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.rahamaara), "Kassassa on rahaa 100400 euroa")

    def test_kortin_lataaminen(self):
        self.maksukortti = Maksukortti(1000)
        self.maksukortti.lataa_rahaa_kortille()
        self.assertEqual(str(self.rahamaara), "Kassassa on rahaa")
