import json
import datetime
import argparse

# Функция для добавления заметки


def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": str(datetime.datetime.now())
    }
    notes.append(note)
    save_notes()

# Функция для чтения заметок


def read_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['message']}")
        print(f"Дата/время: {note['timestamp']}")
        print()

# Функция для редактирования заметки


def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новый текст заметки: ")
            note['title'] = title
            note['message'] = message
            note['timestamp'] = str(datetime.datetime.now())
            save_notes()
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для удаления заметки


def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для сохранения заметок в файле


def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

# Функция для загрузки заметок из файла


def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Функция для вывода всех заметок


def list_notes():
    for note in notes:
        print(note['id'], note['title'])


# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser(
    description="Консольное приложение для заметок")
parser.add_argument("command", choices=[
                    "add", "read", "edit", "delete", "list"],
                    help="Команда для выполнения")
parser.add_argument("--title", help="Заголовок заметки")
parser.add_argument("--msg", help="Текст заметки")

# Парсинг аргументов командной строки
args = parser.parse_args()

# Загрузка заметок из файла
notes = load_notes()

# Выполнение команды
if args.command == "add":
    add_note()
elif args.command == "read":
    read_notes()
elif args.command == "edit":
    edit_note()
elif args.command == "delete":
    delete_note()
elif args.command == "list":
    list_notes()
