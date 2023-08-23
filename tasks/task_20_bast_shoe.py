class Lapotle:
    def __init__(self):
        self.string = ""
        self.last_action = 0
        self.undo_stack = []
        self.redo_stack = []

    def add(self, s):
        self.redo_stack.clear()
        if self.last_action in (4, 5):
            self.undo_stack.clear()
        self.undo_stack.append(self.string)
        self.string += s
        self.last_action = 1

    def delete(self, n):
        self.redo_stack.clear()
        if self.last_action in (4, 5):
            self.undo_stack.clear()
        self.undo_stack.append(self.string)
        self.string = self.string[:-n]
        self.last_action = 2

    def issue(self, i):
        self.last_action = 3
        return self.string[i] if 0 <= i < len(self.string) else ""

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.string)
            self.string = self.undo_stack.pop()
            self.last_action = 4

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.string)
            self.string = self.redo_stack.pop()
            self.last_action = 5


def BastShoe(command: str) -> str:
    if not hasattr(BastShoe, 'shoe'):
        BastShoe.shoe = Lapotle()

    if command:
        cmd = command.split(' ', 1)
        option = int(cmd[0])
        param = cmd[1] if len(cmd) > 1 else ""

        if option == 1:
            BastShoe.shoe.add(param)
        elif option == 2:
            BastShoe.shoe.delete(int(param))
        elif option == 3:
            return BastShoe.shoe.issue(int(param))
        elif option == 4:
            BastShoe.shoe.undo()
        elif option == 5:
            BastShoe.shoe.redo()

    return BastShoe.shoe.string
