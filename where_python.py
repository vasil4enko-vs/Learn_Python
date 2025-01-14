"""Скрипт показывает версию Python и полный путь к исполняемому файлу."""

import sys

# Получаем путь и версию Python
python_path = sys.executable
python_version = sys.version

# Выводим информацию
print(f"Python Version: {python_version}")
print(f"Python Path: {python_path}")
