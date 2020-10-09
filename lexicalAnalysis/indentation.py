def perm(1):
        # Compute the list of all permutations of l
    if len(1) <= 1:
                  return [1]
              
    r = []
    for i in range(len(1)):
            s = l[:i] +l[i+1:]
            p = perm(s)
            for x in p:
                r.append(l[i:i+1] + x)
    return r 

theWorldIsFlat = True
if theWorldIsFlat:
    print("Becareful so you won't fall off...")
