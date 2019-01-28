def grouper(stack):
    while len(stack) > 0:
        yield (stack[0], stack[1], stack[2])
        del stack[0]
        del stack[0]
        del stack[0]
    return None


def process(command, a, b):
    if command == 1:
        return a + b
    if command == 2:
        return a - b
    if command == 3:
        return a * b
    if command == 4:
        return a / b
    return None


def run(code, debug=False):
    ans = 0
    code = code.replace('\r', '')
    while '\n\n' in code:
        code = code.replace('\n\n', '\n')
    while '  ' in code:
        code = code.replace('  ', ' ')
    parts = code.replace('\n', ' ').split(' ')
    if len(parts) % 3 != 0:
        return "Неверное количество команд"
    for bcommand, a, b in grouper(parts):

        if len(bcommand) != 8:
            return "Неизвестная команда '{}'".format(bcommand)

        try:
            command = int(bcommand, 2)
        except:
            return "Неизвестная команда '{}'".format(bcommand)

        if command > 4 or command == 0:
            return "Неизвестная команда '{}'".format(bcommand)

        if debug:
            print("command is {}".format(command))

        try:
            if len(a) != 8:
                raise Exception()
            a = int(a, 2)
        except:
            return "Некорректное числовое значение '{}'".format(a)

        if debug:
            print("a is {}".format(a))

        try:
            if len(b) != 8:
                raise Exception()
            b = int(b, 2)
        except:
            return "Некорректное числовое значение '{}'".format(b)

        if debug:
            print("b is {}".format(b))

        if a == 255:
            a = ans
        if b == 255:
            b = ans
        ans = process(command, a, b)

    return ans

if __name__ == "__main__":
    code = "00000001 00001000 00000100 00000010 11111111 00000001 3"
    print(run(code))

