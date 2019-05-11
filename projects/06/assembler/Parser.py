class Command:
    A, C, L, EMPTY = range(4)

class Parser:

    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.current = None

    def __del__(self):
        self.file.close()

    def has_more_commands(self):
        cur_pos = self.file.tell()
        has_more = bool(self.file.readline())
        self.file.seek(cur_pos)
        return has_more

    def advance(self):
        line = self.file.readline()
        if '//' in line:
            line = line.split('//')[0]
        line = line.strip()
        self.current = line

    def command_type(self):
        if self.__is_A_command():
            return Command.A
        if self.__is_C_command():
            return Command.C
        if self.__is_L_command():
            return Command.L
        if self.current == '':
            return Command.EMPTY
        raise Exception("Current command is invalid: {}".format(self.current))

    def __is_A_command(self):
        return self.current.startswith('@')

    def __is_C_command(self):
        return '=' in self.current or ';' in self.current

    def __is_L_command(self):
        return self.current.startswith('(') and self.current.endswith(')')

    def symbol(self):
        if self.__is_A_command():
            return self.current[1:]
        if self.__is_L_command():
            return self.current[1:-1]
        raise Exception("Not A_COMMAND or L_COMMAND")

    def dest(self):
        if self.__is_C_command():
            eq_idx = self.current.find('=')
            if eq_idx == -1:
                return ''
            return self.current[:eq_idx]
        raise "Not C_COMMAND"

    def comp(self):
        if self.__is_C_command():
            eq_idx = self.current.find('=')
            sem_idx = self.current.find(';')
            if self.dest() == '':
                return self.current[:sem_idx]
            if self.jump() == '':
                return self.current[eq_idx + 1:]
            return self.current[eq_idx + 1:sem_idx]
        raise "Not C_COMMAND"

    def jump(self):
        if self.__is_C_command():
            sem_idx = self.current.find(';')
            if sem_idx == -1:
                return ''
            return self.current[sem_idx + 1:]
        raise "Not C_COMMAND"