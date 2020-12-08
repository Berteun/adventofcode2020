from enum import Enum
from collections import namedtuple
class OpCode(Enum):
    acc = 1
    jmp = 2
    nop = 3

Instruction = namedtuple('Instruction', ['opcode', 'argument'])

class Machine:

    def __init__(self, instructions):
        self.__states = set()
        self.acc = 0
        self.ip = 0
        self.instructions = instructions

    def run(self):
        while self.ip not in self.__states:
            self.__states.add(self.ip)
            instr = self.instructions[self.ip]        
            if instr.opcode == OpCode.acc:
                self.acc += instr.argument
                self.ip += 1
            elif instr.opcode == OpCode.jmp:
                self.ip += instr.argument
            elif instr.opcode == OpCode.nop:
                self.ip += 1
            else: 
                raise RuntimeError("Impossible!")
            if 0 <= self.ip < len(self.instructions):    
                break

def read_input():
    f = open("input")
    instructions = []
    for l in f:
        opc, arg = l.strip().split()
        instructions.append(Instruction(OpCode[opc], int(arg)))
    return instructions

def main():
    instructions = read_input()
    machine = Machine(instructions)
    machine.run()
    print(machine.acc)

if __name__ == '__main__':
    main()
