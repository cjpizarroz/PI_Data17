<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1 - DATA17** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>


<hr>  

## **Descripción del problema**

## Rol a desarrollar

Trabajar como **`Data Scientist`** a partir de datos de  "Steam", una plataforma multinacional de videojuegos. <br>
Revise los datos y me di cuenta que la madurez de los mismos es nula :sob: : Datos anidados, de tipo raw, no hay procesos automatizados para la actualización de nuevos productos, entre otras cosas… 

Realice un trabajo rápido de **`Data Engineer`** y consegui tener un **`MVP`** (_Minimum Viable Product_) para el cierre del proyecto! 

## **Propuesta de trabajo**

**`Transformaciones`**:  Se realizaron algunas transformaciones de datos. Me enfoque principalmente en leer el dataset con el formato correcto. Elimine las columnas que no necesito para responder las consultas o preparar el modelo de aprendizaje automático, y de esa manera optimizar el rendimiento de la API y el entrenamiento del modelo.

**`Feature Engineering`**:  En el dataset *user_reviews* se incluyen reseñas de juegos hechos por distintos usuarios. Cree la columna ***'sentiment_analysis'*** aplicando análisis de sentimiento con NLP con la siguiente escala: el valor '0' si es malo, '1' si es neutral y '2' si es positivo. Esta nueva columna reemplazo la de user_reviews.review para facilitar el trabajo de los modelos de machine learning y el análisis de datos. A los valores nulos, le asigne el valor de `1`.

**`Desarrollo API`**:   Se disponibilizo los datos de la empresa usando el framework ***FastAPI***.  Para la elaboración de las consultas.<br>
Las consultas solicitadas son las siguientes:

+ def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.
  
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,
			     "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **UsersWorstDeveloper( *`año` : int* )**:
   Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **sentiment_analysis( *`empresa desarrolladora` : str* )**:
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total 
    de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor. 

Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}

<br/>


> `Importante`<br>
Las consultas tienen que ser por intermedio de una API, para que pueda ser consumida segun los criterios de [API REST o RESTful](https://rockcontent.com/es/blog/api-rest/) desde cualquier dispositivo conectado a internet. 


**`Deployment`**: Se utilizo Render [Render](https://render.com/docs/free#free-web-services), para poder disponibilizar la api en internet
<br/>


**`Modelo de aprendizaje automático`**: 

Se solicito hacer un  **sistema de recomendación**.<br>
El modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto, se recomiendan similares. Aquí el input es un juego y el output es una lista de juegos recomendados, para ello aplique la *similitud del coseno*. 

Sistema de recomendación item-item:
+ def **recomendacion_juego( *`id de producto`* )**:
    Ingresando el id de producto, debe retornar una lista con 5 juegos recomendados similares al ingresado.



**`Video`**: Se genero un video mostrando la funcionalidad de las consultas😉


## **Fuente de datos**

+ [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj): Carpeta con el archivo que requieren ser procesados, tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link): Diccionario con algunas descripciones de las columnas disponibles en el dataset.
<br/>

## **Material de apoyo**

En este mismo repositorio podrás encontrar algunos (hay repositorios con distintos sistemas de recomendación) [links de ayuda](https://github.com/HX-PRomero/PI_ML_OPS/raw/main/Material%20de%20apoyo.md). Recuerda que no son los unicos recursos que puedes utilizar!

***Contacto: Carlos Javier Pizarro  pizarrocarlosjavier@gmail.com***


