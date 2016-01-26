# This code is based on the julia code found at the following link:
# https://github.com/JuliaLang/julia/issues/1684
# posted by GlenHertz

# Read until takes the file handler "s" and the string "t" as an input
# and goes through "s" starting from the current position until it finds
# the matching pattern "t".
# In that case it returns the string it just read. If it reaches the end of file
# whatever he read from the starting point up to the end of file.

def readuntil (s, t):
    if (len(t) == 0):
        return ""
    nmi = 0  # current non-matching index
    out = ""
    while (True):
        c = s.read(1)
        if (c == ""):
            return out
        out += c
        if (c == t[nmi]):
            nmi += 1
            if (nmi > len(t)-1):
                return out
        else:
            nmi = 0
    return out
