from reticulado import Reticulado
from barra import Barra

def caso_D():
	
	# Unidades base
	m = 1.
	kg = 1.
	s = 1. 
	
	#Unidades derivadas
	N = kg*m/s**2
	cm = 0.01*m
	mm = 0.001*m
	KN = 1000*N
	Pa = N / m**2
	KPa = 1000*Pa
	MPa = 1000*KPa
	GPa = 1000*MPa
	
	#Parametros
	L = 5.0 * m
	B = 2.0 * m
	H = 3.5 * m
	Z = 100 * m
	O = 10.0 * m
	
	A_X = 115.0 * m   
	A_Z = 70.0  * m
	
	#Inicializar modelo
	ret = Reticulado()

	#Nodos
	
	x = 43
	
	#Nodos Tablero
	for i in range(x+1):#47
		ret.agregar_nodo(O + i*L     , 0  ,  Z  )
	
	#Nodos en y = 2
	for i in range(x+1):#47
		ret.agregar_nodo(O + i*L     , B  ,  Z  )
		
	#Nodos arriba
	for i in range(x):#46
		ret.agregar_nodo(O + (2*i+1)*L/2   , B/2 ,  Z + H  )	
	
	#Nodos de apoyo
	ret.agregar_nodo(A_X  , 0 ,  A_Z  )	#140
	
	#Barras
	R = 100 *cm
	t = 50 *mm
	props = [R, t, 200*GPa, 7600*kg/m**3, 420*MPa]

	for i in range(x):
		ret.agregar_barra(Barra(i,i+1,*props))
		ret.agregar_barra(Barra(x+i+1,x+i+2,*props))
		
	for i in range(2*x+2,2*x+2+x-1):
		ret.agregar_barra(Barra(i,i+1,*props))
	
	for i in range(x):
		ret.agregar_barra(Barra(i,2*x+2+i,*props))
		ret.agregar_barra(Barra(x+1+i,2*x+2+i,*props))

	for i in range(2*x+2,2*x+2+x):
		ret.agregar_barra(Barra(i,i-x,*props))
		ret.agregar_barra(Barra(i,i-2*x-1,*props))
	
	for i in range (x+1):
		ret.agregar_barra(Barra(i,x+1+i,*props))
	
	for i in range(x):	
		ret.agregar_barra(Barra(i,x+i+2,*props))
		ret.agregar_barra(Barra(x+i+1,i+1,*props))
	
	#Apoyo
	ret.agregar_barra(Barra(131,21,*props))
	
	
	#Nodo 0  y 4 fijos
	ret.agregar_restriccion(0  , 0, 0)
	ret.agregar_restriccion(0  , 1, 0)
	ret.agregar_restriccion(0  , 2, 0)
	ret.agregar_restriccion(x+1, 0, 0)
	ret.agregar_restriccion(x+1, 1, 0)
	ret.agregar_restriccion(x+1, 2, 0)

	# Nodos 3 y 7 libres en X
	ret.agregar_restriccion(x    ,  1, 0)
	ret.agregar_restriccion(x    ,  2, 0)
	ret.agregar_restriccion(2*x+1,  1, 0)
	ret.agregar_restriccion(2*x+1,  2, 0)
	
	ret.agregar_restriccion(131  ,  0, 0)
	ret.agregar_restriccion(131  ,  1, 0)
	ret.agregar_restriccion(131  ,  2, 0)
    
	
	return ret

