#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line

def reset_database():
    """Remove e recria completamente o banco de dados"""
    print("\n" + "="*50)
    print("🔄 INICIANDO RESET DO BANCO DE DADOS")
    print("="*50)

    try:
        # 1. Remove o arquivo do banco de dados se existir
        db_file = 'db.sqlite3'
        if os.path.exists(db_file):
            print(f"🗑️  Removendo arquivo do banco de dados: {db_file}")
            os.remove(db_file)
            print("✅ Banco de dados removido com sucesso!")
        else:
            print(f"ℹ️  Arquivo {db_file} não encontrado - prosseguindo com criação")

        # 2. Remove as migrações existentes (opcional)
        migrations_dir = os.path.join('instruments', 'migrations')
        if os.path.exists(migrations_dir):
            print(f"🧹 Limpando migrações antigas em {migrations_dir}")
            for f in os.listdir(migrations_dir):
                if f not in ['__init__.py', '__pycache__']:
                    os.remove(os.path.join(migrations_dir, f))

        # 3. Cria um novo banco de dados
        print("\n🔨 Criando novo banco de dados...")
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])

        print("\n" + "="*50)
        print("🎉 BANCO DE DADOS RESETADO COM SUCESSO!")
        print("="*50 + "\n")

    except Exception as e:
        print("\n❌ ERRO durante o reset do banco de dados:")
        print(f"Erro: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica se o comando atual é 'runserver' para evitar rodar o reset em outros comandos (como collectstatic)
    if 'runserver' in sys.argv:
        reset_database()
    
    # Inicia o Django normalmente
    execute_from_command_line(sys.argv)
