# Clase 9 · Visualización interactiva: Plotly y Streamlit

De la figura estática al dashboard: gráficos interactivos con plotly y una app que se filtra y se
recalcula sola, con streamlit.

## Qué hay aquí

| Archivo | Para qué |
|---------|----------|
| `slides.html` | Diapositivas de la clase |
| `demo.ipynb` | El demo guiado de plotly. Trae el código ya escrito |
| `streamlit_demo.py` | La app del demo: el dashboard que arma el profesor en clase |
| `reto.md` | La consigna del reto: qué se pide y con qué criterios se revisa |
| `reto.ipynb` | El cuaderno donde se resuelve la primera parte del reto |
| `streamlit_app_starter.py` | El punto de partida de la app del reto, con las secciones marcadas para completar |

## Datos

| Archivo | Dónde se usa |
|---------|--------------|
| [`../datos/calidad_aire_risaralda.csv`](../datos/calidad_aire_risaralda.csv) | Demo, y valor de arranque de la app del reto |
| [`../datos/educacion_estadisticas.csv`](../datos/educacion_estadisticas.csv) | Reto, primera parte |

**La app del reto va sobre el dataset de su equipo.** El archivo arranca apuntando al del demo; el
primer paso es cambiarlo por el suyo.

## Cómo se corren las apps

Con el entorno activo, desde esta carpeta:

```bash
streamlit run streamlit_demo.py
```

Se detiene con `Ctrl+C` en la terminal; cerrar la pestaña del navegador no la apaga. Si el puerto
está ocupado, agregue `--server.port 8502`.

## Cómo se usa

- **El demo se recorre en clase.** El código ya está escrito: se ejecuta, se lee y se responden las
  preguntas de interpretación.
- **El reto se hace después**, solo, con el profesor circulando. Aquí sí se escribe. Lo que empieza
  en esta clase es el entregable del Momento 2.
- Trabaje sobre una copia para que `git pull` no le reclame.

## Antes de empezar

- El entorno activo, con `streamlit` y `plotly` instalados ([`../INSTALACION.md`](../INSTALACION.md)).
- El demo recorrido antes de abrir el reto.
- El dataset del equipo limpio y a la mano.
