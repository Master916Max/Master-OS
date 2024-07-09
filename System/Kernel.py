import os
import multiprocessing

#Init
def StartUp():
  from System.KP.SFRP import P4, P2
  error, code = P4()
  if code:
    print(error)
    exit()
  else:
  error, code = None, None
  error, code = P2()
  if code:
    print(error)
    exit()
  else:
    del error
    del code

def Run():
  pass
