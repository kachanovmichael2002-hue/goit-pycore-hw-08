import pickle


class AddressBook(dict):
    """Клас адресної книги."""

    def add_record(self, name, phone):
        self[name] = phone


def save_data(book, filename="addressbook.pkl"):
    """Зберігає адресну книгу у файл."""
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="addressbook.pkl"):
    """Завантажує адресну книгу з файлу."""
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()

    print("Адресна книга запущена.")

    while True:
        command = input("Введіть команду (add/show/exit): ").strip().lower()

        if command == "add":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            book.add_record(name, phone)
            print("Контакт додано.")

        elif command == "show":
            if not book:
                print("Адресна книга порожня.")
            else:
                for name, phone in book.items():
                    print(f"{name}: {phone}")

        elif command == "exit":
            save_data(book)
            print("Дані збережено. До побачення!")
            break

        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()