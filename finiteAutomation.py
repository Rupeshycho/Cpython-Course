def check_even_odd(binary):
    state = "q0"
    
    for bit in binary:
        
        if bit == "1":
            if state == "q0":
                state = "q1"   # flip to odd
            else:
                state = "q0"   # flip back to even
        # if bit == "0": do nothing
    
    if state == "q0":
        return "Even number of 1s"
    else:
        return "Odd number of 1s"


binary = input("Enter the binary string: ")
result = check_even_odd(binary)
print(result)