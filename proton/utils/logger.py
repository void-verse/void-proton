from colorama import Fore, Style


def highlight(msg):
    hl = False
    chars = [char for char in msg]
    msg = ""
    for char in chars:
        if char == "*" and not hl:
            msg += Fore.YELLOW
            hl = True
        elif char == "*" and hl:
            msg += Style.RESET_ALL
            hl = False
        else:
            msg += char
    return msg


def err(field, err):
    err = highlight(err)
    return f"{Fore.RED}{Style.BRIGHT}[ERR]  {Style.RESET_ALL}{Fore.YELLOW}{field}: {Style.RESET_ALL}{err}"


def warn(msg):
    return f"{Fore.YELLOW}{msg}{Style.RESET_ALL}"


def msg(field, msg):
    msg = highlight(msg)
    return f"\b\b{Fore.YELLOW}{Style.BRIGHT}[{field}]  {Style.RESET_ALL}{msg}"


def log(field, head, body):
    clr = Fore.GREEN if field == 'REQ' else Fore.BLUE
    body = highlight(body)
    return f"{clr}{Style.BRIGHT}[{field}]  {Style.RESET_ALL}{Fore.YELLOW}{head}: {Style.RESET_ALL}{body}"


if __name__ == '__main__':
    print(log("REQ", "POST", "*/*test*/*url"))
    print(log("RES", 200, "OK"))
    print(err("TEST", "Testing *logging* system"))
    print(msg("TEST", "Testing *logging* system"))
    print(warn("Testing logging system"))
