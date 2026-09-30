# Отчёт по лабораторной работе №5

Самодуров Матвей Николаевич, группа 221341, вариант 8.

## Средняя сложность

- **№4 Список (Listbox) и выбор элемента** — `lab5/listbox_app.py`:
  функция `build_listbox_window(root, items, on_select)` наполняет
  `tk.Listbox` строками из `items`, подписывает событие
  `<<ListboxSelect>>` и показывает выбранное значение в метке под
  списком, вызывая `on_select`. Чистая функция `selected_item(items,
  index)` возвращает элемент по индексу или `None`, если индекс
  отрицательный или за пределами длины. `tkinter` импортируется
  лениво — внутри функции, поэтому модуль загружается без дисплея.
- **№8 Диалог выбора файла** — `lab5/file_dialog.py`:
  `choose_file(dialog=None)` по умолчанию берёт
  `tkinter.filedialog.askopenfilename` (ленивый импорт), но принимает
  подделанный `dialog` для тестов; пустая строка отмены нормализуется
  в `None`. `build_file_window(root, chooser)` собирает кнопку и метку
  статуса, в которую записывается выбранный путь.
- **№10 Простейший GUI на PyQt5** — `lab5/pyqt_hello.py`:
  `build_window()` ленивого импортирует `PyQt5.QtWidgets` внутри
  тела функции, создаёт `QWidget` с `QLabel` и `QPushButton`; слот
  кнопки заменяет текст метки. Модуль импортируется даже там, где
  PyQt5 не установлен.

## Повышенная сложность

- **№1 Программа «Заметки»** — `lab5/notes.py` + `lab5/notes_app.py`:
  класс `NotesModel` хранит заметки в списке и полностью работает без
  GUI: `add()`, `all()` (возвращает копию), `save(path)` пишет JSON
  массив строк с `ensure_ascii=False`, `load(path)` заменяет
  содержимое и проверяет структуру (`ValueError` для не-массива и
  не-строк, `FileNotFoundError` для отсутствующего файла).
  `lab5/notes_app.py` — Tkinter-обёртка: поле ввода, кнопка
  «Сохранить» и список заметок; ленивые импорты, вызов только из
  `__main__`.
- **№8 Программа с несколькими окнами** — `lab5/multiwindow.py`:
  `build_main_window(root, open_child)` создаёт кнопку «Открыть
  окно», `open_child_window(parent)` открывает `Toplevel` с полем
  ввода и кнопкой закрытия, а чистая функция
  `child_window_title(index)` выдаёт заголовок вида
  `Child window N` и отвергает индексы меньше единицы
  (`ValueError`).

## Стратегия headless-тестов

В среде выполнения и в CI нет графического дисплея, поэтому:

1. `tkinter` и `PyQt5` импортируются **лениво** — внутри функций
   конструкторов окон, а не на уровне модуля; аннотации типов
   (`tk.Misc`, `QWidget`) — строки под `from __future__ import
   annotations` и `TYPE_CHECKING`.
2. Ни один тест не создаёт `tk.Tk()`, `Toplevel` и `QApplication`:
   проверяется только чистая логика (`selected_item`,
   `choose_file` с подделанным `dialog`, `NotesModel`,
   `child_window_title`) и импорт модулей.
3. Тест PyQt5 оформлен через
   `unittest.skipUnless(importlib.util.find_spec("PyQt5") is not
   None, ...)` — без установленного пакета он помечается как skipped,
   а `find_spec` ничего не импортирует.
4. Демо `python -m lab5` печатает списки задач и открывает окно
   только при заданной переменной `DISPLAY`, иначе печатает
   `No display available`.

## Проверки

- Демонстрация без дисплея:

```text
$ env -u DISPLAY uv run python -m lab5
Medium tasks
  No.4 listbox and item selection -> lab5.listbox_app
  No.8 file open dialog -> lab5.file_dialog
  No.10 simplest GUI on PyQt5 -> lab5.pyqt_hello
Advanced tasks
  No.1 notes program -> lab5.notes, lab5.notes_app
  No.8 multi-window program -> lab5.multiwindow
No display available
```

- Тесты (`uv run --with flake8 python -m unittest discover -s tests -v`),
  вывод реальный:

```text
test_empty_string_means_cancellation (test_file_dialog.ChooseFileTests.test_empty_string_means_cancellation)
An empty dialog result is normalised to ``None``. ... ok
test_module_imports_without_tkinter (test_file_dialog.ChooseFileTests.test_module_imports_without_tkinter)
The module imports headless and exposes its builder. ... ok
test_returns_path_from_injected_dialog (test_file_dialog.ChooseFileTests.test_returns_path_from_injected_dialog)
A path returned by the dialog is passed through. ... ok
test_empty_sequence_always_returns_none (test_listbox_app.SelectedItemTests.test_empty_sequence_always_returns_none)
Any index on an empty sequence is out of range. ... ok
test_existing_index_returns_element (test_listbox_app.SelectedItemTests.test_existing_index_returns_element)
An index inside the sequence returns its element. ... ok
test_index_past_the_end_returns_none (test_listbox_app.SelectedItemTests.test_index_past_the_end_returns_none)
An index equal to the length is out of range. ... ok
test_module_imports_without_display (test_listbox_app.SelectedItemTests.test_module_imports_without_display)
The module imports headless and exposes its builder. ... ok
test_negative_index_returns_none (test_listbox_app.SelectedItemTests.test_negative_index_returns_none)
Negative positions are out of range, not from the tail. ... ok
test_first_window_title (test_multiwindow.ChildWindowTitleTests.test_first_window_title)
Window number one gets the base title. ... ok
test_index_below_one_is_rejected (test_multiwindow.ChildWindowTitleTests.test_index_below_one_is_rejected)
Zero and negative indexes are not valid window numbers. ... ok
test_later_window_title (test_multiwindow.ChildWindowTitleTests.test_later_window_title)
The index is embedded in the title verbatim. ... ok
test_module_imports_without_display (test_multiwindow.ChildWindowTitleTests.test_module_imports_without_display)
The module imports headless and exposes both builders. ... ok
test_add_collects_notes_in_order (test_notes.NotesModelTests.test_add_collects_notes_in_order)
Notes are appended and returned in insertion order. ... ok
test_all_returns_a_copy (test_notes.NotesModelTests.test_all_returns_a_copy)
Mutating the returned list does not touch the model. ... ok
test_load_missing_file_raises (test_notes.NotesModelTests.test_load_missing_file_raises)
Loading a nonexistent file reports FileNotFoundError. ... ok
test_load_rejects_non_array_payload (test_notes.NotesModelTests.test_load_rejects_non_array_payload)
A JSON object instead of an array is rejected. ... ok
test_load_rejects_non_string_items (test_notes.NotesModelTests.test_load_rejects_non_string_items)
An array holding non-string values is rejected. ... ok
test_notes_app_imports_without_display (test_notes.NotesModelTests.test_notes_app_imports_without_display)
The Tkinter wrapper module loads headless. ... ok
test_save_and_load_roundtrip (test_notes.NotesModelTests.test_save_and_load_roundtrip)
A saved model is restored with the same notes. ... ok
test_save_keeps_unicode_readable (test_notes.NotesModelTests.test_save_keeps_unicode_readable)
Non-ASCII text is stored literally, not as escapes. ... ok
test_module_imports_without_pyqt5 (test_pyqt_hello.PyqtHelloTests.test_module_imports_without_pyqt5)
The module imports headless and exposes its builder. ... ok
test_pyqt5_is_imported_lazily (test_pyqt_hello.PyqtHelloTests.test_pyqt5_is_imported_lazily)
Reloading the module never touches PyQt5. ... ok
test_qt_is_available_and_builder_callable (test_pyqt_hello.PyqtHelloTests.test_qt_is_available_and_builder_callable)
With PyQt5 installed the spec resolves and the API works. ... skipped 'PyQt5 is not installed'

----------------------------------------------------------------------
Ran 23 tests in 0.002s

OK (skipped=1)
```

- Прогон с установленным PyQt5
  (`uv run --with flake8 --with PyQt5 python -m unittest discover -s tests -v`):
  те же 23 теста, `OK` без skipped.

- Стиль (`uv run --with flake8 flake8 lab5 tests`) — замечаний нет,
  пустой вывод, код возврата 0:

```text
$ uv run --with flake8 flake8 lab5 tests; echo "exit=$?"
exit=0
```

- Компиляция (`uv run python -m compileall -q lab5 tests`):

```text
$ uv run python -m compileall -q lab5 tests; echo "exit=$?"
exit=0
```

- CI: GitHub Actions workflow `.github/workflows/python-checks.yml`
  с матрицей Python `["3.12", "3.13"]`: flake8, compileall, unittest.
