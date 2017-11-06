#zadanie pierwsze
def podzielNapis(napis):
  slownik = {}
  lista = napis.split()
  print 'lista po podziale'
  print lista
  while (len(lista) != 0):
    slownik[lista[0].replace(':', '')] = lista[1]
    del lista[0]
    del lista[0]
  print 'slownik'
  return slownik

def rozwiazanieZTablicy(napis):
  slownik = {}
  for x in napis.split('\n'):
    elem = x.split(": ")
    slownik[elem[0]] = elem[1]
  return slownik

napis = '''k1: w1
k2: w2
k3: w3'''


print  podzielNapis(napis)
print rozwiazanieZTablicy(napis)

#zadanie drugie
import sys

def wczytajIPodzielZPliku(path):
  plik = open(path)
  slownik = {}
  for x in plik:
    print x
    elem = x.split(": ")
    slownik[elem[0]] = elem[1].replace('\n','')
  plik.close()
  return slownik


print wczytajIPodzielZPliku(sys.argv[1])

#zadanie trzecie
import sys

def wczytajIPoliczZPliku(path):
  plik = open(path)
  slownik = {}
  for line in plik:
    for word in line.split():
        if(None == slownik.get(word)):
            slownik[word] = 1
        else:
            slownik[word] += 1
  plik.close()
  return slownik


print wczytajIPoliczZPliku(sys.argv[1])

#zadanie czwarte
#!/usr/bin/env python
# encoding: utf-8

import sys

def znajdzWPliku(path, toFind):
  plik = open(path)
  for line in plik:
    if ( -1 != line.find(toFind)):
        print line.replace("\n","")
  plik.close()
        
def znajdzZWejscia(toFind):
  lista = []
  for line in sys.stdin:
    if  len(line.strip()) == 0:
        break
    lista.append(line)
  for line in lista:
    if ( -1 != line.find(toFind)):
        print line.replace("\n","") 

sciezka = sys.argv[1]
ciag = sys.argv[2]

if( '-' != sciezka):
    znajdzWPliku(sciezka, ciag)
else:
    znajdzZWejscia(ciag)
#zadanie piate
import sys

def parsujPlik(path):
    plik = open(path)
    lista = []
    for line in plik:
        lista.append(line.replace("\n",''))
    plik.close()
    return lista

def zapiszDoPliku(path, string):
    plik = open(path, 'w')
    plik.write(string)
    plik.close()
    
def caesar(plainText, shift): 
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                cipherText += finalLetter
    print "Your ciphertext is: ", cipherText
    return cipherText

def caesar2(plaintext, shift):
    ciphertext = ""
    for c in plaintext:
        if c.isalpha(): ciphertext += I2L[ (L2I[c] + shift)%26 ]
    else: ciphertext += c
    
sciezkaDoWczytania = sys.argv[1]
sciezkaDoZapisania = sys.argv[2]

print caesar2(parsujPlik(sciezkaDoWczytania), 2)
zapiszDoPliku(sciezkaDoZapisania, caesar2(parsujPlik(sciezkaDoWczytania), 2))
