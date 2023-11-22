
try:
  from pytest import *
  print("modulo importado")
except ImportError:
  print("error importando modulo")
  