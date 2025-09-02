# Kata TDD: Simulador del Juego Dudo Chileno


## Integrantes
- Luis Martinez Neira
- Daniel Tamaro Sierra
- Gabriela Zambrano Novoa

## Instalación

1. Clona el repositorio
```
https://github.com/gzambrano2022/TDD_20.git
```

2. Asegurate de tener Python 3.13, pues el proyecto fue desarrollado en esa versión.

3. Crea un entorno virtual
```
python -m venv venv
venv\Scripts\activate
```

4. Instala las dependencias
```
pip install pytest
```

## Ejecución

### Ejecución de pruebas y detalles de los tests

Para ejecutar todas las pruebas unitarias.
```
pytest
o
python3 -m pytest
```

Para saber el detalle de la cobertura de los tests
```
pytest --cov=src --cov-report=term-missing
o
python3 -m pytest --cov=src --cov-report=term-missing
```

### Ejecutar el juego

Script para mostrar la funcionalidad de todos los módulos integrados.
```
python partida_simple.py
```





