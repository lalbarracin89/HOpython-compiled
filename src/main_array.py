import ctypes as C
import numpy as np

intp = C.POINTER(C.c_int)
flp = C.POINTER(C.c_float)

math = C.CDLL('./mylib.so')


N = 5

#inicializacion de variables int

int_a = np.array([1 , 2, 3, 4, 5], dtype=C.c_int)
int_b = np.array([10, 9, 8, 7, 6], dtype=C.c_int)
int_res = np.zeros(N, dtype=C.c_int) 


#Suma int 

math.add_int_array(int_a.ctypes.data_as(intp), 
					int_b.ctypes.data_as(intp), 
					int_res.ctypes.data_as(intp), 
					C.c_int(N))
print int_res


#inicializacion de variables float

math.add_float.restype = C.c_float
float_a = np.array([1.0 , 2.0, 3.0, 4.0, 5.0], dtype=C.c_float)
float_b = np.array([10.0, 9.0, 8.0, 7.0, 6.0], dtype=C.c_float)
float_res = C.c_float()
print type(float_res)

#Producto float

float_res(float_a.ctypes.data_as(flp),
						float_b.ctypes.data_as(flp),
						C.c_int(N))
						
print cd type(float_res)


