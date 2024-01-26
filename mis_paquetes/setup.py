# mi_paquete/setup.py

from setuptools import setup, find_packages

setup(
    name='image_processing',
    version='0.1',
    packages=find_packages(),
    description='Un módulo simple de procesamiento de imágenes con OpenCV',
    long_description=open('README.md').read(),
    install_requires=[
        'opencv-python',  # Asegúrate de incluir todas las dependencias necesarias
    ],
    include_package_data=True,
    author='Alfredo Maussa',
    author_email='tu_email@example.com',
    url='URL de tu proyecto, si existe',
)
