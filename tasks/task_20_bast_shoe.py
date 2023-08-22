class Lapotle:
    def __init__(self):
        self.string = ""
        self.undo_stack = []
        self.redo_stack = []

    def add(self, s):
        self.undo_stack += self.redo_stack
        self.redo_stack.clear()
        self.undo_stack.append(self.string)
        self.string += s

    def delete(self, n):
        self.undo_stack += self.redo_stack
        self.redo_stack.clear()
        self.undo_stack.append(self.string)
        self.string = self.string[:-n]

    def issue(self, i):
        return self.string[i] if 0 <= i < len(self.string) else ""

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.string)
            self.string = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.string)
            self.string = self.redo_stack.pop()


def BastShoe(command: str) -> str:
    global shoe
    if not ('shoe' in globals()):
        shoe = Lapotle()

    if command:
        cmd = command.split(' ', 1)
        option = int(cmd[0])
        param = cmd[1] if len(cmd) > 1 else ""

        actions = {
            1: lambda: shoe.add(param),
            2: lambda: shoe.delete(int(param)),
            3: lambda: shoe.issue(int(param)),
            4: lambda: shoe.undo(),
            5: lambda: shoe.redo(),
        }

        action = actions.get(option)
        result = action()
        if option == 3:
            return result

    return shoe.string
