def is_correctly_sorted(constraints, lst):
    position = {value: idx for idx, value in enumerate(lst)}

    for before, after in constraints:
        if before in position.keys() and after in position.keys() and  position[before] > position[after]:
          return False
    
    return True 
    
def fix_the_list(constraints, lst):
    if is_correctly_sorted(constraints, lst):
        return lst 

    position = {value: idx for idx, value in enumerate(lst)}

    for before, after in constraints:
        if before in position.keys() and after in position.keys() and position[before] > position[after]:
            lst[position[before]], lst[position[after]] = lst[position[after]], lst[position[before]] 
            return fix_the_list(constraints, lst) 

    