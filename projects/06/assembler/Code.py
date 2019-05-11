from helpers.comp_dict import build_comp_dict
from helpers.dest_dict import build_dest_dict
from helpers.jump_dict import build_jump_dict

class Code:
    
    def __init__(self):
        self.comp_dict = build_comp_dict()
        self.dest_dict = build_dest_dict()
        self.jump_dict = build_jump_dict()

    def dest(self, mnemonic):
        if mnemonic == '':
            mnemonic = 'null'
        if mnemonic in self.dest_dict:
            return self.dest_dict[mnemonic]
        raise Exception("Unknown dest: {}".format(mnemonic))

    def comp(self, mnemonic):
        if mnemonic in self.comp_dict:
            return self.comp_dict[mnemonic]
        raise Exception("Unknown comp: {}".format(mnemonic))

    def jump(self, mnemonic):
        if mnemonic == '':
            mnemonic = 'null'
        if mnemonic in self.jump_dict:
            return self.jump_dict[mnemonic]
        raise Exception("Unknown jump: {}".format(mnemonic))