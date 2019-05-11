import sys
from Parser import *
from Code import *

def process_file(filename_full, func_a_cmd, func_c_cmd, func_l_cmd):
    parser = Parser(filename_full)
    while(parser.has_more_commands()):
        parser.advance()
        cmd_type = parser.command_type()

        if cmd_type == Command.A:
            func_a_cmd(parser)
        elif cmd_type == Command.C:
            func_c_cmd(parser)
        elif cmd_type == Command.L:
            func_l_cmd(parser)
        elif cmd_type == Command.EMPTY:
            continue
        else:
            raise Exception("Invalid HACK command: {}".format(parser.current))

def parse_a_cmd(parser):
    a = parser.symbol()
    binary_a = format(int(a), 'b')
    while(len(binary_a) < 16):
        binary_a = '0' + binary_a
    return binary_a

def parse_c_cmd(parser, code):
    c = parser.comp()
    d = parser.dest()
    j = parser.jump()

    cc = code.comp(c)
    dd = code.dest(d)
    jj = code.jump(j)

    return '111' + cc + dd + jj

def main():
    filename_full = str(sys.argv[1])

    filename = filename_full.split('.')[0]
    out_f = open(filename + '.hack', 'w')

    code = Code()

    process_file(filename_full,\
        lambda p: out_f.write(parse_a_cmd(p) + '\n'),\
        lambda p: out_f.write(parse_c_cmd(p, code) + '\n'),\
        None)

    out_f.close()

if __name__ == "__main__":
    main()