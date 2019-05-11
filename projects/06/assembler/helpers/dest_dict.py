def build_dest_dict():
    data = '''
null 0 0 0
M 0 0 1
D 0 1 0
MD 0 1 1 
A 1 0 0
AM 1 0 1 
AD 1 1 0 
AMD 1 1 1
    '''

    dest_dict = {}
    lines = data.split('\n')

    for line in lines:
        splitted = line.split(' ')

        cmd_left = splitted[0]
        if not cmd_left:
            continue

        list_body = splitted[1:]
        body = ''.join(list_body)

        dest_dict[cmd_left] = body

    return dest_dict