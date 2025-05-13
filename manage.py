#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def reset_database():
    """Remove e recria completamente o banco de dados"""
    print("\n" + "="*50)
    print("🔄 INICIANDO RESET DO BANCO DE DADOS")
    print("="*50)

    try:
        # 1. Remove o arquivo do banco de dados se existir
        db_file = 'db.sqlite3'
        if os.path.exists(db_file):
            print(f"🗑️  Removendo banco: {db_file}")
            os.remove(db_file)
            print("✅ Banco removido com sucesso!")
        else:
            print(f"ℹ️  Arquivo {db_file} não encontrado - criando novo")

        # 2. Limpa migrações (opcional, apenas as que não são __init__.py)
        migrations_dir = os.path.join('instruments', 'migrations')
        if os.path.exists(migrations_dir):
            for f in os.listdir(migrations_dir):
                if f not in ['__init__.py', '__pycache__']:
                    os.remove(os.path.join(migrations_dir, f))

        # 3. Recria o banco
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])

        print("\n🎉 Banco de dados resetado com sucesso!\n")

    except Exception as e:
        print(f"\n❌ ERRO ao resetar banco: {str(e)}\n")
        sys.exit(1)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_api.settings')

    # Roda reset do banco só no comando runserver
    if 'runserver' in sys.argv:
        reset_database()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
