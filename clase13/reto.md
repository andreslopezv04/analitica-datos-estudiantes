# Clase 13 · Reto — Inferencia sobre la educación en Colombia

**Curso:** Analítica de Datos · Universidad Cooperativa de Colombia
**Momento 3 · Clase 13 de 16**

Este es el entregable de la clase.

---

## La situación

Eres analista de datos contratado por el Ministerio de Educación Nacional. Te entregan la serie
histórica de indicadores educativos por departamento y te hacen tres preguntas:

1. ¿Qué podemos afirmar sobre los indicadores nacionales, y con cuánta seguridad?
2. ¿Los departamentos urbanizados y los rurales dispersos tienen resultados académicos distintos?
3. ¿La cobertura educativa cambió entre la década pasada y la actual?

Tu trabajo no es responder "sí" o "no". Es responder **con cuánta certeza**, con cuánto tamaño, y
escribirlo de forma que un funcionario que no sabe estadística pueda tomar una decisión con eso.

---

## Datos

**Archivo:** `../datos/educacion_estadisticas.csv`

Es el mismo archivo del demo. **Las variables no son las mismas.**

| | Demo | Reto |
|--|------|------|
| Variables de los intervalos | `tasa_matriculacion_5_16` | `cobertura_neta`, `aprobacion`, `repitencia` |
| Variables de las pruebas | `desercion` | `aprobacion`, `cobertura_bruta` |
| Comparaciones | Urbanizado vs rural disperso | Urbanizado vs rural disperso **y** dos periodos |

**No hay ningún otro archivo de datos para esta clase.** No busques una carpeta `data/` en `clase13/`:
no existe.

### Columnas que vas a usar

| Columna | Qué mide |
|---------|----------|
| `ano` | Año del registro (2011-2024) |
| `c_digo_departamento` | Código DANE del departamento (entero, limpio) |
| `cobertura_neta` | % de la población en edad escolar matriculada en el nivel que le corresponde |
| `cobertura_bruta` | % de matriculados sobre la población en edad escolar, sin importar el nivel. Puede superar 100 |
| `aprobacion` | % de estudiantes que aprueban el año |
| `repitencia` | % de estudiantes que repiten el año |

### Lo que ya sabes que está sucio

Lo viste en el demo. La limpieza mínima ya viene escrita en el starter:

- `ano` llega como decimal (`2018.0`).
- `departamento` está inconsistente (`'Guainia'` y `'Guainía'` son el mismo). El paso 0 lo
  estandariza con la receta de la clase 3, pero **la llave sigue siendo `c_digo_departamento`**:
  un código no tiene ortografía.
- Hay 20 pares (año, departamento) duplicados. Se eliminan.
- Hay nulos dispersos. Se aplica `dropna()` por columna y **se reporta el `n` resultante**.
- `tamano_promedio_grupo` tiene valores imposibles. No la uses.

---

## Qué hay que entregar

Cuatro partes. Se trabajan en clase con acompañamiento; lo que quede se cierra
en casa.

### Parte 1 · Tres intervalos de confianza al 95%

Para `cobertura_neta`, `aprobacion` y `repitencia`:

- `n`, media y desviación estándar.
- Intervalo de confianza al 95% con `stats.t.interval`.
- **Una frase de interpretación correcta** por cada uno.

Recuerda: `dropna()` antes de calcular, siempre. Y en `scale` va el **error estándar**, no la
desviación estándar.

### Parte 2 · Dos pruebas de hipótesis

Con los **cuatro pasos completos** cada una:

1. Plantear H0 y H1 en español, antes de mirar los datos.
2. Elegir alfa.
3. Calcular estadístico y p-valor.
4. Decidir y redactar.

| Prueba | Pregunta | Grupos |
|--------|----------|--------|
| **A** | ¿La tasa de aprobación difiere entre territorios? | Urbanizado vs rural disperso |
| **B** | ¿La cobertura bruta cambió entre periodos? | 2011-2018 vs 2019-2024 |

Usa `stats.ttest_ind(..., equal_var=False)` en las dos. Reporta descriptivos **antes** del test.

> **Advertencia.** Una de las dos pruebas va a dar significativa y la otra no. Eso es un resultado, no
> un error. **No cambies los grupos, ni los años, ni la columna, buscando que dé menor a 0.05.**
> Eso se llama p-hacking y aquí se penaliza. Un resultado no significativo bien reportado vale más que
> uno significativo fabricado.

### Parte 3 · Resumen ejecutivo

De 5 a 7 frases, dirigido a **un funcionario del Ministerio de Educación** que no sabe estadística.

Tiene que:

- Decir qué encontraste y **de cuánto** es cada diferencia, en puntos porcentuales.
- Incluir la incertidumbre en lenguaje llano ("con los datos disponibles, la diferencia está entre X y
  Y puntos").
- Decir claramente cuando **no** hubo evidencia suficiente.
- Terminar con una recomendación accionable.

No puede:

- Contener las palabras "p-valor", "hipótesis nula", "estadísticamente significativo" ni "t-test".
- Decir que una cosa **causa** la otra. Estos son datos observacionales.
- Afirmar nada sin número.

### Parte 4 · Dos visualizaciones de significancia

1. **Gráfico de barras de error** con los tres intervalos de confianza de la Parte 1.
   Pista: `plt.errorbar` con `yerr` igual a la **mitad** del ancho del intervalo, no al intervalo
   completo.
2. **Boxplot comparativo** de la prueba A, con la anotación del resultado sobre el gráfico.

Ejes rotulados, título que diga el hallazgo (no "Gráfico 1"), y unidades visibles. Las reglas de la
clase 8 siguen vigentes.

---

## Opcional (no se hace en clase, se cierra en casa si te sobra tiempo)

Está marcado como `OPCIONAL` en el starter. No entra en la nota mínima.

- Calcular a mano el intervalo de confianza **de la diferencia** en cada prueba, con la fórmula de
  Welch.
- Repetir la prueba A con `stats.mannwhitneyu` (prueba no paramétrica) y comentar si la conclusión
  cambia.
- Calcular el d de Cohen como medida estandarizada del tamaño del efecto.

---

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegues familiarizado a las clases
6, 12 y 15. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen peso**:
no se suman ni se promedian, alimentan una sola banda por dimensión.

| Dimensión | Qué se mira en este reto |
|-----------|--------------------------|
| **Saber** | Los 4 pasos con H0 y H1 escritas **antes** del cálculo, y la interpretación: ninguna de las tres malinterpretaciones del p-valor, ninguna aceptación de H0 |
| **Ser** | Honestidad: el resultado no significativo se reporta como tal, sin maquillarlo. Y el resumen ejecutivo, sin jerga, con números y con recomendación |
| **Hacer** | Corrección técnica (`dropna()` aplicado, error estándar en `scale`, `equal_var=False`, `n` reportado) y visualizaciones legibles solas, rotuladas, con la anotación de significancia |

**Topes por omisión** (techo a la banda, nunca resta, y no se acumulan):

- Interpretar el IC como "95% de probabilidad de que el valor esté ahí": **Saber** no pasa de
  Insuficiente.
- Escribir "se acepta H0" o "se demostró que no hay diferencia": **Saber** no pasa de Insuficiente.
- Reportar solo el p-valor, sin tamaño del efecto: **Saber** no pasa de Aceptable.
- Evidencia de p-hacking en la prueba B: **Ser** no pasa de Insuficiente.
- Notación científica en el resumen ejecutivo (`p = 5.4e-12` en vez de `p < 0.001`): **Ser** no pasa
  de Bueno.

---

## Formato de reporte que se te exige

Los cuatro elementos, en este orden:

1. **Tamaño del efecto** en unidades del negocio.
2. **Intervalo de confianza** de ese efecto.
3. **P-valor** y tamaños de muestra.
4. **Frase en lenguaje llano.**

Ejemplo del demo:

> Los departamentos con área metropolitana grande registran una deserción escolar 1.55 puntos
> porcentuales menor que los de Amazonía, Orinoquía y Chocó (3.57% frente a 5.12%). La diferencia es
> estadísticamente significativa (IC 95% de la diferencia: [-1.97, -1.14]; t = -7.39; p < 0.001;
> n = 139 y n = 116).

Reglas de formato: `p < 0.001` cuando corresponda, tres decimales en el resto, siempre el `n`, y
"se asocia con" en lugar de "causa".

---

## Archivos

| Archivo | Qué es |
|---------|--------|
| `reto_starter.ipynb` | Tu punto de partida. Aquí trabajas |
| `README.md` | Este documento |

---

## Entrega

Sube `reto_starter.ipynb` resuelto al aula virtual.

Antes de subir:

- [ ] Kernel > Restart & Run All corre sin errores de punta a punta.
- [ ] Los tres intervalos están calculados **y** interpretados.
- [ ] Las dos pruebas tienen H0 y H1 escritas.
- [ ] El resumen ejecutivo no contiene la palabra "p-valor".
- [ ] Las dos visualizaciones tienen título, ejes rotulados y unidades.
- [ ] El `n` de cada cálculo está reportado.

---

## Conexión con el Momento 3

Para el proyecto final de la clase 15 necesitas, como mínimo, **dos intervalos de confianza y una
prueba de hipótesis** sobre tu propio dataset, reportados con este mismo formato.

Lo que practicas hoy es literalmente una sección de tu entrega final.
