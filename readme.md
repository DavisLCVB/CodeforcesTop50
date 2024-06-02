# Asignación de Web Scraping
#### Módulo Web Scraping - Especialización en Estadística y ciencia de datos - GEM
#### Alumno: Davis Leonardo Cartagena Valera Brush
---
## Descripción
El presente archivo acompaña al script correspondiente a la asignación dada por el docente.

El script de `Python` obtiene la información de la página [Codeforces](https://codeforces.com),
que es una página dedicada a la programación competitiva. Los datos se obtienen específicamente
del apartado de **ratings** que corresponde al top de usuarios con más puntos obtenidos
producto de las competiciones.

Se obtiene los nombres de usuarios de los primeros 50 usuarios y se procede a obtener información
del perfil de cada uno de ellos, específicamente:
- Nombre de usuario
- Rango
- Puntaje
- Foto de perfil
- Información adicional

Se guarda toda la información en una tabla de excel y se descargan las fotos de perfil de cada uno.

## Ejecución
La carpeta incluye un archivo llamado **requirements.txt** con las librerías necesarias. Este
puede ser instalado de la siguiente manera con pip:
```pwsh
pip install -r requirements.txt
```
Seguidamente la ejecución del archivo **main.py**. La opcion `--headless` viene descomentada