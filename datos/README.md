# datos/

Todos los CSV del curso, en un solo lugar.

Los notebooks los leen con una ruta relativa desde su carpeta de clase:

```python
import pandas as pd
df = pd.read_csv("../datos/HISTORICO_CONSUMO.csv")
```

Es una sola carpeta y no una por clase porque varios datasets se usan en más de una sesión
(`HISTORICO_CONSUMO.csv` aparece en las clases 1, 4, 5 y 14). Una sola copia significa una sola ruta
que aprender y ningún riesgo de que dos copias del mismo archivo terminen distintas.

Se llena a medida que avanza el semestre: cada clase trae sus datos cuando se publica.

`HISTORICO_CONSUMO.csv` ya está desde el primer día porque lo usa `verificacion.ipynb`, el notebook
que confirma que su entorno quedó bien montado.

**No edite estos archivos.** Si un ejercicio produce un CSV nuevo, guárdelo en la carpeta de su
proyecto, no aquí.
