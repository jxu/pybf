# Derpy brainfuck interpreter. Anyone can use this.


# Global variables
DEBUG = False
FILE = "multiply2.b"
CELL_MAX = 256


with open("examples/"+FILE, 'r') as f:
    program = f.read()

tape = [0] * 300000 # Standard size
instruction_pointer = 0
data_pointer = 0
loop_level = 0

while instruction_pointer < len(program):
    instruction_pointer_forward = True
    
    char = program[instruction_pointer]
    data = tape[data_pointer]
    
    if DEBUG:
        if char in "><+-.,[]":
            print(char, instruction_pointer, data)

    if char == ">":
        data_pointer += 1

    if char == "<":
        data_pointer -= 1

    if char == "+":
        tape[data_pointer] = (data + 1) % CELL_MAX

    if char == "-":
        tape[data_pointer] = (data - 1) % CELL_MAX

    if char == ".":
        print(chr(data), end="")

    if char == ",":
        tape[data_pointer] = ord(input())
             
    if char == "[" and data == 0:
        instruction_pointer_forward = False
        
        loop_level = 1
        
        while loop_level > 0:
            instruction_pointer += 1
            char = program[instruction_pointer]
            # Simple bracket parsing
            if char == "[":
                loop_level += 1
            if char == "]":
                loop_level -= 1

        instruction_pointer += 1
            
    if char == "]" and data != 0:
        instruction_pointer_forward = False
        
        loop_level = 1
        
        while loop_level > 0:
            instruction_pointer -= 1
            char = program[instruction_pointer]
            # Reverse parsing
            if char == "[":
                loop_level -= 1
            if char == "]":
                loop_level += 1
                
        instruction_pointer += 1

    if instruction_pointer_forward:
        instruction_pointer += 1
        
