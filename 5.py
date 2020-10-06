Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Aprendizaje automático 02

importar  numpy  como  np

# TECNICAS DE APILAMIENTO

print ( 'Tecnicas De Apilamiento \ n ' )
print ( '1) Horizontal \ n 2) Vertical \ n 3) En Profundidad \ n 4) Por Columnas \ n 5) Por Filas \ n ' )
print ( 'Opción:' )
opción  =  int ( entrada ())

# Matrices Inciales

a  =  np . arange ( 9 ). remodelar ( 3 , 3 )
b  =  a * 3

imprimir ( 'a = \ n ' , a , ' \ n ' )
imprimir ( 'b = \ n ' , b , ' \ n ' )

si  opción  ==  1 :
    print ( 'Apilamiento horizontal = \ n ' , np . hstack (( a , b )))
 opción  elif ==  2 :
    print ( 'Apilamiento vertical = \ n ' , np . vstack (( a , b )))
 opción  elif ==  3 :
    print ( 'Apilamiento en profundidad = \ n ' , np . dstack (( a , b )))
 opción  elif ==  4 :
    print ( 'Apilamiento por columnas = \ n ' , np . column_stack (( a , b )))
 opción  elif ==  5 :
    print ( 'Apilamiento por filas = \ n ' , np . row_stack (( a , b )))
otra cosa :
    imprimir ( 'Opcion Invalida' )

# ------------------------------------------------- -----------------

# DIVISION DE ARRAYS

print ( 'División de matrices \ n ' )
print ( '1) Horizontal \ n 2) Vertical \ n 3) En Profundidad \ n ' )
print ( 'Opción:' )
opción  =  int ( entrada ())

# Matrices Inciales

c  =  np . arange ( 9 ). remodelar ( 3 , 3 )
d  =  np . arange ( 27 ). remodelar ( 3 , 3 , 3 )

si  opción  ==  1 :
    imprimir ( c , ' \ n ' )
    print ( 'División horizontal = \ n ' , np . hsplit ( c , 3 ), ' \ n ' )
 opción  elif ==  2 :
    imprimir ( c , ' \ n ' )
    print ( 'División vertical = \ n ' , np . vsplit ( c , 3 ), ' \ n ' )
 opción  elif ==  3 :
    imprimir ( d , ' \ n ' )
    print ( 'División en profundidad = \ n ' , np . dsplit ( d , 3 ), ' \ n ' )
otra cosa :
    imprimir ( 'Opcion Invalida' )

# ------------------------------------------------- -----------------

# PROPIEDADES DE LOS ARRAYS

imprimir ( b , ' \ n ' )

print ( ' \ n numero de dimenciones:' , b . ndim )

print ( 'numero de elementos:' , b . tamaño )

print ( 'número de bytes por elemento:' , b . tamaño del artículo )

print ( 'numero total de bytes:' , b . nbytes , ' \ n ' )


b . redimensionar ( 6 , 4 )
imprimir ( b , ' \ n ' )
print ( 'Transpuesta:' , b . T )


b  =  np . matriz ([ 1.j  +  1 , 2.j  +  3 ])

print ( 'parte complejo: \ n ' , b )

print ( 'parte real:' , b . real , ' \ n ' )

print ( 'parte imaginario:' , b . imag )