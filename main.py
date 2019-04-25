import csv
import os
import sys
CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames = CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer= csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Client is not in clients list')


def delete_client(client):
        try:
            global clients

            delete = clients.pop(int(client))
            print('You delete: {}'.format(delete))
            print('')
        except IndexError:
            print('Index out range, intent with another one')
            client_uid = _get_client_uid()
            delete_client(client_uid)


def search_client(client_name):
    print('WELCOME TO SEARCH CLIENT')
    print('*' * 50)
    print('What would you like to SEARCH?')
    print('[N]ame')
    print('[C]ompany')
    print('[E]mail')
    print('[P]osition')
    print('')

    search_field = input()
    search_field = search_field.upper()

    if search_field == 'N':
        field = 'name'
    elif search_field == 'C':
        field = 'company'
    elif search_field == 'E':
        field = 'email'
    elif search_field == 'P':
        field = 'position'
    else:
        Print('Invalid command')

    _get_client_field(field)


    print(search_field)
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    """print('*' * 50)"""
    print('')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))

    return field


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_client_uid():
    client_uid = None
    while not client_uid:
        try:
            client_uid = int(input('What is the index number? '))
        except ValueError:
            print('Command incorrect please use a number')

    return client_uid


if __name__ == '__main__':
    _initialize_clients_from_storage()

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)

    elif command == 'L':
        list_clients()
    elif command == 'D':

        print('')
        client_uid = _get_client_uid()
        delete_client(client_uid)

    elif command == 'U':

        client_name = _get_client_name()
        update_client_name = input('What is the updated client name: ')
        update_client(client_name, update_client_name)

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')

    _save_clients_to_storage()
