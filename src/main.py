import ctypes as C
math = C.CDLL('./mylib.so')
math.add_float.restype = C.c_float

#declaracion de variables

int_a = 3
int_b = 4

float_a = 3.0
float_b = 4.0

tres_int = C.c_int(3)
cuatro_int = C.c_int(4)
res_int = C.c_int()

tres_float = C.c_float(3)
cuatro_float = C.c_float(4)
res_float= C.c_float()

#Suma entre int por valor

suma_int = math.add_int(int_a, int_b)
print suma_int

#Suma entre float por valor

suma_float = math.add_float(C.c_float(float_a), C.c_float(float_b))
print suma_float

#Suma entre int por referencia

math.add_int_ref(C.byref(tres_int), C.byref(cuatro_int),C.byref(res_int))
print res_int.value

#Suma entre float por referencia

math.add_float_ref(C.byref(tres_float), C.byref(cuatro_float),C.byref(res_float))
print res_float.value
