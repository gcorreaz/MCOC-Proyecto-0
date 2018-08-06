# MCOC-Proyecto-0

<b> <H1> Introducción </H1> </b> 

En este proyecto se ilustra con algun ejemplo el efecto de perdida de significancia en  operaciones  de  aritmetica  de  punto  flotante.

<b> <H1> Ejemplo </H1> </b> 

Aquí se puede visualizar, a modo de ejemplo, como el coeficiente de asimetría de Fisher pierde significancia al aumentar el tamaño de la muestra. También es posible ver la diferencia entre ocupar un float32 y float64 en la operación, logrando con esta última mayor precisión en el resultado

Se implementan y comparan 4 ideas.

         1 - Definir un arreglo "a" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float64 y usar la función skew() para conocer el coef. de asimetría.
         2-. Definir un arreglo "b" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float32 y usar la función skew() para conocer el coef. de asimetría.  
         3-. Definir un arreglo "a" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float64 y crear una función el cual permite conocer el coef. de asimetría
         4-. Definir un arreglo "b" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float32 y crear una función el cual permite conocer el coef. de asimetría
        

<b> <H1> Resultados </H1> </b> 
         Se procede a calcular el coeficiente de asimetría de Fitcher para cada uno de las ideas planteadas. De esta forma, se podrá visualizar la variación que tiene esta operación para un mismo arreglo. Luego, como el arreglo está compuesto de numeros aleatorios, se procederá a calcular los respectivos coeficientes para tres arreglos distintos.
       


|                      | Coef. Asimetría en 1 | Coef. Asimetría en 2 | Coef. Asimetría en 3 | Coef. Asimetría en 4 |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
|        Primero       |  0.0226748540343     | 0.0202737223305      | 0.0222870794775      | 0.0202731641426      |
|        Segundo       | -0.030844182667      | 0.011177033807       | 0.0375461298091      | 0.0111774521023      |
|        Tercero       |  0.0376172129178     | 0.0122305747438      | 0.0375461298091      | 0.012294849748       |


Se conoce como error relativo:

         ERROR = (Promedio_Calculado - Resultado_Exacto) / Resultado_Exacto
         
Luego, llamaremos:

        Error #1 = Diferencia que se produce entre el coeficiente de asimetría planteado 3 y en 1.
        Error #2 = Diferencia que se produce entre el coeficiente de asimetría planteado 4 y en 1.
        Error #3 = Diferencia que se produce entre el coeficiente de asimetría planteado 2 y en 1.
        
Luego, los errores serán los siguientes:        


|                      | Error  #1            | Error #2             | Error #3             |
| -------------------- | -------------------- | -------------------- | -------------------- |
|        Primero       | 0.017101523841       | 0.105918648391       | 0.105894031345       |
|        Segundo       | 0.00050110012759     | 1.36238444775        | 1.36237088618        |
|        Tercero       | 0.00188964314842     | 0.673158939894       | 0.674867599296       |



Ahora, tambien es posible notar que a medida que aumenta la cantidad de datos, aumenta el error..
Esto se podrá ver reflejado en el siguiente grafico 
