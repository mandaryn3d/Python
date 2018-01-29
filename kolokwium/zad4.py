




class Pojazd:
    marka = None
    kolor = None
    przebieg = 0
    def __init__(self, marka, kolor, przebieg):
        self.marka = marka
        self.kolor = kolor
        self.przebieg = przebieg
    def zmienKolor(self, kolor):
        self.kolor = kolor
    def przejedzDystans(self, odleglosc):
        self.przebieg += odleglosc
    def __str__(self):
        return self.marka + ' ' + self.kolor + ' ' + str(self.przebieg)
        
        
class Osobowy(Pojazd):
    iloscMiejsc = 0
    pojemnoscBagaznika = 0
    czyMaSystemWspomagania = False
    def __init__(self, marka, kolor, przebieg, iloscMiejsc, pojemnoscBagaznika, czyMaSystemWspomagania):
        self.marka = marka
        self.kolor = kolor
        self.przebieg = przebieg
        self.iloscMiejsc = iloscMiejsc
        self.pojemnoscBagaznika = pojemnoscBagaznika
        self.czyMaSystemWspomagania = czyMaSystemWspomagania
    def zainstalujWspomaganie(self):
        self.czyMaSystemWspomagania = True
    def sprawdzCzyZmiesciSieWBagazniku(self, objetosc):
        return self.pojemnoscBagaznika >= objetosc

class Ciezarowy(Pojazd):
    iloscMiejsc = 0
    czyMaPrzyczepe = False
    maksymalnaPojemnosc = 0
    zajeteMiejsce = 0
    def __init__(self, marka, kolor, przebieg, iloscMiejsc, czyMaPrzyczepe, maksymalnaPojemnosc):
        self.marka = marka
        self.kolor = kolor
        self.przebieg = przebieg
        self.iloscMiejsc = iloscMiejsc
        self.czyMaPrzyczepe = czyMaPrzyczepe
        self.maksymalnaPojemnosc = maksymalnaPojemnosc
    def doczepPrzyczepe(self):
        self.czyMaPrzyczepe = True
    def zaladujTowar(self, objetosc):
        if self.czyMaPrzyczepe:
            if self.zajeteMiejsce + objetosc <= self.maksymalnaObjetosc:
                self.zajeteMiejsce += objetosc
                
                
                
                
                
class Salon:
    lokalizacja = None
    nazwa = None
    marka = None
    samochody = []
    def __init__(self, lokalizacja, nazwa, marka):
        self.lokalizacja = lokalizacja
        self.nazwa = nazwa
        self.marka = marka
    def dodajPojazd(self, samochod):
        self.samochody.append(samochod)
    def sprzedajPojazd(self, samochod):
        self.samochody.remove(samochod)


s = Salon('LBN', 'salon mercedesa', 'mercedes')

c = Ciezarowy('mercedes', 'czerwony', 1000, 2, False, 50)

s.dodajPojazd(c)
s.sprzedajPojazd(c)

