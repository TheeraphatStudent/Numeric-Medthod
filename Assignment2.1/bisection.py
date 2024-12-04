import math

def bisections_method(f, errAbs, container):
    if (len(container) % 2 != 0):
        print("Container must be even! ")
        return
    
    results = []
    i = 0
    
    while i < (len(container) - 1):
        print(f"{'-' * 25}> Round {i+1}/{len(container) - 1} <{'-' * 25}")
        
        a = container[i]
        b = container[i + 1]
        
        checkErr = abs(b - a) / 2
        j = 0
        
        while checkErr > errAbs:
            m = (a + b) / 2
            fm = f(m)
            fa = f(a)
            
            print(f" [{a}, {b}], Midpoint = {m}, f(a) = {fa}, f(m) = {fm}")
            
            if fm * fa < 0:
                b = m
            else:
                a = m
            
            checkErr = abs(b - a) / 2
            j += 1
            
            print(f"Check Abs Error: {checkErr:.10f} \n")
            
            if j > 10000:
                print("Can't continue calculated!")
                checkErr = 0

        results.append(m)
        print(f"Root found [{container[i]}, {container[i+1]}]: {m}\n")
        print("-=-" * 25)
        
        i += 1
    
    return results

f = lambda x: x - math.tan(x)

errAbs = 0.000001

container = [2.6, 4.6]

roots = bisections_method(f, errAbs, container)
print("Roots found:", roots)
