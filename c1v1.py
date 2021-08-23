import ctypes


# using C1V1 = C2V2
C2 = 0.3 # Vodka concentration at the end
v2 = 2.0 #final diluated solution amount

c1 = 0.4 #initial vodka concentration

v1 = (C2*v2) / c1


MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None,  str(v1), 'V1 amount', 0)