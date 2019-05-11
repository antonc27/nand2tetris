def build_jump_dict():
    data = '''
null 0 0 0
JGT 0 0 1
JEQ 0 1 0
JGE 0 1 1
JLT 1 0 0
JNE 1 0 1
JLE 1 1 0
JMP 1 1 1
    '''

    jump_dict = {}
    lines = data.split('\n')

    for line in lines:
        splitted = line.split(' ')

        cmd_left = splitted[0]
        if not cmd_left:
            continue

        list_body = splitted[1:]
        body = ''.join(list_body)

        jump_dict[cmd_left] = body

    return jump_dict