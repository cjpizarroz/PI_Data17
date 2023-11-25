from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi.encoders import jsonable_encoder 
import logging
import gc
import json


app = FastAPI()


#---------- END POINT NRO 1 --------------

@app.get("/get_data_ep1/")
async def PlayTimeGenre(genero):  # Agregar anotación de tipo y descripción
    """
    ***def PlayTimeGenre( genero: str ) : Debe devolver año con más horas jugadas para dicho género.***.<br>
    ***parametro: genero juego:***       Ingresar el genero del juego para realizar la consulta.<br>
    ***return:***      Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
    """
    try:
        df = pd.read_csv('CSV\consulta1.csv', sep=',', encoding='UTF-8')  
        df_filtrado = df[df[genero] == 1]
         # Agrupa por año y suma las horas de juego
        resumen = df_filtrado.groupby('release_date')['playtime_forever'].sum()
        anio_mas_horas = resumen.idxmax()
       
        return {
            "Año con más horas jugadas para Género "+genero : int(anio_mas_horas)
        }
    except Exception as e:
        return {"error": str(e)}   



#---------- END POINT NRO 2 --------------
@app.get("/get_data_ep2/")
async def UserForGenre(genero: str):  # Agregar anotación de tipo y descripción
    """
    ***def UserForGenre( genero: str ) : Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año***.<br>
    ***parametro: genero juego:***       El genero del juego para realizar la consulta.<br>
    ***return:***    Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas : 23}]}
    """
    try:
        df = pd.read_csv('CSV\consulta1.csv', sep=',', encoding='UTF-8')  

        df_filtrado = df[df[genero] == 1]

        # Agrupa por usuario y suma las horas de juego
        resumen = df_filtrado.groupby('user_id')['playtime_forever'].sum()

        usuario_mas_horas = resumen.idxmax()
        max_horas_jugadas = resumen.max()

        df1 = df_filtrado[df_filtrado['user_id'] == usuario_mas_horas]

        # Agrupa por usuario y año, y suma las horas de juego
        resumen = df1.groupby(['user_id', 'release_date'])['playtime_forever'].sum().reset_index()

        # Convierte el resultado en una lista de horas acumuladas por año
        horas_acumuladas_por_año = []
        for _, row in resumen.iterrows():
            horas_acumuladas_por_año.append({"Año": row["release_date"], "Horas": row["playtime_forever"]})

        return {
            "Usuario con más horas jugadas para Género " + genero: usuario_mas_horas,
            "Horas jugadas": horas_acumuladas_por_año
        }
    except Exception as e:
        return {"error": str(e)}
    



#---------- END POINT NRO 3 --------------

@app.get("/get_data_ep3/")
async def UsersRecommend(año: int):
    """
    ***def UsersRecommend( año: int ) : Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)***.<br>
    ***parametro: año juego:***       El año del juego para realizar la consulta.<br>
    ***return:***    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    """
    try:
        df3 = pd.read_csv('CSV\consulta3.csv', sep=',', encoding='UTF-8')
        df_filtrado = df3[df3['posted year'] == año] 
    
        # Agrupar por 'item_id' y contar los valores 2 en la columna 'sentimiento'
        conteo_sentimiento_2 = df_filtrado[df_filtrado['sentiment_analysis'] == 2].groupby('item_id').size()
    
        # Ordenar en orden descendente según el conteo
        conteo_sentimiento_2 = conteo_sentimiento_2.sort_values(ascending=False)
        top_3 = conteo_sentimiento_2.head(3)

        # Obtener títulos de los ítems más recomendados
        items_recomendados = top_3.index.tolist()
        titulos_recomendados = df3[df3['item_id'].isin(items_recomendados)][['item_id', 'title']] \
                                .drop_duplicates().set_index('item_id').loc[items_recomendados]
        
        # Obtener los títulos como una lista para el diccionario
        valores = titulos_recomendados['title'].values.tolist()

        # Crear el diccionario con claves fijas para los primeros 3 títulos
        claves = ['Primero: ', 'Segundo: ', 'Tercero: ']
        diccionario = dict(zip(claves, valores))
        return diccionario
        
       
    except Exception as e:
        return {"error": str(e)}
    
#---------- END POINT NRO 4 --------------  
@app.get("/get_data_ep4/")
async def UsersWorstDeveloper(año: int):
    """
    ***def UsersWorstDeveloper( año: int ) : Devuelve el top 3 de desarrolladores con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)***.<br>
    ***parametro: año ***       Ingrese un año para realizar la consulta.<br>
    ***return:***     Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    """
    try:

        df4 = pd.read_csv('CSV\consulta4.csv', sep=',', encoding='UTF-8')
        df_filtrado = df4[df4['posted year'] == año] 
        # Agrupar por 'item_id' y contar los valores 2 en la columna 'sentimiento'
        conteo_sentimiento_0 = df_filtrado[df_filtrado['sentiment_analysis'] == 0].groupby('item_id').size()
        # Ordenar en orden descendente según el conteo
        conteo_sentimiento_0 = conteo_sentimiento_0.sort_values(ascending=False)
        top_3 = conteo_sentimiento_0.head(3)
        # Obtener títulos de los ítems más recomendados
        items_menos_recomendados = top_3.index.tolist()
        developer_menos_recomendados = df4[df4['item_id'].isin(items_menos_recomendados)][['item_id', 'developer']] \
                                    .drop_duplicates().set_index('item_id').loc[items_menos_recomendados]
        developer_menos_recomendados = developer_menos_recomendados.reset_index(drop=True)
        clave = ['Primero: ', 'Segundo: ', 'Tercero: ']
        valor = developer_menos_recomendados['developer'].values
        # Crear un diccionario a partir de los arrays usando zip()
        diccionario = dict(zip(clave, valor))

        return diccionario
    except Exception as e:
        return {"error": str(e)}
 
    
#---------- END POINT NRO 5 --------------
@app.get("/get_data_ep5/")
async def sentiment_analysis(empresa: str):
    """
    ***def sentiment_analysis( empresa desarrolladora: str ) : Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentran categorizados con un análisis de sentimiento como valor.***.<br>
    ***parametro: empresa desarrolladora ***       Ingrese una empresa desarrolladora para realizar la consulta.<br>
    ***return:***     Ejemplo de retorno: {'Valve' : [Negativo = 182, Neutro = 120, Positivo = 278]}
    """
    try:      
        # Seleccionamos las columnas que vamos a usar y cargamos el dataframe a partir del archivo csv
        columnas = ['user_id','item_id', 'sentiment_analysis']
        df_users_reviews = pd.read_csv("CSV/australian_user_reviews.csv",usecols= columnas ,sep=",", encoding='UTF-8')
    
        # eliminamos los valores NaN
        df_users_reviews.dropna(inplace=True)
        # Convertimos a int los valores de la columna item:id
        df_users_reviews['item_id'] = df_users_reviews['item_id'].astype(int)

        # Seleccionamos las columnas que vamos a usar y cargamos el dataframe a partir del archivo csv
        columnas = ['item_id', 'developer']
        df_output_steam_games = pd.read_csv('CSV\output_steaam_games.csv', usecols=columnas, sep=',', encoding='UTF-8')

        # Unimos los dos dataframe
        df_merge = df_users_reviews.merge(df_output_steam_games, on='item_id')

        # Filtramos por developer
        df_filtrado = df_merge[df_merge['developer'] == empresa]

        # Obtengo el conteo de cada valor en la columna 'sentiment_analysis'
        conteo_sentimientos = df_filtrado['sentiment_analysis'].value_counts()

        # Almaceno los recuentos de cada valor en variables separadas
        valor_0 = conteo_sentimientos.get(0, 0)  # Si no hay valores 0, asigna 0
        valor_1 = conteo_sentimientos.get(1, 0)  # Si no hay valores 1, asigna 0
        valor_2 = conteo_sentimientos.get(2, 0)  # Si no hay valores 2, asigna 0

        # Preparo los datos para obtener la salida reequerida
        r0 = 'Negativo = '
        r1 = 'Neutro = '
        r2 = 'Positivo = '
        # Cargo en una lista el valor concatenado de los resultados con su respectivo mensaje
        lista = [f"{r0}{valor_0}",f"{r1}{valor_1}", f"{r2}{valor_2}"]
    
        return {empresa:lista}

        
    except Exception as e:
        return {"error": str(e)}
    
#---------- END POINT NRO 6 --------------
