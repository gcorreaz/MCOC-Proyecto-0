# MCOC-Proyecto-0

<b> <H1> Introducción </H1> </b> 

En este proyecto se ilustra con algun ejemplo el efecto de perdida de significancia en  operaciones  de  aritmetica  de  punto  flotante.

<b> <H1> Ejemplo </H1> </b> 

Aquí se puede visualizar, a modo de ejemplo, como el coeficiente de asimetría de Fisher pierde significancia al aumentar el tamaño de la muestra. También es posible ver la diferencia entre ocupar un float32 y float64 en la operación, logrando con esta última mayor precisión en el resultado

Se implementan y comparan 4 ideas.

         1 - Definir un arreglo "a" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float64 y usar la función skew().
         2-. Definir un arreglo "b" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float32 y usar la función skew(). 
         3-. Definir un arreglo "a"  con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float64 y crear una función el cual permite conocer el coef. de asimetría
         4-. Definir un arreglo "b" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float32 y crear una función el cual permite conocer el coef. de asimetría
        

<b> <H1> Resultados </H1> </b>          
