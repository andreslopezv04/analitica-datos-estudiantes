# Analítica de Datos — repositorio de estudiantes

**Este repositorio es un destino, no una fuente. Aquí no se escribe material a mano.**

Si usted (persona o agente) llegó aquí a redactar una diapositiva, un notebook, una consigna de reto
o a corregir un dato: está en el repositorio equivocado. Dé media vuelta.

## Los dos repositorios

| Repositorio | Ruta local | Qué es |
|-------------|-----------|--------|
| **Profesor** (fuente) | `/Users/juliangarzon/universdad/analitica-datos` | Fuente única. Todo el material se escribe ahí. Contiene además material interno que nunca sale: notas, rúbricas, soluciones, expectativas |
| **Estudiantes** (canal) | `/Users/juliangarzon/universdad/analitica-datos-estudiantes` — este repo | **Público.** Canal del estudiante. Solo recibe copias generadas |

- Repositorio del profesor en GitHub: <https://github.com/juliangarzon/analitica-datos>
- Repositorio de estudiantes en GitHub: <https://github.com/juliangarzon/analitica-datos-estudiantes>
  — es este repo. La misma URL aparece en `README.md` (dos veces) e `INSTALACION.md` (una vez), en
  los comandos `git clone`. Si alguna vez cambia, hay que actualizar los tres sitios.

El material llega aquí por un solo camino, ejecutado **desde el repo del profesor**:

```bash
python3 scripts/publicar_clase.py 4              # simulacion, no escribe nada
python3 scripts/publicar_clase.py 4 --aplicar    # copia de verdad
```

El script simula por defecto y **nunca commitea**. Después de `--aplicar`, el profesor revisa
`git status` aquí y commitea a mano.

## Qué NUNCA puede aparecer en este repositorio

Este repositorio es **público**. Cualquier cosa que llegue aquí es visible para el curso entero y
para internet, y borrarla después no la borra del historial de Git.

| Nunca | Por qué |
|-------|---------|
| `*_solucion.*` (`reto_solucion.ipynb`, `streamlit_app_solucion.py`) | El reto entrena la competencia que las rúbricas evalúan. Con la solución al lado no se practica: se copia |
| `professor_notes.md` | Guion interno. Contiene los tiempos de clase, que no van en manos del estudiante |
| `rubrica.md`, `expectativas_profesor.md`, `evaluaciones/` completo | Fuente única en el repo del profesor; al aula llegan por el canal institucional |
| `ESTETICA.md`, `slides/previews/` | Material de producción de los decks. Ruido |
| `plans/`, `base/`, `aula_virtual/` | Insumos internos e institucionales |

`scripts/publicar_clase.py` codifica esta lista negra: aborta la clase completa si alguno entra al
conjunto a copiar, y **audita este repositorio entero** después de cada corrida. Si el script reporta
`FILTRACION`, no haga push: borre el archivo y averigüe cómo llegó.

## Estructura

```
clase01/ ... clase16/     Material de cada clase
  README.md               Qué trae la clase (a mano)
  slides.html             Diapositivas                     (generado)
  demo.ipynb              Notebook del bloque 2            (generado)
  reto.md                 Consigna del bloque 3            (generado)
  reto.ipynb              Notebook de arranque del reto    (generado)
datos/                    Todos los CSV del curso, en un solo lugar
  README.md               Cómo se usan las rutas (a mano)
  *.csv                                                    (generado)
README.md                 Portada del curso para el estudiante (a mano)
INSTALACION.md            Cómo montar el entorno              (a mano)
verificacion.ipynb        Notebook que confirma el entorno    (a mano)
requirements.txt          Librerías del curso                 (a mano)
.gitignore                                                    (a mano)
```

`datos/` es **una sola carpeta en la raíz**, no una por clase. Los notebooks leen con
`../datos/<archivo>.csv`. El script reescribe `../../datasets/` y `../data/` a `../datos/` al copiar,
y aborta si después de reescribir queda un `read_csv` apuntando a una ruta inexistente aquí.

## Qué se edita a mano y qué no

Sin ambigüedad: la regla no es "nada se edita aquí", es "**lo que el script genera no se edita aquí**".

**Se edita a mano en este repositorio** (el script no los toca nunca; no están en su lista de orígenes):

- `README.md`
- `INSTALACION.md`
- `verificacion.ipynb`
- `requirements.txt`
- `.gitignore`
- `CLAUDE.md` (este archivo)
- `claseXX/README.md` y `datos/README.md`

**Nunca se edita a mano** (todo esto lo sobrescribe el próximo `publicar_clase.py`):

- `claseXX/slides.html`
- `claseXX/demo.ipynb`
- `claseXX/reto.md`
- `claseXX/reto.ipynb`
- `claseXX/*.py` publicados (por ejemplo `streamlit_demo.py`, `streamlit_app_starter.py`)
- `datos/*.csv`

## Cómo se corrige un error en el material

Una errata en una diapositiva, un `read_csv` roto, un enunciado confuso en un reto:

1. Se arregla **en el repo del profesor**, en el archivo de origen
   (`claseXX/slides/claseXX_*.html`, `claseXX/demo/demo.ipynb`, `claseXX/reto/README.md`, …).
2. Se vuelve a publicar: `python3 scripts/publicar_clase.py XX --aplicar`.
3. Se commitea aquí.

**No se parchea aquí.** Un arreglo hecho directamente sobre `claseXX/demo.ipynb` sobrevive hasta la
próxima publicación de esa clase y luego desaparece sin dejar rastro, mientras el error sigue vivo en
la fuente. Es exactamente la clase de divergencia silenciosa que el script existe para evitar.

Excepción: los archivos de la lista "se edita a mano" de arriba se corrigen aquí directamente, porque
aquí es donde viven. No tienen origen en el repo del profesor.

## Convenciones

- Todo en español. Se explica en español, se nombra en inglés: librerías, funciones, métodos y tipos
  conservan su nombre original (`groupby`, `dropna`, `DataFrame`, `outlier`, `overfitting`).
  Si el estudiante lo va a teclear o lo va a ver en un error, va en inglés; si lo va a leer para
  entender, va en español.
- Sin emojis en ningún archivo.
- Nada de trabajos de estudiantes aquí. El proyecto de cada equipo vive en el repositorio del equipo.

El contexto completo del curso (malla de las 16 clases, evaluación, contrato de los decks) está en el
`CLAUDE.md` del repo del profesor. Este archivo no lo duplica a propósito.
