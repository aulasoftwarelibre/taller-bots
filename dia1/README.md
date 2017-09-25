# LEEME

## Instalar entorno

1. Es necesario tener instalado python2.7 y virtualenv. Python ya viene con las distribuciones de Linux 
pero virtualenv es posible que no. Formas de instalar virtualenv:
    ```sh
    # Debian/Ubuntu/Otras basadas en Debian
    sudo apt-get install virtualenv
    # RedHat/Fedora/Otras basadas en RedHat
    sudo yum install python-virtualenv
    # Otras opciones
    sudo easy_install virtualenv
    sudo pip install virtualenv
    ```

1. Ejecutar:

    ```sh
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
1. Copiar el archivo config.py.dist en config.py
    ```sh
    cp config.py.dist config.py
    ```

1. Editar el archivo config.py y configurar con tu propio token

1. Ejecutar cualquiera de los 3 programas


* echo.py: Repite todo lo que se le envía
* guest_number.py: Adivina un número del 1 al 100
* newton.py: Bot que realiza cálculos matemáticos a través de la API de [Newton](https://newton.now.sh/).
