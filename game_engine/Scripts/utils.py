#python -m pip install --upgrade pip
#python -m venv caminho...\nome da venv
#caminho da venv...\Scripts\activate
#caminho da venv...\Scripts\deactivate

import os

def show_pythonVersion(label="Versão do python: "):
    """
    Exibi versão do python
    
    Parâmetros:
        label (string) - rótulo
    
    Return:
        Versão do python
    """
    
    x = os.popen("python -V").read()
    print(label + x.replace("Python ", "").replace("\n", ""))

