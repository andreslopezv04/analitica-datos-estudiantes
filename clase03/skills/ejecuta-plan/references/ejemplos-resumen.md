# Ejemplos de resumen de paso

Un buen resumen es corto, trae cifras y le sirve a quien lo lea dentro de tres semanas, que casi
siempre es usted.

Los ejemplos de abajo son de un trabajo con datos y de un trabajo con texto. La forma del resumen
es la misma en los dos, y en cualquier otro: que quedo, con cifras.

## Sirven

```markdown
- [x] 1. Cargar el archivo de consumo y mirar su forma
  > 9.000 filas, 12 columnas. Faltantes concentrados en ESTRATO (312) y
  > FECHA_LECTURA (588). CONSUMO_M3 viene con coma decimal, hay que
  > leerlo con decimal=",".

- [x] 3. Quitar los registros sin fecha de lectura
  > 9.000 filas antes, 8.412 despues: se fueron 588 (6,5%), todas de 2019.
  > No se toco ninguna otra columna.

- [x] 4. Calcular el consumo promedio mensual por estrato
  > Tres filas, una por estrato, en metros cubicos al mes. Estrato 1: 18,4.
  > Estrato 2: 22,1. Estrato 3: 411,2.
  > OJO: el 411,2 esta fuera del rango del criterio de aceptacion (10 a 40).
  > La comprobacion falla y no sigo al paso 5.

- [x] 2. Redactar la seccion de antecedentes del informe
  > Dos paginas, 640 palabras. Las cuatro fuentes del encargo quedaron
  > citadas; la quinta no se consiguio en acceso abierto.
  > OJO: la fuente de 2018 contradice a la de 2021 en la cifra de cobertura.
  > Lo dejo anotado y lo resuelvo en el paso 4.
```

## No sirven, y por que

```markdown
- [x] 3. Quitar los registros sin fecha de lectura
  > Listo.
```
Muy corto. No dice cuanto se fue, que es justo lo unico que importaba.

```markdown
- [x] 4. Calcular el consumo promedio por estrato
  > Se agrupo la tabla por la columna ESTRATO usando el metodo groupby, sobre
  > el cual se aplico la funcion mean a la columna CONSUMO_M3, y despues se
  > ordeno el resultado de mayor a menor usando sort_values...
```
Muy largo, y ademas cuenta el como en lugar del que. El trabajo hecho ya esta ahi para eso.

```markdown
- [x] 4. Calcular el consumo promedio por estrato
  > Quedo bien, los numeros se ven razonables.
```
Vago, y sospechoso: "se ven razonables" no es una comprobacion. Cual era el rango, cual fue la
cifra.

## Reglas del resumen

- Empiece por lo que quedo, no por como se hizo
- Cifras siempre: el antes y el despues, el valor obtenido, el limite esperado
- Nombre los objetos exactos: el archivo, la columna, la seccion
- Marque con **OJO:** lo que hay que recordar mas adelante
- Dos o tres lineas, salvo que el paso lo justifique
- Si la comprobacion fallo, el resumen lo dice, y dice que no se siguio
