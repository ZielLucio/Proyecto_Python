import sys
clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer',
    }

]


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
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        list_clients()
        print('')
        client_uid = _get_client_uid()
        delete_client(client_uid)
        list_clients()
    elif command == 'U':
        list_clients()
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name: ')
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
