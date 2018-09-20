import sys

def add_value(value):
    print('Add Value', value + 5)

def delete_value(value):
    print('Delete Value', value - 5)

def exit_operations(value):
    sys.exit()

def wrong_option(value):
    print('Invalid option')

operations = {
    'a': add_value,
    'd': delete_value,
    'e': exit_operations,
}

while True:
    option = str(input('''
        ¿What do you want to do?

        [a]dd value
        [d]elete value
        [e]xit
        '''))

    value = 5
    operations.get(option, wrong_option)(value)
