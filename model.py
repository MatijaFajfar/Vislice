STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = '+'
POJNOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'burek'

import random

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo.upper()
        self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return set(self.pravilne_crke()) == set(self.geslo)

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += '_'
        return niz

# zanimivost        ''.join([crka if crka in self.crke else '_' for crka in self.geslo])

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return POJNOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open('besede.txt', encoding = 'utf8') as bazen:
        bazen_besed = bazen.read().split('\n')

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


class Vislice:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if not self.igre:
            return 0
        else:
            return max(self.igre.keys()) + 1
#        id = random.randint()
#        while id in self.igre:
#            id = random.randint()
#        return id

    def nova_igra(self):
        i = self.prost_id_igre()
        igra = nova_igra()
        self.igre[i] = (igra, ZACETEK)
        return i

    def ugibaj(self, i, crka):
        igra, stanje = self.igre[i]
        stanje = igra.ugibaj(crka)
        self.igre[i] = (igra, stanje)
