¿Cuál es el separador de columnas (coma , o punto y coma ;)?
El separador entre columnas en los archivoc Lineas, Objetivos y Procesos es una ",". En el archivo Indicadores_Finales es un ";".

¿La primera fila contiene los nombres de las columnas (encabezados)? ¿Son claros?
En algunos encabezados el nombre si que es claro en cambio hay algunos encabezados que son bastante confusos, sobretodo cuando se trata de hacer relaciones entre los diferentes archivos.

Inspecciona visualmente las primeras 20-30 filas. ¿Ves valores que te parezcan extraños o que faltan (celdas vacías, "N/A", "s/d")?
Si, en el archivo Indicadores_Finales podemos ver algunos valores extraños y varias filas con algunas celdas vacías.

¿Los formatos son consistentes? Por ejemplo, ¿las fechas están siempre como DD/MM/AAAA o a veces cambian?
Solo tenemos fechas en el archivo Indicadores_Finales en la columna de cursos y siempre se repite la misma estructura, como la de este ejemplo "2021/22".

Identifica las "claves" o "IDs" que podrían servir para relacionar unos ficheros con otros (ej: id_alumno en el fichero de calificaciones.csv y también en alumnos.csv).
En el archivo de Indicadores_Finales podemos utilizar como clave la columna de Identificador.
En el archivo de Lineas podemos utilizar como clave la columna de Linea.
En el archivo de Objetivos podemos utilizar como clave la columna de Objetivo_PAA.
En el archivo de Procesos podemos utilizar como clave la columna de Proceso.

Relaciones:
Entre Lineas y Objetivos, el numero de linea. 
Entre Procesos e Indicadores una parte del id de Indicadores se ralaciona con proceso de Procesos.
Entre Indicadores y Objetivos se relaciona una parte de Cod_PAA de Indicadores con Objetivo_PAA de Objetivo.

