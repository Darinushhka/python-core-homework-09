def input_error(func):                                                 #декоратор
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command. Please try again."                   #оброблюємо винятки
    return wrapper


contacts = {}                                                               #для збереження контактів у словник


@input_error                                                                #декоратор накладаємо                                                       
def hello_command():
    return "How can I help you?"                                                            #функції для обробки команд


@input_error
def add_contact_command(params):
    name, phone = params.split()
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"


@input_error
def change_contact_command(params):
    name, phone = params.split()
    contacts[name] = phone
    return f"Phone number for {name} changed to {phone}"


@input_error
def phone_command(name):
    return contacts[name]


@input_error
def show_all_command():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."


def main():
    print("Welcome to the Assistant Bot!")
    print("Available commands: hello, add [name] [phone], change [name] [phone], phone [name], show all, good bye")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "hello":
            print(hello_command())
        elif command.startswith("add"):
            print(add_contact_command(command[4:].strip()))
        elif command.startswith("change"):
            print(change_contact_command(command[7:].strip()))
        elif command.startswith("phone"):
            print(phone_command(command[6:].strip()))
        elif command == "show all":
            print(show_all_command())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
