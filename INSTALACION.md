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

---

## 1. Qué vamos a instalar y por qué

Antes de teclear nada, el mapa. Son cinco piezas y cada una hace una cosa distinta.

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

El curso pide **Python 3.10 o superior**. La recomendación concreta es **Python 3.12**, que es la
versión con la que se probó y se instaló este entorno completo sin un solo conflicto.

Si ya tiene 3.10, 3.11 o 3.13, sirve igual. Si tiene 3.9 o menos, actualice.

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

**Qué debería pasar:** imprime algo como `Python 3.12.5`. Si el número es 3.10 o mayor, salte a la
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
git clone URL_DEL_REPOSITORIO analitica-datos
```

> **`URL_DEL_REPOSITORIO` es un marcador, no un comando literal.** La URL real se anuncia en la
> clase 1 y queda publicada en el aula virtual. Reemplace el marcador completo por esa URL antes de
> presionar `Enter`.

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

1. Ejecute la primera celda de `verificacion.ipynb`: imprime la ruta del Python que está usando el
   notebook. **Si esa ruta no contiene `.venv`, ese es el problema.**
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
