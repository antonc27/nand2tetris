def build_comp_dict():
    data = '''
0 1 0 1 0 1 0
1 1 1 1 1 1 1
-1 1 1 1 0 1 0
D 0 0 1 1 0 0
A 1 1 0 0 0 0 M
!D 0 0 1 1 0 1
!A 1 1 0 0 0 1 !M
-D 0 0 1 1 1 1
-A 1 1 0 0 1 1 -M
D+1 0 1 1 1 1 1
A+1 1 1 0 1 1 1 M+1
D-1 0 0 1 1 1 0
A-1 1 1 0 0 1 0 M-1
D+A 0 0 0 0 1 0 D+M
D-A 0 1 0 0 1 1 D-M
A-D 0 0 0 1 1 1 M-D
D&A 0 0 0 0 0 0 D&M
D|A 0 1 0 1 0 1 D|M
    '''

    comp_dict = {}
    lines = data.split('\n')

    for line in lines:
        splitted = line.split(' ')

        cmd_left = splitted[0]

        cmd_right = splitted[-1]
        has_right = cmd_right != '' and cmd_right != '0' and cmd_right != '1'

        if has_right:
            list_body = splitted[1:-1]
        else:
            list_body = splitted[1:]
        
        body = ''.join(list_body)

        if not cmd_left:
            continue

        comp_dict[cmd_left] = '0' + body

        if has_right:
            comp_dict[cmd_right] = '1' + body

    return comp_dict