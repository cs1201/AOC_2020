
class State:
    pc = 0
    acc = 0
    last_acc = 0
    visted_instructions = set()

    def reset(self):
        self.acc = 0
        self.pc = 0
        self.last_acc = 0
        self.visted_instructions = set()


def parse_instruction(state, instruction):
    op, arg = instruction
    state.last_acc = state.acc
    if op == "acc":
        state.acc += int(arg)
        state.pc += 1
    if op == "jmp":
        state.pc += int(arg)
    if op == "nop":
        state.pc += 1

def part_one(data):
    state = State()
    while state.pc < len(data):
        parse_instruction(state, data[state.pc])
        if state.pc not in state.visted_instructions:
            state.visted_instructions.add(state.pc)
        else:
            return state.last_acc

def part_two(data):
    state = State()  
    # Brute force - swapping jmp/nop until we terminate successfully
    for i, (op, arg) in enumerate(data):
        state.reset() #Reset computer
        data_edit = data.copy()
        if op == "jmp":
            data_edit[i] = ("nop", arg)
        elif op == "nop":
            data_edit[i] = ("jmp", arg)
        else:
            continue

        while state.pc <= len(data_edit):
            # Terminated
            if state.pc == len(data_edit):
                return state.acc
            parse_instruction(state, data_edit[state.pc])
            # Check not in Infinite loop by visiting instruction twice
            if state.pc in state.visted_instructions:    
                break
            else:
                state.visted_instructions.add(state.pc)
        
with open("data/day_8.txt") as f:
    data = [(i.split()[0].strip(), i.split()[1].strip()) for i in f.readlines()]
    print(f"Part One: {part_one(data)}") # 1814
    print(f"Part Two: {part_two(data)}") # 1056