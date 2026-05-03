#!/usr/bin/env python3

# Simple VM Bytecode Interpreter

class SimpleVM:
    def __init__(self):
        self.registers = {'A': 0, 'B': 0, 'PC': 0}
        
    def execute(self, bytecode):
        """Execute bytecode"""
        pc = 0
        while pc < len(bytecode):
            op = bytecode[pc]
            
            if op == 0x01:  # LOAD A
                self.registers['A'] = bytecode[pc + 1]
                pc += 2
            elif op == 0x02:  # LOAD B
                self.registers['B'] = bytecode[pc + 1]
                pc += 2
            elif op == 0x03:  # ADD
                self.registers['A'] += self.registers['B']
                pc += 1
            elif op == 0x04:  # CMP
                if self.registers['A'] == bytecode[pc + 1]:
                    print("MATCH!")
                pc += 2
            elif op == 0xFF:  # END
                break
            else:
                pc += 1

# Example bytecode
bytecode = [
    0x01, 0x0A,  # LOAD A 10
    0x02, 0x05,  # LOAD B 5
    0x03,        # ADD
    0x04, 0x0F,  # CMP 15
    0xFF         # END
]

vm = SimpleVM()
vm.execute(bytecode)
