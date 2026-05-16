solutions = []
for x in range(1, 10):
    for o in range(0, 10):
        if o == x:
            continue
        for d in range(0, 10):
            if d in (x, o):
                continue
            for m in range(1, 10):
                if m in (x, o, d):
                    continue
                for a in range(0, 10):
                    if a in (x, o, d, m):
                        continue
                    for t in range(0, 10):
                        if t in (x, o, d, m, a):
                            continue
                        hod = x * 100 + o * 10 + d
                        mat = m * 100 + a * 10 + t
                        if hod * 3 == mat:
                            solutions.append(f"{hod}+{hod}+{hod}={mat}")

for sol in sorted(solutions):
    print(sol)