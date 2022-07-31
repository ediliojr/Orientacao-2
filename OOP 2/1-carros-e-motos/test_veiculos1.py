from unicodedata import numeric
from carro import Carro
from moto import Moto

fusca = Carro("Fusca", "Amarelo", 1980)
gol = Carro("Gol", "Prata", 2021)
honda_neo = Moto("Honda Neo", "Preto", 2022)
kawasaki = Moto("Kawasaki Ninja", "Verde", 2000)

def test_carro():
  assert type(fusca.buzinar()) is str
  assert type(fusca.hodometro) is int
  old_hodometro = fusca.hodometro
  fusca.dirigir()
  assert old_hodometro < fusca.hodometro
  assert fusca.abrir_porta_malas() is True

def test_moto():
  assert type(kawasaki.buzinar()) is str
  assert type(kawasaki.hodometro) is int
  old_hodometro = kawasaki.hodometro
  kawasaki.pilotar()
  assert old_hodometro < kawasaki.hodometro
