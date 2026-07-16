from .preprocessor import preprocess 

def interpret(program):

    MEMORY_SIZE = 30000
    memory = [0] * MEMORY_SIZE

    #DP is the data pointer which points to the memory in the memory tape
    dp = 0

    #IP is the instruction pointer, this points to the instruction, i.e., ><+-[]., in the program through the file reader.
    ip = 0


    class TapeOverflowError(Exception):
        pass

    jump_table = preprocess(program)

    while ip < len(program):
        instruction = program[ip]
        
        if instruction == ">":
            if dp == 29999:
                raise TapeOverflowError("Out of memory, tape is full")
            else:
                dp += 1

        elif instruction == "<":
            if dp == 0:
                raise TapeOverflowError("Data pointer on block 0, cannot move backwards.")
            else:
                dp -= 1

        elif instruction == ".":
            print(chr(memory[dp]), end="")
        
        elif instruction == "+":
            memory[dp] = (memory[dp] + 1) % 256

        elif instruction == "-":
            memory[dp] = (memory[dp] - 1) % 256

        elif instruction == ",":
            memory[dp] = ord(input()[0])

        elif instruction == "[":
            if memory[dp] == 0:
                ip = jump_table[ip]

        elif instruction == "]":
            if memory[dp] != 0:
                ip = jump_table[ip]

        ip += 1
