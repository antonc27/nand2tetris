import sys
from Parser import *
from Code import *

class Counter:
    def __init__(self):
        self.value = 0

    def set(self, value):
        self.value = value

    def inc(self):
        self.value += 1

    def count(self):
        return self.value

def init_symbol_table():
    s_table = {}
    for i in range(16):
        k = 'R{}'.format(i)
        s_table[k] = i
    s_table['SP'] = 0
    s_table['LCL'] = 1
    s_table['ARG'] = 2
    s_table['THIS'] = 3
    s_table['THAT'] = 4
    s_table['SCREEN'] = 16384
    s_table['KBD'] = 24576
    return s_table

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

def parse_a_cmd(parser, st, var_counter):
    a = parser.symbol()

    if not a.isdigit():
        if not a in st:
            st[a] = var_counter.count()
            var_counter.inc()

        a = str(st[a])

    return parse_a_cmd_str(a)

def parse_a_cmd_str(a):
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

def parse_l_cmd(parser):
    return parser.symbol()

def main():
    filename_full = str(sys.argv[1])

    filename = filename_full.split('.')[0]
    out_f = open(filename + '.hack', 'w')

    code = Code()
    symbol_table = init_symbol_table()

    instrs_counter = Counter()
    process_file(filename_full,\
        lambda p: instrs_counter.inc(),\
        lambda p: instrs_counter.inc(),\
        lambda p: symbol_table.update({parse_l_cmd(p): instrs_counter.count()}))

    var_counter = Counter()
    var_counter.set(16)
    process_file(filename_full,\
        lambda p: out_f.write(parse_a_cmd(p, symbol_table, var_counter) + '\n'),\
        lambda p: out_f.write(parse_c_cmd(p, code) + '\n'),\
        lambda p: None)

    out_f.close()

if __name__ == "__main__":
    main()