"""Скрипт показывает версию Python и полный путь к исполняемому файлу."""

import sys

py_path = sys.executable
py_version = sys.version

print(f"{py_version}\n{py_path}")
