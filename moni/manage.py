#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Establece la configuración predeterminada de Django para el proyecto 'moni'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moni.settings')
    
    try:
        # Intenta importar la función de ejecución de comandos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no está instalado o no se puede importar, lanza un error con un mensaje explicativo
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Ejecuta el comando de línea de comandos de Django con los argumentos proporcionados
    execute_from_command_line(sys.argv)

# Si este script se está ejecutando como el programa principal, llama a la función main()
if __name__ == '__main__':
    main()