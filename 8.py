# Taller Validacion Regresion y Clasificacion

importar  numpy  como  np , os
desde el  preprocesamiento de importación de sklearn  


# PROCESAMIENTO DIGITAL

imprimir ( ' \ n Procesamiento Digital \ n ' )
print ( '1) Binarizar los datos \ n '
      '2) Media y desviacion estandar (SIN ESCALAR) \ n '
      '3) Media y desviacion estandar (DESPUES DE ESCALAR) \ n '
      '4) Escalamiento Min Max \ n '
      '5) Normalización de datos \ n ' )
print ( 'Opción:' )
opción  =  int ( entrada ())

# Datos iniciales
input_data  =  np . matriz ([[ 5.1 , - 2.9 , 3.3 ],
                       [ - 1.2 , 7.8 , - 6.1 ],
                       [ 3.9 , 0.4 , 2.1 ],
                       [ 7.3 , - 9.9 , - 4.5 ]])

print ( " \ n Datos iniciales = \ n " , input_data )


si  opción  ==  1 :
    data_binarized  =  preprocesamiento . Binarizador ( umbral = 2,1 ). transformar ( input_data )
    print ( " \ n Datos binarizados = \ n " , data_binarizados )

 opción  elif ==  2 :
    print ( "Media =" , input_data . mean ( axis = 0 ))
    print ( "Desviación estándar =" , input_data . std ( axis = 0 ))

 opción  elif ==  3 :
    data_scaled  =  preprocesamiento . escala ( input_data )
    print ( "Media =" , data_scaled . mean ( axis = 0 ))
    print ( "Desviación estándar =" , data_scaled . std ( axis = 0 ))

 opción  elif ==  4 :
    data_scaler_minmax  =  preprocesamiento . MinMaxScaler ( feature_range = ( 0 , 1 ))
    data_scaled_minmax  =  data_scaler_minmax . fit_transform ( input_data )
    print ( " \ n Min max escalamiento de datos: \ n " , data_scaled_minmax )

 opción  elif ==  5 :
    data_normalized_l1  =  preprocesamiento . normalizar ( input_data , norm = 'l1' )
    data_normalized_l2  =  preprocesamiento . normalizar ( input_data , norm = 'l2' )
    print ( " \ n L1 dato normalizado: \ n " , data_normalized_l1 )
    print ( " \ n L2 dato normalizado: \ n " , data_normalized_l2 )

otra cosa :
    imprimir ( 'Opcion Invalida' )
    os . sistema ( 'cls' )

# ------------------------------------------------- -----------------
