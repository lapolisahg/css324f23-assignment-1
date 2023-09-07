def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] ==4
    

def successors(s):
    x, y, z = s
    successors_states = []
    # Rules for pouring water between bottles
    # 1. Pour x to y
    if x > 0 and y < 5:
        amount_to_pour = min(x, 5-y)
        new_state = (x-amount_to_pour, y+amount_to_pour,z)
        successors_states.append((new_state,amount_to_pour))
    # 2. Pour x to z 
    if x > 0 and z < 3:
        amount_to_pour = min(x,3-z)
        new_state = (x-amount_to_pour,y,z+amount_to_pour)
        successors_states.append ((new_state,amount_to_pour))
    # 3. Pour y to x
    if y > 0 and x < 8:
        amount_to_pour = min(y,8-x)
        new_state = (x+amount_to_pour, y-amount_to_pour,z)
        successors_states.append ((new_state,amount_to_pour))
    # 4. Pour y to z
    if y > 0 and z < 3:
        amount_to_pour = min(y,3-z)
        new_state = (x, y-amount_to_pour,z+amount_to_pour)
        successors_states.append ((new_state,amount_to_pour))
    # 5. Pour z to x
    if z > 0 and x < 8:
        amount_to_pour = min(z,8-x)
        new_state = (x+amount_to_pour, y,z-amount_to_pour)
        successors_states.append ((new_state,amount_to_pour))
    # 6. Pour z to y
    if z > 0 and y < 5:
        amount_to_pour = min(z,5-y)
        new_state = (z,y+amount_to_pour,z-amount_to_pour)
        successors_states.append ((new_state,amount_to_pour))
    return successors_states
