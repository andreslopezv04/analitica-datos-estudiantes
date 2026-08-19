# Clase 14 · Reto — Tu primer modelo de machine learning

**Curso:** Analítica de Datos · Universidad Cooperativa de Colombia
**Momento 3 · Clase 14 de 16**

Este es el entregable de la clase.

---

## La situación

Un equipo médico tiene diez mediciones de rutina de 442 pacientes diabéticos (edad, sexo, índice de masa
corporal, presión arterial y seis análisis de sangre) y, para cada uno, un indicador de cómo progresó la
enfermedad un año después.

La pregunta es directa: **¿se puede anticipar la progresión de la enfermedad a partir de las mediciones
de hoy?** Y la pregunta detrás: si se puede, ¿qué medición es la que más informa?

Tu trabajo no es conseguir el mejor número. Es construir el modelo, medirlo con honestidad y decir qué
se puede y qué no se puede afirmar con él.

---

## Datos

**No hay archivo CSV. El dataset viene dentro de scikit-learn.**

```python
from sklearn.datasets import load_diabetes
```

| Campo | Valor |
|-------|-------|
| Filas | 442 pacientes |
| Variables de entrada | 10, todas numéricas y ya estandarizadas |
| Variable objetivo | Progresión de la enfermedad a un año (número continuo) |
| Nulos | Ninguno |
| Limpieza necesaria | Ninguna |

Es un dataset distinto al del demo: otro dominio, otro archivo, otra escala. La técnica es la misma.

### Las diez variables de entrada

| Nombre | Qué es |
|--------|--------|
| `age` | Edad |
| `sex` | Sexo |
| `bmi` | Índice de masa corporal |
| `bp` | Presión arterial promedio |
| `s1` a `s6` | Seis mediciones de suero sanguíneo |

Todas vienen centradas y escaladas, así que sus valores no se leen en unidades originales. Para un árbol
de decisión eso da igual: los árboles no necesitan variables escaladas.

---

## Aviso importante antes de empezar

**En este dataset todos los modelos sobreajustan.** Incluso el más simple.

Es esperado: 442 filas y diez variables ruidosas es un problema difícil, y un árbol de decisión
individual no es la herramienta adecuada. No hiciste nada mal.

La conclusión correcta de este reto **no** es "encontré el mejor modelo". Es algo del estilo:

> El mejor `max_depth` está entre 3 y 5, con un R2 de prueba alrededor de 0.33, y aun así el gap supera
> 0.10. Un árbol de decisión individual no generaliza bien en este problema.

**Que un modelo salga malo no es un error tuyo. No reportarlo sí lo es.**

---

## Qué hay que entregar

Cuatro partes. Se trabajan en clase con acompañamiento; lo que quede se cierra en casa.

### Parte 1 · Cargar, explorar y partir

- Cargar el dataset y armarlo como DataFrame.
- Confirmar la forma y la ausencia de nulos.
- Definir `X` (las diez variables) e `y` (la progresión).
- Partir 80/20 con `random_state=42`.

Antes de seguir, responde por escrito: **¿esto es regresión o clasificación? ¿Por qué?**

### Parte 2 · Curva de overfitting

Entrena un `DecisionTreeRegressor` para cada valor de `max_depth` en:

```
{2, 3, 5, 10, 20, None}
```

Para cada uno registra: R2 de entrenamiento, R2 de prueba, gap y MAE de prueba.

Entrega:

1. Una **tabla** con los seis resultados y una columna de diagnóstico según la regla del gap.
2. Un **gráfico** con las dos curvas (entrenamiento y prueba) contra la profundidad.
3. Una **respuesta escrita**: qué profundidad elegirías y por qué. No vale "la que da mejor test": hay
   que justificar con el gap.

Recuerda la regla:

```
gap < 0.05       bien
gap 0.05 - 0.10  aceptable
gap > 0.10       SOBREAJUSTE
```

### Parte 3 · Clasificador

Convierte el mismo problema en clasificación:

1. Corta la variable objetivo en **tres categorías** (`Baja`, `Media`, `Alta`) con `pd.qcut`, que parte
   por terciles.
2. Entrena un `DecisionTreeClassifier` con al menos tres profundidades distintas.
3. Evalúa con `accuracy_score` sobre entrenamiento y prueba.
4. Compara contra el punto de referencia: con tres clases balanceadas, adivinar al azar acierta el 33%.

Pregunta a responder: **¿el clasificador funciona mejor que el regresor, o solo lo parece porque la
métrica es distinta?**

### Parte 4 · Importancia de variables

1. Extrae `feature_importances_` del mejor modelo de la Parte 2.
2. Grafícalas ordenadas.
3. Escribe la interpretación: qué variables mandan, y qué **no** se puede concluir de eso.

La interpretación tiene que mencionar explícitamente que la importancia **no es causalidad**.

---

## Opcional (no se hace en clase, se cierra en casa)

Marcado como `OPCIONAL` en el starter. No entra en la nota mínima.

- **`min_samples_leaf`** como segunda palanca contra el sobreajuste. Prueba 1, 5, 10, 20 y 50 con
  `max_depth=5` y mira qué le pasa al gap.
- **El modelo tonto.** Compara tu mejor modelo contra `DummyRegressor(strategy="mean")`, que siempre
  predice la media. Si tu modelo no le gana, no tienes modelo.
- **Dibujar el árbol** con `sklearn.tree.plot_tree` para un `max_depth=3`. Es la ventaja de este
  algoritmo: se puede leer.

---

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegues familiarizado a las clases
6, 12 y 15. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen peso**:
no se suman ni se promedian, alimentan una sola banda por dimensión.

| Dimensión | Qué se mira en este reto |
|-----------|--------------------------|
| **Saber** | La profundidad elegida se justifica con el gap, no con el máximo del test. Y la lectura correcta de las importancias: asociación, no causalidad |
| **Ser** | Honestidad: el sobreajuste se reporta, y no hay métricas de entrenamiento presentadas como resultado |
| **Hacer** | Partición 80/20 con `random_state` y evaluación **solo** sobre prueba, curva de overfitting con las seis profundidades (tabla, gráfico y columna de gap), clasificador con terciles bien construidos y accuracy comparada contra el 33%, y gráfico de importancias ordenado |

**Topes por omisión** (techo a la banda, nunca resta, y no se acumulan):

- Reportar la métrica de entrenamiento como el desempeño del modelo: **Ser** no pasa de Insuficiente.
- Omitir el gap o esconder que todos los modelos sobreajustan: **Ser** no pasa de Insuficiente.
- Concluir que `max_depth=None` es el mejor modelo porque su R2 de entrenamiento es 1.000: **Saber**
  no pasa de Insuficiente.
- Interpretar `feature_importances_` como causalidad ("el `bmi` causa la progresión"): **Saber** no
  pasa de Insuficiente.
- Usar `r2_score` para el clasificador o `accuracy_score` para el regresor: **Hacer** no pasa de
  Aceptable.

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
- [ ] La tabla de la Parte 2 tiene las seis profundidades y la columna de gap.
- [ ] El gráfico de la curva tiene ejes rotulados y leyenda.
- [ ] La profundidad elegida está justificada con el gap.
- [ ] La Parte 3 compara la accuracy contra el 33% de referencia.
- [ ] La interpretación de la Parte 4 dice explícitamente que no es causalidad.
- [ ] Ninguna métrica de entrenamiento está presentada como resultado del modelo.

---

## Conexión con el Momento 3

La sección de machine learning de tu proyecto final tiene que responder cuatro preguntas:

1. **¿Qué predijiste?** La variable objetivo, y por qué le importa a alguien.
2. **¿Es regresión o clasificación?** Y por qué esa y no la otra.
3. **¿Cómo evaluaste?** Métrica sobre el conjunto de **prueba**, más el gap contra entrenamiento.
4. **¿Qué decisión soporta la predicción?** Si no soporta ninguna, el modelo sobra.

Este reto es un ensayo completo de esa sección, con un dataset que no es el tuyo.

Y no olvides el otro requisito del Momento 3, de la clase 13: mínimo **dos intervalos de confianza y
una prueba de hipótesis**.
