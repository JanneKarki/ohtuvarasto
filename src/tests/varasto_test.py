import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_varastosta_liikaa(self):
        self.varasto.ota_varastosta(1000)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_liikaa(self):
        tila = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(tila+10)
        self.assertEqual(self.varasto.paljonko_mahtuu(),0)

    def test_varaston_alku_saldo_negatiivinen(self):
        self.varasto = Varasto(10, -10)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_alle_nolla(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_alku_saldo_nolla(self):
        self.varasto = Varasto(0,0)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_alku_saldo_suurempi_kuin_tilavuus(self):
        self.varasto = Varasto(10, 20)
        self.assertEqual(self.varasto.saldo, 10)


    def test_ota_varastosta_alle_nolla(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(-10)
        self.assertEqual(self.varasto.saldo, 10)

    def test_str_method(self):
        tuloste = self.varasto.__str__()
        self.assertEqual(tuloste, f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")