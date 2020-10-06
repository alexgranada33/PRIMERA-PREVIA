Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>   
# Aprendizaje automático 01

importar  numpy  como  np

# Creando un arreglo

print ( 'Dígito número de elementos:' )
n  =  int ( entrada ())
a  =  np . arange ( n )

print ( 'Arreglo a =' , a , ' \ n ' )
print ( 'Tipo de a =' , a . dtype , ' \ n ' )
print ( 'Dimensión de a =' , a . ndim , ' \ n ' )
print ( 'Número de elementos de a =' , a . shape )

# Creando un arreglo multidimensional

print ( ' \ n Digite numero de elementos para areglo 1:' )
f  =  int ( entrada ())
print ( 'Número de elementos para arreglo 2:' )
c  =  int ( entrada ())
m  =  np . matriz ([ np . arange ( f ), np . arange ( c )])
imprimir ( m );

# Utilización de arreglos multidimensionales

print ( 'Dígito número de elementos:' )
n  =  int ( entrada ())
print ( 'Número de bloques de dígitos:' )
b  =  int ( entrada ())
print ( 'Número de filas de dígitos:' )
f  =  int ( entrada ())
print ( 'Número de columnas de dígitos:' )
c  =  int ( entrada ())

z  =  np . arange ( n ). remodelar ( b , f , c )
imprimir ( 'z = \ n ' , z )

print ( 'Buscar un elemento en especifico \ n ' )
print ( 'Bloque:' )
b  =  int ( entrada ())
imprimir ( 'Fila:' )
f  =  int ( entrada ())
imprimir ( 'Columna:' )
c  =  int ( entrada ())
imprimir ( ' \ n z [b, f, c] =' , z [ b , f , c ])