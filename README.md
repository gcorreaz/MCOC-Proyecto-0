# MCOC-Proyecto-0

<b> <H1> Introducción </H1> </b> 

En este proyecto se ilustra con algun ejemplo el efecto de perdida de significancia en  operaciones  de  aritmetica  de  punto  flotante.

<b> <H1> Ejemplo </H1> </b> 

Aquí se puede visualizar, a modo de ejemplo, como el coeficiente de asimetría de Fisher pierde significancia al aumentar el tamaño de la muestra. También es posible ver la diferencia entre ocupar un float32 y float64 en la operación, logrando con esta última mayor precisión en el resultado

Se implementan y comparan 3 ideas.

         1 - Definir un arreglo "a" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float64 y usar la función skew() para conocer el coef. de asimetría.
         2-. Definir un arreglo "a" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float64 y crear una función el cual permite conocer el coef. de asimetría
         3-. Definir un arreglo "b" con numeros aleatorias desde el 0 al 9 y tipo de datos dtype=sp.float32 y crear una función el cual permite conocer el coef. de asimetría
        

<b> <H1> Resultados </H1> </b> 
         Se procede a calcular el coeficiente de asimetría de Fitcher para cada uno de las ideas planteadas. De esta forma, se podrá visualizar la variación que tiene esta operación para un mismo arreglo.
         Luego, se conoce como error relativo:

         ERROR = (Promedio_Calculado - Resultado_Exacto) / Resultado_Exacto
         
Luego, llamaremos:

        Error #1 = Diferencia que se produce entre el coeficiente de asimetría planteado 3 y en 1.
        Error #2 = Diferencia que se produce entre el coeficiente de asimetría planteado 4 y en 1.
        
A continuación se muestra como va creciendo el error relativo en la medida en que se consideran cada vez mas dígitos. Esto se produce principalmente debido a la perdida de significancia.


<img src="https://prnt.sc/kf5mbg">

        
Output de la consola:        

        N = 10
         Coeficiente de Asimetria en 1 =  0.0010001456686  ,  error =  0.0
         Coeficiente de Asimetria en 2 =  0.00102016582627  ,  error1 =  0.020017241786
         Coeficiente de Asimetria en 3 =  0.00102016577919  ,  error2 =  0.0200171947134
          
         N = 11
         Coeficiente de Asimetria en 1 =  0.0010001456686  ,  error =  0.0
         Coeficiente de Asimetria en 2 =  0.00102016582627  ,  error1 =  0.020017241786
         Coeficiente de Asimetria en 3 =  0.00102016577919  ,  error2 =  0.0200171947134

         N = 12
         Coeficiente de Asimetria en 1 =  0.0010001456686  ,  error =  0.0
         Coeficiente de Asimetria en 2 =  0.00102016582627  ,  error1 =  0.020017241786
         Coeficiente de Asimetria en 3 =  0.00102016577919  ,  error2 =  0.0200171947134

         N = 13
         Coeficiente de Asimetria en 1 =  0.0010001456686  ,  error =  0.0
         Coeficiente de Asimetria en 2 =  0.00102016582627  ,  error1 =  0.020017241786
         Coeficiente de Asimetria en 3 =  0.00102016577919  ,  error2 =  0.0200171947134

         N = 14
         Coeficiente de Asimetria en 1 =  0.0010001456686  ,  error =  0.0
         Coeficiente de Asimetria en 2 =  0.00102016582627  ,  error1 =  0.020017241786
         Coeficiente de Asimetria en 3 =  0.00102016577919  ,  error2 =  0.0200171947134





# Anexos

1-. https://www.ejemplode.com/17-html/81-ejemplo_de_como_colocar_imagenes_con_html.html
2-. https://glosarios.servidor-alicante.com/terminos-estadistica/coeficiente-de-asimetria-de-fisher


