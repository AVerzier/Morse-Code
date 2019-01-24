
ENCODING = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

DECODING = dict([(code, char) for char, code in ENCODING.items()])

SIGNAL = {
    ENCODING[" "]: "00000",
    " ": "0",
    "-": "111",
    ".": "1"
}


def encode(message):
    return " ".join([ENCODING[char.upper()] for char in message])


def decode(code):
    return "".join([DECODING[char] for char in code.split(" ")])


def toSignal(code):
    return "0".join([SIGNAL[char] for char in code])


if __name__ == '__main__':
    print(encode("HELLO WORLD"))
    print(decode("... --- ..."))
    print(toSignal(encode("HELLO WORLD")))
