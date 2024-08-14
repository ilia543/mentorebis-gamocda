def walk(wlk):
    i = len(wlk)
    if i != 10:
        print(False)
    else:
        if wlk.count("n")!= wlk.count("s") and wlk.count("w") != wlk.count("e"):
            print(False)
        elif wlk.count("n") != wlk.count("s") and wlk.count("w") == wlk.count("e"):
            print(False)
        elif wlk.count("n") == wlk.count("s") and wlk.count("w") != wlk.count("e"):
            print(False)
        elif wlk.count("n") == wlk.count("s") and wlk.count("w") == wlk.count("e"):
            print(True)



walk(["n", "s", "n", "s", "n", "s", "n", "s", "w", "e"])