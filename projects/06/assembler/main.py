import sys
from Parser import *
from Code import *

def main():
    filename_full = str(sys.argv[1])

    filename = filename_full.split('.')[0]
    out_f = open(filename + '.hack', 'w')

    parser = Parser(filename_full)
    code = Code()

    while(parser.has_more_commands()):
        parser.advance()
        cmd_type = parser.command_type()

        if cmd_type == Command.A:
            a = parser.symbol()
            binary_a = format(int(a), 'b')
            while(len(binary_a) < 16):
                binary_a = '0' + binary_a

            out = binary_a
            out_f.write(out + '\n')
        elif cmd_type == Command.C:
            c = parser.comp()
            d = parser.dest()
            j = parser.jump()

            cc = code.comp(c)
            dd = code.dest(d)
            jj = code.jump(j)

            out = '111' + cc + dd + jj
            out_f.write(out + '\n')
        elif cmd_type == Command.EMPTY:
            continue
        else:
            raise Exception("Invalid HACK command: {}".format(parser.current))

    out_f.close()

if __name__ == "__main__":
    main()