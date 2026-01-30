import re

ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def remove_colour(text):
    return ANSI_RE.sub("", text)
