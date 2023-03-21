import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.tyhjakortti = Maksukortti(0)

    def test_kassa_oikeanlainen(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisosto_toimii_edullisella(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(vaihto, 260)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kateisosto_toimii_edullisella_kun_ei_tarpeeksi(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihto, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateisosto_toimii_maukkaalla(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(vaihto, 100)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateisosto_toimii_maukkaalla_kun_ei_tarpeeksi(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihto, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_toimii_edullisella_kun_tarpeeksi(self):
        vaihto = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(vaihto, True)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_korttiosto_toimii_edullisella_kun_ei_tarpeeksi(self):
        vaihto = self.kassa.syo_edullisesti_kortilla(self.tyhjakortti)
        self.assertEqual(vaihto, False)
        self.assertEqual(self.kassa.edulliset, 0)
    def test_korttiosto_toimii_maukkaalla_kun_tarpeeksi(self):
        vaihto = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(vaihto, True)
        self.assertEqual(self.kassa.maukkaat, 1)
    def test_korttiosto_toimii_maukkaalla_kun_ei_tarpeeksi(self):
        vaihto = self.kassa.syo_maukkaasti_kortilla(self.tyhjakortti)
        self.assertEqual(vaihto, False)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortin_lataaminen(self):
        self.kassa.lataa_rahaa_kortille(self.tyhjakortti, -500)
        self.assertEqual(str(self.tyhjakortti), "Kortilla on rahaa 0.00 euroa")
        self.kassa.lataa_rahaa_kortille(self.tyhjakortti, 500)
        self.assertEqual(str(self.tyhjakortti), "Kortilla on rahaa 5.00 euroa")

