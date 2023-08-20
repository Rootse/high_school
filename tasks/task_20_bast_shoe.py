class Lapotle:
    def __init__(self):
        self.string = ""
        self.history = [""]
        self.index = 0

    def add(self, s: str):
        self.string += s

        self.history.append(self.string)
        self.index = len(self.history) - 1

    def delete(self, n: int):
        n = min(n, len(self.string))
        self.string = self.string[:-n]
        self.history.append(self.string)
        self.index = len(self.history) - 1

    def issue(self, i: int):
        return self.string[i] if 0 <= i < len(self.string) else ""

    def undo(self):
        self.index = max(self.index - 1, 0)
        self.string = self.history[self.index]

    def redo(self):
        self.index = min(self.index + 1, len(self.history) - 1)
        self.string = self.history[self.index]


def BastShoe(command: str) -> str:
    global shoe
    if not ('shoe' in globals()):
        shoe = Lapotle()

    if command:
        cmd = command.split(' ', 1)
        option = int(cmd[0])
        param = cmd[1] if len(cmd) > 1 else ""

        actions = {
            1: shoe.add,
            2: shoe.delete,
            3: shoe.issue,
            4: shoe.undo,
            5: shoe.redo,
        }

        if option in actions:
            if option == 1:
                actions[option](param)
            elif option == 2:
                actions[option](int(param))
            if option == 3:
                return actions[option](int(param))
            elif option in (4, 5):
                actions[option]()

    return shoe.string
