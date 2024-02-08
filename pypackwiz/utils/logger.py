from . import colors

def info(msg: str, **kwargs):
    print(f"{colors.BLUE}info:{colors.RESET} {msg}{colors.RESET}", **kwargs)

def warn(msg: str, **kwargs):
    print(f"{colors.YELLOW}warning:{colors.RESET} {msg}{colors.RESET}", **kwargs)

def error(msg: str, code: int = 1, **kwargs):
    print(f"{colors.RED}error:{colors.RESET} {msg}{colors.RESET}", **kwargs)
    exit(code)

def status(backend, function, msg: str):
    backend(msg, end="\r")
    function()
    backend(msg + f" {colors.GREEN}ok")

def prompt(msg: str, default: str = "") -> str:
    default_str = " [{}]".format(default) if default != "" else ""
    inp = input(f"{colors.GREEN}prompt:{colors.RESET} {msg}{default_str} > ")

    if inp == "":
        return default

    return inp