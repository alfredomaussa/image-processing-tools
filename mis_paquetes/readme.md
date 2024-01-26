Estructura básica:

mi_paquete/
│
├── image_processing/
│   ├── __init__.py
│   └── core.py
│
└── setup.py



en la carpeta 'mi_paquete', para instalar ejecutas:
pip install -e .

verificas con pip list
pip show image_processing