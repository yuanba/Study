def print_map(state,nums):    
    print("0 "*nums)
    for i in range(nums):
        print('. '*state[i] + 'X ' + '. '*(nums - 1 - state[i]))
    print("0 "*nums)

#(j,state[j]) - (len(state),i)
def confict(state,i):
    for j in range(len(state)):
        if abs(state[j] - i) in (0,len(state) - j):return True
    return False

def queens(step = 0,state = [],nums = 8):
    result = 0
    if step == nums :
        #raise Exception(state)
        print_map(state,nums)
        return 1
    judge = False
    for i in range(nums):
        if not confict(state,i):
            judge = True
            state.append(i)
            result += queens(step + 1,state,nums)
            del state[-1]
    return result

if __name__ == "__main__":
    print(queens(nums = 8))
