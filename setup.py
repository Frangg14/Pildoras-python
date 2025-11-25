# setup.py hace que la carpeta calculos, por ejemplo, sea un paquete de Python, 
# distribuible e instalable, donde sea necesario.
from setuptools import setup

setup(
    name='paquetecalculos',
    version='1.0',
    description='Un paquete para realizar cálculos matemáticos básicos',
    author='FGG',
    packages=['4avanzado', '4avanzado.calculos']
)