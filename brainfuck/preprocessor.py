def preprocess(program):

    stack = []
    jump_table = {}
        
    i = 0
    while i < len(program):
        if program[i] == "[":
            stack.append(i)
        elif program[i] == "]":
            if not stack:
                raise SyntaxError("Unexpected ']'")
                
            jt_id = stack.pop()
            jump_table[jt_id] = i
            jump_table[i] = jt_id

        i += 1
    if stack:
        raise SyntaxError("Missing Closing ']'")
    
    return jump_table