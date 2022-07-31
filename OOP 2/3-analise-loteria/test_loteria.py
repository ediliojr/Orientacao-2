from loteria import Loteria

def test_loteria():
  loteria = Loteria
  loteria.sorteio()

  assert len(loteria.sorteio()) == 6
  assert type(loteria.sorteio()) is list
