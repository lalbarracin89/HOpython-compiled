import ctypes as C
import numpy as np
intp = C.POINTER(C.c_int)
math = C.CDLL('./mylib.so')

#inicializacion de variables int

int_a = np.array([1 , 2, 3, 4, 5], dtype=C.c_int)
int_b = np.array([10, 9, 8, 7, 6], dtype=C.c_int)
int_res = np.zeros(5, dtype=np.int16) 
int_n = 5

#Suma int 

math.add_int_array(int_a.ctype.data_as(intp), 
					int_b.ctype.data_as(intp), 
					int_res.ctype.data_as(intp),  
					C.c_int(int_n))
print int_res

#inicializacion de variables float

int_a = np.array([1.0 , 2.0, 3.0, 4.0, 5.0], dtype=C.c_float)
int_b = np.array([10.0, 9.0, 8.0, 7.0, 6.0], dtype=C.c_float)
int_res = np.zeros(5, dtype=np.float16) 

#Producto float

