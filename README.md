# Лабораторная работа №5

Самодуров Матвей Николаевич, группа 221341, вариант 8, лабораторная №5.

## Задания варианта

**Средняя сложность:**

- №4 — список (Listbox) и выбор элемента (`lab5/listbox_app.py`)
- №8 — диалог выбора файла (`lab5/file_dialog.py`)
- №10 — простейший GUI на PyQt5 (`lab5/pyqt_hello.py`)

**Повышенная сложность:**

- №1 — программа «Заметки» с сохранением в файл
  (`lab5/notes.py`, `lab5/notes_app.py`)
- №8 — программа с несколькими окнами (`lab5/multiwindow.py`)

## Клонирование

```bash
git clone https://github.com/kyomufs/mtp-lab5-variant8.git
cd mtp-lab5-variant8
```

## Запуск

Демонстрация (выводит список задач; GUI-окно открывается только при
заданной переменной `DISPLAY`):

```bash
uv run python -m lab5
```

## Проверки

```bash
uv run --with flake8 python -m unittest discover -s tests -v
uv run --with flake8 flake8 lab5 tests
python -m compileall -q lab5 tests
```

Тесты не создают окон: чистая логика и импорты проверяются всегда,
GUI-конструкторы вызываются только из `__main__`. Подробное описание —
в `docs/report.md`.
