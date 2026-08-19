# Analítica de Datos — materiales del curso

Universidad Cooperativa de Colombia · Ingeniería de Sistemas · Curso 709749, 3 créditos · Semestre 2026-2.

Este repositorio es **el canal oficial del material del curso**. Aquí publico, antes de cada clase, las
diapositivas, el notebook del demo guiado, la consigna del reto y los datos que se necesitan.

No hay página web ni PDF por correo. Es este repositorio y nada más.

---

## Empiece aquí: [INSTALACION.md](INSTALACION.md)

**Antes de la clase 2 tiene que dejar el computador listo.** Todo el procedimiento, paso por paso y
explicando qué hace cada pieza, está en **[INSTALACION.md](INSTALACION.md)**: instalar Python,
clonar este repositorio, crear el entorno virtual, instalar las librerías, configurar VSCode y
verificar que funcione.

Está escrito para alguien que nunca ha abierto una terminal. Si ya sabe, va a ir rápido: los
comandos están separados por Windows y macOS y se copian tal cual.

Cuando termine, ejecute [`verificacion.ipynb`](verificacion.ipynb). Si ese notebook corre completo,
está listo.

---

## 1. Cómo se usa este repositorio

### La primera vez: clonar

Clonar significa "descargar una copia del repositorio a mi computador, conectada al original".
Se hace **una sola vez en el semestre**.

Abra una terminal, ubíquese en la carpeta donde quiera guardar el curso y ejecute:

```bash
git clone https://github.com/juliangarzon/analitica-datos-estudiantes.git analitica-datos
cd analitica-datos
```

La URL también queda publicada en el aula virtual.

### Cada semana: actualizar

Antes de cada clase, y desde dentro de la carpeta `analitica-datos`:

```bash
git pull
```

Eso trae el material nuevo. Si no lo hace, va a llegar a clase con la carpeta de la semana pasada.

> **Regla de oro: no edite los archivos de este repositorio.** Si modifica `demo.ipynb` y luego hace
> `git pull`, Git le va a reclamar un conflicto y usted no sabe resolverlo todavía (no es tema de este
> curso). Para trabajar en clase, **copie** el notebook a la carpeta de su equipo y edite la copia:
>
> ```bash
> cp clase02/demo.ipynb clase02/demo_mio.ipynb
> ```
>
> Si ya se le presentó el conflicto, la salida está en `INSTALACION.md`, sección 10, problema 7.

---

## 2. Qué hay en cada carpeta

```
clase01/ ... clase16/     Material de cada clase
  slides.html             Diapositivas. Se abren con doble clic, en cualquier navegador
  demo.ipynb              Notebook del bloque 2 (demo guiado), con el andamiaje ya escrito
  reto.md                 Consigna del bloque 3: qué hay que entregar y con qué criterios
  reto.ipynb              Notebook de arranque del reto
datos/                    Los CSV de todas las clases, en un solo lugar
requirements.txt          Las librerías del curso
INSTALACION.md            Cómo montar el entorno. Empiece por aquí
verificacion.ipynb        Notebook que confirma que el entorno quedó bien
```

Los notebooks leen los datos con una ruta relativa: desde `clase04/demo.ipynb`, el archivo está en
`../datos/HISTORICO_CONSUMO.csv`. **Esa ruta funciona sola si usted no mueve las carpetas.** Si abre el
notebook desde otro sitio y le da `FileNotFoundError`, casi siempre es eso.

**Todos los `demo.ipynb` y `reto.ipynb` empiezan igual:** una celda de texto *Antes de empezar* con la
rutina y los tres errores más frecuentes, y una celda de código que verifica el entorno (intérprete
correcto, librerías instaladas, CSV en su sitio). Ejecútela primero, siempre. Si falla, no siga: la
salida le dice qué hacer y a qué sección de [INSTALACION.md](INSTALACION.md) ir. El detalle está en la
sección 9.1 de ese manual.

No todas las clases tienen los cuatro archivos:

| Clase | Qué trae |
|-------|----------|
| 1 | Solo diapositivas. Es la clase de encuadre: no hay demo ni reto |
| 2, 3, 4, 5, 7, 8, 9, 10, 13, 14 | Diapositivas + demo + reto |
| 6, 12, 15 | Clases evaluativas. Sustentaciones. No hay demo ni reto |
| 11 | Laboratorio: se trabaja sobre el proyecto del equipo, no sobre un dataset del curso |
| 16 | Cierre del semestre |

---

## 3. Montar el entorno

El procedimiento completo está en **[INSTALACION.md](INSTALACION.md)**. No se repite aquí para que
haya un solo sitio que mantener.

Se hace una sola vez, idealmente **antes de la clase 2**. Si algo falla, lleve el error a clase: se
resuelve en los primeros minutos.

El resumen, si ya sabe lo que hace:

```bash
git clone https://github.com/juliangarzon/analitica-datos-estudiantes.git analitica-datos
cd analitica-datos
python3 -m venv .venv                 # en Windows: python -m venv .venv
source .venv/bin/activate             # en Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Y después, abrir `verificacion.ipynb` en VSCode con el kernel de `.venv` y ejecutarlo entero.
Requiere **Python 3.12 o superior**; se probó con 3.12. El `requirements.txt` fija versiones mínimas
para `pandas`, `numpy`, `scipy` y `scikit-learn`, y el porqué está en `INSTALACION.md`, sección 3.1.

Cada semana, lo único que hay que repetir es `git pull` y activar el entorno.

---

## 4. Git: se da por conocido

**Git no se enseña en este curso y no se evalúa en ninguna rúbrica.** No aparece como criterio en
ninguna parte: entregar con un solo commit que diga "entrega" vale exactamente igual que entregar con
cincuenta commits impecables. Lo único que Git determina es si hay entregable o no.

Pero sí se usa: es la vía por la que baja el material y por la que entrega los tres momentos. Con
`clone`, `add`, `commit`, `push` y `pull` le alcanza para todo el semestre.

Si no lo ha visto nunca, con esto se pone al día:

| Recurso | Qué es | Para qué le sirve aquí |
|---------|--------|------------------------|
| [Pro Git, en español](https://git-scm.com/book/es/v2) | El libro oficial de Git, completo y gratis | Capítulos 1 a 3. Es todo lo que este curso necesita |
| [Hello World de GitHub, en español](https://docs.github.com/es/get-started/start-your-journey/hello-world) | Guía de 15 minutos, sin instalar nada | El camino más corto para tener un repositorio funcionando hoy mismo |
| [Documentación oficial de Git](https://git-scm.com/doc) | Referencia de todos los comandos | Para consultar cuando algo falle, no para leer de corrido |

---

## 5. Su proyecto NO va en este repositorio

Este repositorio es de solo lectura para usted: yo publico, usted actualiza.

**El proyecto de su equipo vive en un repositorio propio**, que crea el equipo y se registra en la
clase 2 (nombre del equipo, integrantes y URL). Es uno solo para los tres momentos: el proyecto crece,
no se empieza de cero cada vez.

Ahí adentro van las tres entregas y el snapshot del CSV de su equipo. La estructura exacta, los
criterios de cada momento y la hora de corte están en las guías de entrega que se reparten en clase.

Nunca suba trabajos de estudiantes a este repositorio. No tiene permiso de escritura, así que en la
práctica ni siquiera podría.

---

## 6. Cómo se dicta cada clase

Tres bloques, siempre en el mismo orden:

1. **Teoría** — conceptos y analogías. Sin código en pantalla. No se entrega nada.
2. **Demo guiado** — yo conduzco, usted replica. Es `demo.ipynb`. Se publica con el andamiaje ya
   escrito: lo que usted escribe son las celdas de acción, no el código de arriba.
3. **Reto** — lo hace solo, sobre datos que no vio en el demo pero con la misma técnica. Es `reto.md`
   y `reto.ipynb`. **Es lo que se entrega.**

Las soluciones de los retos no se publican en este repositorio. Se resuelven en voz alta en clase.

---

## 7. Sobre el idioma

Todo el material está en español. La terminología técnica, los nombres de librerías y las funciones se
quedan en inglés a propósito (`groupby`, `dropna`, `DataFrame`, `outlier`, `overfitting`), porque así
los va a encontrar en la documentación y en los mensajes de error. La regla es simple: si lo va a
teclear o lo va a ver en un error, está en inglés; si lo va a leer para entender, está en español.
