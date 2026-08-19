# Instalación y puesta en marcha del entorno

Curso Analítica de Datos (709749) · Universidad Cooperativa de Colombia · Semestre 2026-2.

Este es el primer documento del curso. Se hace **una sola vez**, idealmente **antes de la clase 2**.
Toma entre 30 y 60 minutos la primera vez, y buena parte de ese tiempo es esperar descargas.

**No hace falta saber programar ni haber abierto una terminal nunca.** Cada paso dice qué escribir,
qué debería pasar y cómo saber que salió bien.

Si algo falla, primero mire la [sección 10, Problemas frecuentes](#10-problemas-frecuentes). Si aun así
no sale, **lleve el error a clase**: se resuelve en los primeros minutos, y no se pierde nada por
llegar con el entorno a medias.

---

## Índice

1. [Qué vamos a instalar y por qué](#1-qué-vamos-a-instalar-y-por-qué)
2. [Abrir una terminal](#2-abrir-una-terminal)
3. [Instalar Python](#3-instalar-python)
4. [Instalar Git](#4-instalar-git)
5. [Clonar el repositorio del curso](#5-clonar-el-repositorio-del-curso)
6. [Crear y activar el entorno virtual](#6-crear-y-activar-el-entorno-virtual)
7. [Instalar las librerías](#7-instalar-las-librerías)
8. [VSCode y los notebooks](#8-vscode-y-los-notebooks)
9. [Verificación final](#9-verificación-final)
10. [Problemas frecuentes](#10-problemas-frecuentes)
11. [La rutina de cada semana](#11-la-rutina-de-cada-semana)
12. [Opcional: un CLI de IA en su máquina](#12-opcional-un-cli-de-ia-en-su-máquina)

---

## 1. Qué vamos a instalar y por qué

Antes de teclear nada, el mapa. Son cinco piezas y cada una hace una cosa distinta.

> **Las cinco son obligatorias, y no hay una sexta.** Al final de este manual hay una sección 12
> sobre instalar un CLI de IA. Es **opcional**: ninguna clase, ningún reto y ninguna evaluación
> del curso lo necesitan. Si no la lee nunca, no le falta nada.

| Pieza | Qué es | Por qué la necesitamos |
|-------|--------|------------------------|
| **Python** | El lenguaje de programación. Es un programa que lee sus instrucciones y las ejecuta | Todo el análisis del semestre se escribe en Python |
| **Git** | Un programa que descarga y sincroniza carpetas de código | Es el canal por el que baja el material de cada clase y por el que entrega su proyecto |
| **Entorno virtual** | Una carpeta con las librerías de *este* curso, separadas del resto del computador | Evita que instalar algo para la universidad le rompa otra cosa que ya tenía |
| **Librerías** | Código que otras personas ya escribieron: pandas, matplotlib, scikit-learn... | Nadie escribe un análisis desde cero. Son las herramientas del oficio |
| **VSCode + extensiones** | El editor donde se escribe y se ejecuta el código | Es lo que se usa en clase. Con las extensiones Python y Jupyter, ejecuta notebooks |

Cómo encajan: **Git** trae la carpeta del curso. Dentro de esa carpeta, **Python** crea un **entorno
virtual**. Dentro del entorno virtual se instalan las **librerías**. Y **VSCode** abre la carpeta y
ejecuta el código usando ese entorno.

```
carpeta del curso  (la trae Git)
  .venv/           el entorno virtual  (lo crea Python)
    pandas, numpy, matplotlib, ...     (las instala pip)
  clase01/  clase02/  ...  datos/      el material
```

Un detalle que ahorra confusión más adelante: **el entorno virtual no se comparte y no se sube a
ningún lado.** Es suyo, vive en su computador y se puede borrar y volver a crear en cinco minutos.
Lo que se comparte es la lista de librerías, que es el archivo `requirements.txt`.

---

## 2. Abrir una terminal

La terminal es una ventana donde se escriben comandos en vez de hacer clic. Se ve intimidante y no
lo es: usted escribe una línea, presiona `Enter`, y el computador responde.

**Windows.** Presione la tecla `Windows`, escriba `PowerShell` y abra **Windows PowerShell**.
Use siempre PowerShell en este manual, no el "Símbolo del sistema" (CMD), salvo donde se diga.

**macOS.** Presione `Command + Espacio`, escriba `Terminal` y presione `Enter`.

Para comprobar que la entiende, escriba esto y presione `Enter`:

```
cd
```

No pasa nada visible. Bien: eso significa que el comando funcionó. La terminal solo habla cuando
tiene algo que decir, casi siempre un error.

Dos comandos que va a usar todo el semestre:

| Comando | Qué hace |
|---------|----------|
| `cd nombre-de-carpeta` | Entrar a una carpeta ("change directory") |
| `cd ..` | Salir a la carpeta de arriba |

> **Al copiar comandos de este manual, no copie el símbolo del sistema** (`$`, `>` o `PS C:\>`) si
> lo ve en otros tutoriales. Aquí los bloques de código no lo traen: se copian tal cual.

---

## 3. Instalar Python

### 3.1 Qué versión

El curso pide **Python 3.12 o superior**. La recomendación concreta es **Python 3.12**, que es la
versión con la que se probó y se instaló este entorno completo sin un solo conflicto.

Si tiene 3.13, sirve igual. Si tiene 3.11 o menos, actualice: dos de las librerías del curso
(`numpy` y `scipy`, en las versiones que el material necesita) ya no se publican para esas
versiones, y `pip` le va a instalar unas más viejas sin avisarle.

#### Por qué el `requirements.txt` tiene versiones mínimas

Ábralo y va a ver que cuatro líneas llevan `>=` con un número: `pandas`, `numpy`, `scipy` y
`scikit-learn`. Las demás van sueltas.

La razón es concreta. Esas cuatro son las que **producen los números** de los cuadernos: un
promedio, un intervalo de confianza, el puntaje de un modelo. Sus versiones nuevas cambian de vez
en cuando algún detalle de cálculo, y ese detalle mueve el resultado en la tercera cifra. En el
curso eso no es cosmético: **el verificador de los retos compara una huella de su resultado contra
la esperada**, y una huella distinta es un rechazo, aunque su código esté perfecto.

Los números del material están verificados con estas versiones:

| Librería | Versión verificada | Piso en `requirements.txt` |
|----------|--------------------|----------------------------|
| pandas | 3.0.5 | `>=3.0.5` |
| numpy | 2.5.2 | `>=2.5.2` |
| scipy | 1.18.0 | `>=1.18.0` |
| scikit-learn | 1.9.0 | `>=1.9.0` |

**Qué pasa si instala una más vieja.** `pandas` 2 trata el texto de otra manera y varias celdas de
limpieza fallan directamente; `scikit-learn` anterior a 1.9 entrena el mismo árbol y devuelve un
puntaje distinto en la tercera cifra, así que el verificador de la clase 14 le va a decir que está
mal cuando no lo está. Si el verificador rechaza algo que usted revisó y está correcto, **lo primero
que hay que mirar son las versiones**, con `pip list`.

**Es un piso, no un clavo.** `>=` permite instalar versiones más nuevas: si el año que viene sale
`pandas` 3.1, se instala sin problema. Lo que no se permite es quedarse atrás.

**Y por qué solo cuatro.** `matplotlib`, `seaborn`, `plotly` y `streamlit` dibujan; `ipykernel` y
`jupyterlab` son el entorno. Ninguna cambia un número, así que fijarles versión solo agregaría
conflictos de instalación a cambio de nada.

### 3.2 Ver si ya lo tiene

En la terminal:

**Windows**

```
python --version
```

**macOS**

```
python3 --version
```

**Qué debería pasar:** imprime algo como `Python 3.12.5`. Si el número es 3.12 o mayor, salte a la
sección 4.

**Si dice que el comando no existe**, o si en Windows se abre la tienda de Microsoft, todavía no lo
tiene instalado. Siga abajo.

### 3.3 Instalar en Windows

1. Vaya a https://www.python.org/downloads/ y descargue el instalador de Windows.
2. Ejecute el archivo descargado.
3. **En la primera pantalla, ANTES de dar clic en "Install Now", marque la casilla
   "Add python.exe to PATH"**, abajo del todo.
4. Dé clic en **Install Now** y espere.
5. Cierre la terminal que tuviera abierta y **abra una nueva**. Esto es obligatorio: la terminal solo
   se entera de los programas nuevos al arrancar.

> **La trampa clásica.** Esa casilla del paso 3 es la causa número uno de "instalé Python y la
> terminal dice que no existe". `PATH` es la lista de sitios donde el sistema busca programas; si
> Python no entra en esa lista, el computador lo tiene instalado pero no sabe encontrarlo.
> Si ya instaló sin marcarla: vuelva a ejecutar el instalador, elija **Modify**, y en la pantalla
> siguiente active **"Add Python to environment variables"**.

**Verificar:**

```
python --version
```

Debe imprimir `Python 3.12.x` o similar.

### 3.4 Instalar en macOS

macOS trae un Python viejo de fábrica que no sirve para el curso. Hay que instalar uno propio.

1. Vaya a https://www.python.org/downloads/ y descargue el instalador de macOS (`.pkg`).
2. Ábralo y siga el asistente aceptando los valores por defecto.
3. Al terminar, se abre una carpeta en el Finder. Puede cerrarla.
4. Cierre la terminal y abra una nueva.

**Verificar:**

```
python3 --version
```

Debe imprimir `Python 3.12.x` o similar.

> **En macOS el comando es `python3`, no `python`.** Escribir `python` a secas o falla, o le abre el
> Python viejo del sistema. En Windows es al revés: el comando es `python`. En este manual los
> bloques vienen separados por sistema para no tener que recordarlo.

---

## 4. Instalar Git

Git es el programa que descarga el material del curso y mantiene su copia al día.

> **Git no se enseña ni se evalúa en este curso.** Es la vía de entrega y nada más: nadie va a
> revisar la calidad de sus commits. Con `clone`, `add`, `commit`, `push` y `pull` le alcanza para
> el semestre. Si no lo ha visto nunca, la sección 4 del `README.md` tiene tres recursos para
> ponerse al día en una tarde.

**Ver si ya lo tiene**, en Windows y en macOS por igual:

```
git --version
```

Si imprime algo como `git version 2.43.0`, ya está. Si no:

- **Windows:** descargue e instale desde https://git-scm.com/download/win . Acepte todos los valores
  por defecto del asistente. Cierre la terminal y abra una nueva.
- **macOS:** escriba `git --version` y el sistema mismo le ofrece instalar las Command Line Tools.
  Acepte y espere. Si no aparece el diálogo, instale desde https://git-scm.com/download/mac .

---

## 5. Clonar el repositorio del curso

**Clonar** es descargar una copia de la carpeta del curso, conectada al original. Se hace **una sola
vez en el semestre**. Después, cada semana se actualiza con `git pull` (sección 11).

### 5.1 Dónde conviene clonarlo

En una carpeta suya, con ruta corta y **sin espacios ni tildes en el nombre**. La sugerencia:

- **Windows:** `C:\Users\SU_USUARIO\Documents`
- **macOS:** `~/Documents`

Evite el Escritorio si está sincronizado con OneDrive o iCloud: la sincronización en segundo plano
puede corromper el entorno virtual.

Ubíquese ahí:

**Windows**

```
cd $HOME\Documents
```

**macOS**

```
cd ~/Documents
```

### 5.2 Clonar

```
git clone https://github.com/juliangarzon/analitica-datos-estudiantes.git analitica-datos
```

> **Copie el comando tal cual, sin cambiar nada.** El repositorio en GitHub se llama
> `analitica-datos-estudiantes`, pero la carpeta que se crea en su computador se llama
> `analitica-datos`: eso lo hace la última palabra del comando, y es a propósito. La misma URL queda
> publicada en el aula virtual.

**Qué debería pasar:** varias líneas tipo `Cloning into 'analitica-datos'...`, `Receiving objects:
100%`. Tarda menos de un minuto.

**Cómo saber que salió bien:** entre a la carpeta y liste su contenido.

**Windows**

```
cd analitica-datos
dir
```

**macOS**

```
cd analitica-datos
ls
```

Debe ver `clase01`, `clase02`, ..., `datos`, `requirements.txt`, `README.md`, `INSTALACION.md`,
`verificacion.ipynb`.

**A partir de aquí, todos los comandos se ejecutan desde dentro de esta carpeta.** Si cierra la
terminal y vuelve mañana, lo primero es volver a entrar con `cd`.

---

## 6. Crear y activar el entorno virtual

### 6.1 Qué es y por qué

Un **entorno virtual** es una carpeta que contiene una copia aislada de Python con sus propias
librerías. Todo lo que instale mientras está activo se guarda ahí adentro y en ningún otro lado.

Por qué importa: sin él, cada `pip install` se le mete al Python del sistema, que es el mismo que
usan todos sus proyectos y, en algunos casos, el propio sistema operativo. Dos proyectos que
necesiten versiones distintas de la misma librería entran en conflicto, y arreglarlo es
desagradable. Con entorno virtual, el peor escenario es borrar la carpeta `.venv` y volver a
empezar, que toma cinco minutos.

La regla mental: **una carpeta de proyecto, un entorno virtual.**

### 6.2 Crearlo

Desde dentro de `analitica-datos`:

**Windows**

```
python -m venv .venv
```

**macOS**

```
python3 -m venv .venv
```

**Qué debería pasar:** nada en pantalla, y tarda unos segundos. Aparece una carpeta nueva llamada
`.venv`. El punto al principio del nombre la hace oculta en el explorador de archivos; es normal.
Está en el `.gitignore` del repositorio, así que Git la ignora a propósito.

**Se crea una sola vez.** No repita este comando cada semana.

### 6.3 Activarlo

Activar es decirle a la terminal: "de aquí en adelante, cuando diga `python` o `pip`, use los de
esta carpeta".

**Windows (PowerShell)**

```
.venv\Scripts\Activate.ps1
```

**Windows (CMD, solo si no usa PowerShell)**

```
.venv\Scripts\activate.bat
```

**macOS**

```
source .venv/bin/activate
```

**Cómo saber que salió bien:** al principio de la línea de la terminal aparece `(.venv)`.

```
(.venv) PS C:\Users\ana\Documents\analitica-datos>
(.venv) ana@MacBook analitica-datos %
```

Si no ve `(.venv)`, el entorno **no** está activo, y todo lo que haga después va al sitio
equivocado.

> **La trampa número uno del semestre.** La activación dura lo que dure esa ventana de terminal. Al
> cerrarla, se pierde. Mañana, al abrir una terminal nueva, hay que activar otra vez. Este es el
> origen del 90% de los "ayer me funcionaba y hoy no": no es que se haya desinstalado nada, es que
> el entorno no está activo. **Antes de escribir cualquier comando, mire si dice `(.venv)`.**

Para desactivarlo, cuando termine de trabajar (opcional, cerrar la terminal hace lo mismo):

```
deactivate
```

**Si en Windows aparece un error rojo que menciona "ejecución de scripts está deshabilitada"**, vaya
a la sección 10, problema 3. Es un ajuste de seguridad de Windows y se arregla con un comando.

---

## 7. Instalar las librerías

### 7.1 Qué es pip y qué es requirements.txt

**pip** es el instalador de librerías de Python. Va a internet, descarga lo que le pida y lo deja
dentro del entorno virtual activo.

**`requirements.txt`** es un archivo de texto con la lista de librerías del curso, una por línea.
Existe para que nadie tenga que instalarlas una por una ni adivinar cuáles son: la lista es la
misma para todo el salón. Ábralo si quiere, es legible.

Cuatro líneas llevan un `>=` con un número: es la versión mínima verificada, y está explicada en la
sección 3.1. En corto: son las librerías que producen los números que el verificador de los retos
comprueba, y con versiones más viejas el verificador rechaza respuestas correctas.

### 7.2 Instalar

**Con `(.venv)` visible en la terminal**, y desde la carpeta `analitica-datos`:

```
pip install -r requirements.txt
```

**Qué debería pasar:** decenas de líneas `Collecting ...`, `Downloading ...`, barras de progreso, y
al final una línea larga que empieza con `Successfully installed`. Descarga unos cuantos cientos de
megabytes.

**Cuánto tarda:** entre 2 y 10 minutos según su conexión. Es normal que parezca colgado en algún
paquete grande; espere.

Puede aparecer un aviso amarillo diciendo que hay una versión nueva de pip. Es informativo, no un
error. Ignórelo.

### 7.3 Verificar

```
pip list
```

Imprime la lista de lo instalado. Deben estar `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`,
`streamlit`, `scipy`, `scikit-learn`, `ipykernel` y `jupyterlab`, entre muchas dependencias que
esas librerías arrastran.

Mire de paso los números de `pandas`, `numpy`, `scipy` y `scikit-learn`: deben ser iguales o
mayores a los de la tabla de la sección 3.1. Si alguno salió menor, `pip` no encontró la versión
buena para su Python, y casi siempre es porque su Python es anterior a 3.12.

Una comprobación más directa:

```
python -c "import pandas, numpy, matplotlib, seaborn, plotly, streamlit, sklearn, scipy; print('Entorno listo')"
```

Si imprime `Entorno listo`, esta parte terminó.

---

## 8. VSCode y los notebooks

### 8.1 Instalar VSCode

Visual Studio Code es el editor que se usa en clase. Es gratis.

1. Descargue de https://code.visualstudio.com/ e instale.
2. En Windows, si el instalador ofrece "Add to PATH" o "Agregar acción Abrir con Code", acepte.

### 8.2 Instalar las dos extensiones

Las extensiones le agregan capacidades a VSCode. Necesitamos dos, ambas publicadas por **Microsoft**
(hay imitaciones con nombres parecidos; fíjese en el editor).

1. Abra VSCode.
2. Clic en el icono de **Extensiones** en la barra izquierda (cuatro cuadritos), o `Ctrl+Shift+X`
   (`Cmd+Shift+X` en macOS).
3. Busque **Python** (de Microsoft) e instale.
4. Busque **Jupyter** (de Microsoft) e instale.

La extensión Python le enseña a VSCode qué es Python. La extensión Jupyter le permite abrir y
ejecutar archivos `.ipynb`, que son los notebooks del curso.

### 8.3 Abrir la carpeta del curso

**Menú `File` > `Open Folder...`** y elija la carpeta `analitica-datos` completa.

No abra archivos sueltos: abra **la carpeta**. VSCode necesita ver la carpeta entera para encontrar
el entorno virtual y para que las rutas relativas a `datos/` funcionen.

Si aparece un cuadro preguntando si confía en los autores de la carpeta ("Do you trust the authors"),
responda que sí.

### 8.4 Seleccionar el intérprete del entorno virtual

**Este es el paso donde más gente se atasca**, porque VSCode escoge un Python por su cuenta y casi
nunca es el correcto. El síntoma es un `ModuleNotFoundError` en un computador donde las librerías
sí están instaladas.

El **intérprete** es el Python que VSCode va a usar. Hay que apuntarlo al del `.venv`.

1. Presione `Ctrl+Shift+P` (`Cmd+Shift+P` en macOS). Se abre una barra de búsqueda de comandos.
2. Escriba `Python: Select Interpreter` y presione `Enter`.
3. En la lista, elija el que dice **`.venv`** y **`Recommended`**. La ruta se ve así:
   - Windows: `.\.venv\Scripts\python.exe`
   - macOS: `./.venv/bin/python`
4. Si no aparece en la lista: elija `Enter interpreter path...` > `Find...` y navegue a mano hasta
   ese archivo.

Una vez seleccionado, VSCode lo recuerda para esta carpeta. No hay que repetirlo cada día.

### 8.5 Qué es un notebook y cómo se ejecuta

Un **notebook** (`.ipynb`) es un documento que mezcla texto y código en bloques llamados **celdas**.
Es el formato de trabajo del analista de datos: se ejecuta un pedazo, se mira el resultado, se
ajusta, se sigue. No hay que ejecutar el programa entero cada vez.

Hay dos tipos de celda:

- **Celda de texto** (markdown): explicaciones. No hace nada al ejecutarse, solo se formatea.
- **Celda de código**: Python. Al ejecutarla, corre y muestra su resultado justo debajo.

**Cómo se ejecuta una celda:** clic dentro de ella y `Shift + Enter`. Eso la ejecuta y salta a la
siguiente. También hay un botón de "play" a la izquierda de cada celda.

**El número entre corchetes**, a la izquierda de cada celda de código:

| Se ve | Significa |
|-------|-----------|
| `[ ]` | Nunca se ha ejecutado en esta sesión |
| `[*]` | Se está ejecutando ahora mismo. Espere |
| `[3]` | Terminó, y fue la tercera celda que se ejecutó en esta sesión |

Ese número es el **orden real de ejecución**, no el orden en que aparecen en pantalla. Importa: si
ejecuta la celda 5 antes que la 3, el notebook puede fallar por una variable que todavía no existe.
**Regla: ejecute siempre de arriba hacia abajo.**

**El kernel** es el proceso de Python que está corriendo el notebook por detrás. Guarda en memoria
todas las variables que usted ha creado. Se ve arriba a la derecha: debe decir `.venv`. Si dice otra
cosa, haga clic ahí, elija **Select Another Kernel** > **Python Environments** y escoja el `.venv`.

Si algo se enreda sin explicación, **Restart** en la barra superior reinicia el kernel: borra todas
las variables y deja el notebook como recién abierto. Después de reiniciar hay que volver a ejecutar
desde la primera celda.

---

## 9. Verificación final

En la raíz del repositorio hay un archivo llamado **`verificacion.ipynb`**. Es la prueba de que todo
quedó bien: importa las ocho librerías del curso, lee un CSV real del repositorio y pinta un
gráfico. Si eso corre, está listo para la clase 2.

1. En VSCode, con la carpeta `analitica-datos` abierta, haga clic en `verificacion.ipynb` en el
   panel izquierdo.
2. Confirme que arriba a la derecha el kernel dice `.venv` (sección 8.4).
3. Ejecute las celdas de arriba hacia abajo con `Shift + Enter`.

**Qué debería pasar:**

- La primera celda imprime su versión de Python y una ruta que **contiene `.venv`**.
- La segunda imprime las versiones de las ocho librerías.
- La tercera dice `Filas: 21816` y `Columnas: 12`, y lista los nombres de las columnas.
- La cuarta muestra una tabla con las primeras cinco filas.
- La quinta pinta un gráfico de barras horizontal.
- La última imprime `Entorno listo`.

Si llegó al final sin ningún recuadro rojo de error, terminó. Cierre el notebook **sin guardar**.

Si prefiere no usar VSCode, el mismo notebook se puede abrir en el navegador. Con `(.venv)` activo:

```
jupyter lab
```

Se abre solo. Para cerrarlo, `Ctrl+C` en la terminal.

### 9.1 Cada notebook de clase se verifica solo

`verificacion.ipynb` se corre una vez, al montar el entorno. Pero el entorno se desconfigura solo:
una terminal nueva sin activar, VSCode que cambia de intérprete después de una actualización, un
`git pull` que no se hizo.

Por eso **todos los `demo.ipynb` y `reto.ipynb` del curso empiezan igual**:

1. Una celda de texto, **Antes de empezar**, con el tema de la clase, la rutina y una tabla de los
   tres errores más frecuentes, cada uno apuntando a la sección de este manual que lo resuelve.
2. Una celda de código de **verificación**: importa las librerías que esa clase necesita, imprime la
   ruta del intérprete y confirma que el CSV de la clase está donde debe.

Ejecútela siempre primero. Debe imprimir dos líneas:

```
Intérprete: .../analitica-datos/.venv/bin/python
Datos: encontrados en ../datos/HISTORICO_CONSUMO.csv
```

**Si esa celda falla o imprime un `AVISO`, deténgase ahí.** No siga a la siguiente: el problema es de
entorno, no del contenido de la clase, y el resto del notebook va a fallar en cadena. La celda dice
qué hacer, y esa misma tabla de la celda de arriba dice en qué sección de este manual está el detalle.

Esa celda es andamiaje, no materia. No se entrega, no se califica y no hay que entenderla para
aprobar: está ahí para que un problema de instalación no le cueste los primeros veinte minutos de
clase.

---

## 10. Problemas frecuentes

### Problema 1 — `python: command not found` o `'python' no se reconoce...`

**Síntoma.** La terminal dice que no conoce el comando. En Windows, a veces se abre la Microsoft
Store.

**Causa.** O Python no está instalado, o está instalado pero no en el `PATH`, o abrió la terminal
antes de instalarlo.

**Solución.**

1. Cierre **todas** las terminales y abra una nueva. Muchas veces es solo eso.
2. En macOS, pruebe `python3` en vez de `python`. En macOS el comando es `python3`.
3. En Windows, reinstale desde https://www.python.org/downloads/ marcando **"Add python.exe to
   PATH"**, o ejecute el instalador otra vez, elija **Modify** y active **"Add Python to environment
   variables"**.

### Problema 2 — `pip: command not found`

**Síntoma.** `pip install ...` dice que el comando no existe.

**Causa.** Casi siempre el entorno virtual no está activo.

**Solución.**

1. Mire si la línea de la terminal empieza con `(.venv)`. Si no, actívelo (sección 6.3).
2. Si aun activo falla, use la forma larga, que siempre funciona:
   - Windows: `python -m pip install -r requirements.txt`
   - macOS: `python3 -m pip install -r requirements.txt`

### Problema 3 — Windows: "la ejecución de scripts está deshabilitada en este sistema"

**Síntoma.** Al activar el entorno en PowerShell sale un texto rojo largo que menciona
`UnauthorizedAccess` o `execution policy`.

**Causa.** Windows bloquea por defecto la ejecución de scripts de PowerShell. El activador del
entorno virtual es uno de esos scripts.

**Solución.** En la misma ventana de PowerShell:

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Confirme con `S` o `Y`. Es un cambio limitado a su usuario y solo permite ejecutar scripts locales;
no baja la seguridad del equipo. Luego vuelva a activar:

```
.venv\Scripts\Activate.ps1
```

**Alternativa sin cambiar nada:** use CMD en vez de PowerShell y active con
`.venv\Scripts\activate.bat`.

### Problema 4 — VSCode no encuentra el kernel, o dice "Select Kernel" y la lista está vacía

**Síntoma.** Al abrir un notebook no hay kernel, o el desplegable no muestra el `.venv`.

**Causa.** Falta la extensión Jupyter, falta `ipykernel` dentro del entorno, o VSCode no está viendo
la carpeta correcta.

**Solución, en este orden.**

1. Confirme que abrió **la carpeta** `analitica-datos` (`File > Open Folder`), no un archivo suelto.
2. Confirme que las extensiones **Python** y **Jupyter** de Microsoft están instaladas (sección 8.2).
3. Con `(.venv)` activo en la terminal: `pip install ipykernel`.
4. Recargue VSCode: `Ctrl+Shift+P` > `Developer: Reload Window`.
5. Seleccione el intérprete otra vez: `Ctrl+Shift+P` > `Python: Select Interpreter` > el que dice
   `.venv`.

### Problema 5 — `ModuleNotFoundError: No module named 'pandas'` aunque sí lo instalé

**Síntoma.** La instalación dijo `Successfully installed`, pero el notebook no encuentra la librería.

**Causa.** Se instaló en un Python y se está ejecutando con otro. Es el desencuentro clásico entre
el entorno virtual y el intérprete que VSCode escogió solo.

**Solución.**

1. Ejecute la celda de verificación con la que empieza el notebook (la primera de código, sección
   9.1): imprime `Intérprete:` seguido de la ruta del Python que está usando. **Si esa ruta no
   contiene `.venv`, ese es el problema**, y la celda misma se lo advierte con un `AVISO`. En
   `verificacion.ipynb`, la primera celda hace lo mismo.
2. Seleccione el intérprete correcto (sección 8.4) y **reinicie el kernel** (botón `Restart`).
3. Si la ruta sí contiene `.venv`, entonces la instalación se hizo sin el entorno activo. Actívelo
   (sección 6.3) y repita `pip install -r requirements.txt`.

### Problema 6 — `FileNotFoundError` al leer un CSV

**Síntoma.** `FileNotFoundError: [Errno 2] No such file or directory: 'datos/HISTORICO_CONSUMO.csv'`.

**Causa.** Las rutas de los notebooks son **relativas** a la carpeta donde está el notebook. Si movió
archivos de sitio, o abrió el notebook desde otra carpeta, la ruta deja de apuntar a donde debe.

**Solución.**

1. No mueva ni renombre carpetas del repositorio. `datos/` vive en la raíz y los notebooks de clase
   la alcanzan con `../datos/`.
2. Abra siempre la carpeta raíz `analitica-datos` en VSCode.
3. Si el CSV que busca no existe todavía, revise que hizo `git pull`: los datos de cada clase se
   publican junto con el material de esa clase.
4. La celda de verificación del notebook (sección 9.1) le dice exactamente qué archivo esperaba y
   dónde. Si imprime `FALTA el archivo ...`, el problema está antes de cualquier línea de análisis:
   arréglelo ahí y no siga bajando.

### Problema 7 — `git pull` falla porque edité un archivo del repositorio

**Síntoma.** Al hacer `git pull` sale algo como:

```
error: Your local changes to the following files would be overwritten by merge:
        clase04/demo.ipynb
Please commit your changes or stash them before you merge.
```

**Causa.** Usted modificó un archivo que el profesor también modificó. Git no sabe cuál de las dos
versiones conservar y se detiene. Resolver conflictos no es tema de este curso.

**Solución para salir del paso ahora**, descartando sus cambios en ese archivo:

```
git checkout -- clase04/demo.ipynb
git pull
```

Si quiere conservar su trabajo antes de descartarlo, primero cópielo con otro nombre.

**Convención del curso, que evita este problema por completo: trabaje siempre sobre una copia,
nunca sobre el archivo original.**

Al empezar la clase, duplique el notebook y edite el duplicado:

**Windows**

```
copy clase04\demo.ipynb clase04\demo_mio.ipynb
```

**macOS**

```
cp clase04/demo.ipynb clase04/demo_mio.ipynb
```

El archivo `demo.ipynb` queda intacto, `git pull` nunca reclama, y su trabajo vive en
`demo_mio.ipynb`. La misma regla aplica a `reto.ipynb` y a `verificacion.ipynb`.

> Los archivos de **su proyecto** no van en este repositorio en ningún caso: van en el repositorio
> de su equipo. Ver la sección 5 del `README.md`.

### Problema 8 — Se me dañó todo y no sé qué toqué

**Solución.** El entorno virtual es desechable. Bórrelo y vuelva a crearlo; no pierde nada porque
ahí no vive su trabajo.

**Windows**

```
deactivate
Remove-Item -Recurse -Force .venv
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**macOS**

```
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 11. La rutina de cada semana

La instalación fue una sola vez. Lo de cada clase son tres líneas:

**Windows**

```
cd $HOME\Documents\analitica-datos
git pull
.venv\Scripts\Activate.ps1
```

**macOS**

```
cd ~/Documents/analitica-datos
git pull
source .venv/bin/activate
```

Y después, abrir VSCode en esa carpeta.

Tres cosas para no olvidar:

1. **`git pull` antes de cada clase.** Si no, llega con el material de la semana pasada.
2. **Activar el entorno en cada terminal nueva.** Busque el `(.venv)`.
3. **Trabajar sobre copias, no sobre los archivos originales del repositorio.**
4. **Ejecutar primero la celda de verificación del notebook** (sección 9.1). Son dos segundos y le
   dice si el entorno está bien antes de que empiece la clase, no a mitad de camino.

---

## 12. Opcional: un CLI de IA en su máquina

> **Esta sección entera es opcional.** Es una **recomendación** del curso, no un requisito.
>
> - **Ninguna clase la necesita.** Los notebooks de todas las clases, incluida la 7, corren sin esto.
> - **Ningún reto la necesita.**
> - **No se evalúa.** No aparece en ninguna rúbrica, ni en el Momento 1, ni en el 2, ni en el 3.
> - No necesita tarjeta de crédito para el camino gratuito, y no la necesita en absoluto si decide
>   no hacer esta sección.
>
> Si su computador es prestado, si no tiene permisos de administrador, o si simplemente no le
> interesa: sáltela. No queda por fuera de nada.

### 12.1 Qué es y qué gana

Un **CLI de IA** es un programa de terminal que puede leer los archivos de su proyecto: su CSV, su
notebook, el error real que le dio pandas. A diferencia de un chat web, que solo ve lo que usted le
pegue, un CLI trabaja sobre su carpeta.

En la clase 7 usted escribe archivos `SKILL.md`: instrucciones reutilizables con un formato de salida
fijo. Esos archivos se escriben, se leen y se revisan sin ejecutar nada, y eso es lo que hace la
clase. Un CLI le permite además **ejecutarlos** y ver la salida real.

Es un buen cierre. No es indispensable.

### 12.2 Qué hace falta

**Node.js 18 o superior.** Es otro lenguaje de programación; los cuatro CLIs se distribuyen con su
gestor de paquetes, `npm`.

Para ver si ya lo tiene, en una terminal:

```
node --version
npm --version
```

Si ve dos números de versión y el primero es 18 o mayor, ya está. Si ve `command not found` o
`no se reconoce`, descárguelo de [nodejs.org](https://nodejs.org) y elija la versión **LTS**.

### 12.3 Cuál elegir

Los cuatro leen el mismo `SKILL.md`. **Lo que escriba es portable entre ellos:** está eligiendo
herramienta, no religión. Si mañana cambia, mueve la carpeta y sigue.

| Herramienta | Fabricante | Cómo se instala | Autenticación | Costo |
|-------------|-----------|-----------------|---------------|-------|
| **Gemini CLI** | Google | `npm install -g @google/gemini-cli` | OAuth con su cuenta Google | Tier gratuito. **La recomendación si no tiene preferencia** |
| **OpenCode** | Open source | `npm install -g opencode-ai` | Depende del proveedor que conecte | Gratuito si conecta un proveedor con tier gratuito |
| **Claude Code** | Anthropic | `npm install -g @anthropic-ai/claude-code` | Cuenta Claude o API key | Requiere plan de pago o crédito |
| **Codex CLI** | OpenAI | `npm install -g @openai/codex` | Cuenta ChatGPT o API key | Requiere plan de pago o crédito |

Los nombres de paquete cambian de vez en cuando. Si alguno da `404 Not Found`, búsquelo en la
documentación oficial de la herramienta y avise en el canal del curso para corregir esta tabla.

### 12.4 Instalar y autenticar

Todo esto va **en una terminal**, no en una celda de notebook. Son programas interactivos que se
quedan esperando lo que usted teclee, y Jupyter no sabe hacer eso: si los pega en una celda, la celda
se queda colgada para siempre y toca interrumpir el kernel.

Instale **una sola**, la que eligió:

```
npm install -g @google/gemini-cli
```

Verifique:

```
gemini --version
```

Y ábrala para autenticarse:

```
gemini
```

Se abre su navegador, inicia sesión con Google y listo. Las otras tres se abren igual, con su propio
nombre: `opencode`, `claude`, `codex`.

### 12.5 Probar que funciona

Dentro de la herramienta, escriba estos tres:

1. `Explica qué es la analítica de datos en una sola frase.`
2. `Escribe una función de pandas que calcule el porcentaje de nulos por columna de un DataFrame.`
3. `Resume en tres viñetas qué es un EDA y sus pasos principales.`

Mire el segundo con atención: lo que le devolvió es **código**. No es un resultado, es una instrucción
para que pandas calcule. Un LLM predice texto: **escribe** bien el código que hace la aritmética, y
**hace** mal la aritmética. Si un número no salió de una celda ejecutada, no es un número, es una
suposición.

### 12.6 Usar sus skills

Los `SKILL.md` que escribió van en una carpeta que depende de la herramienta. El archivo de adentro
es idéntico en las cuatro.

| Herramienta | Carpeta |
|-------------|---------|
| Gemini CLI | `.gemini/skills/<nombre-del-skill>/SKILL.md` |
| OpenCode | `.opencode/skills/<nombre-del-skill>/SKILL.md` |
| Claude Code | `.claude/skills/<nombre-del-skill>/SKILL.md` |
| Codex CLI | `.codex/skills/<nombre-del-skill>/SKILL.md` |

Si escribió sus skills en `.gemini/` y terminó usando otra herramienta, **renombre la carpeta**. Eso
es todo.

Después, abra la herramienta desde la carpeta donde está `.gemini/` y pídale algo así:

```
Usa el skill diccionario-de-datos sobre el archivo ../datos/HISTORICO_CONSUMO.csv
```

Y haga el ejercicio que vale la pena, que es el mismo del Bloque 2 de la clase 7:

1. Ponga la salida al lado de su `SKILL.md`.
2. Marque cada sección de la salida que **no** corresponde a lo que su formato prometía.
3. Marque cada regla que el modelo se saltó.
4. Cambie el archivo, no el prompt.
5. Vuelva a ejecutar.

### 12.7 Antes de instalar un skill de otra persona

La regla de seguridad del curso, que **sí** es materia evaluable de la clase 7 aunque la instalación
no lo sea. Un skill es un archivo de instrucciones que usted le entrega a un programa con permiso de
leer y escribir en su computador.

Las cinco banderas rojas:

1. Le pide al modelo leer `.env`, credenciales, llaves SSH o el historial del shell.
2. Instruye enviar contenido a una URL externa.
3. Pide tokens, contraseñas o llaves de API.
4. La descripción es vaga sobre lo que realmente hace.
5. El autor es desconocido, sin historial ni repositorio público.

Y el procedimiento: leer el `SKILL.md` **completo**, preguntarse si pide archivos sensibles,
preguntarse si manda datos a algún lado, y ante cualquier duda **no instalarlo**.

> Si el skill es demasiado largo para leerlo completo, es demasiado largo para confiar en él.

### 12.8 Problemas frecuentes de esta sección

| Problema | Qué pasó | Solución |
|----------|----------|----------|
| `command not found: npm` | No tiene Node.js | Instálelo desde nodejs.org, versión LTS, y cierre y abra la terminal |
| `EACCES: permission denied` | npm intenta escribir en una carpeta del sistema | **No use `sudo`.** Use `npx @google/gemini-cli` en lugar de instalar, o configure el prefijo de npm en su carpeta de usuario |
| `404 Not Found` al instalar | El nombre del paquete cambió | Búsquelo en la documentación oficial y avise en el canal del curso |
| El navegador no abre para el OAuth | Ventana emergente bloqueada | Pruebe en ventana de incógnito. Si persiste, copie la URL que aparece en la terminal y péguela a mano |
| "Invalid API key" con una key que se ve bien | La pegó con un espacio o un salto de línea al final | Vuelva a pegarla, entre comillas |
| La herramienta no ve la variable de entorno | La definió después de abrir la terminal | Cierre y abra la terminal. Jupyter tampoco ve variables exportadas después de arrancar el kernel |
| "Rate limit" o "quota exceeded" | Se agotó la cuota del tier gratuito | Espere. **Nunca es motivo para poner una tarjeta**: esta sección es opcional |
| La celda del notebook se queda colgada | Pegó un comando interactivo en Jupyter | Interrumpa el kernel. Esos comandos van en una terminal aparte |
| Escribió el skill y "no funciona" | Tres causas, por frecuencia | Ruta de carpeta equivocada; frontmatter mal formado (los tres guiones van en la **línea 1**); o descripción demasiado vaga para que la herramienta sepa cuándo dispararlo |
