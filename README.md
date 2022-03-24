# open-cv-congreso


### Instalación de dependencias ⚙️

1. Instalación de `pipenv`:
    ```bash
    pip install pipenv
    ```

2. Crea un entorno virutal con `pipenv`, utilizando Python 3.8:
    ```bash
    pipenv shell --python 3.8
    ```

3. Instalación de dependencias:
    ```bash
    pipenv install -r requirements.txt
    ```


### Uso 💻

Para extraer frames de una carpeta con videos, puedes tomar como referencia
el script `main.py`. Dicho script procesa cada video de una carpeta de entrada
extrae frames de los mismos.


### To Do

- [X] Agregar función para extraer frames de un video
- [X] Agregar función para iterar sobre videos en folder
- [ ] Agregar función para detectar + recortar rostros y generar un dataset
