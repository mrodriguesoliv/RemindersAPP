#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Adicionando o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def initializedebugger():
    try:
        import debugpy
        debugpy.listen(("0.0.0.0", 4000))
    except Exception as except_:
        sys.stdout.write("Error starting debugger: %s\n" % except_)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlanAI.settings')  # Aqui se refere ao settings.py na pasta AlanAI
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    initializedebugger()

if __name__ == '__main__':
    main()
