import time
total = 0
#Pre-Alpha 1.0.0
#        con,lab,lib
polls = [[40,50,10],
        [30,20,50],
        [39,41,20],
        [38,45,40],
        [40,30,30],
        [19,41,40],
        [41,20,39]]


def validate_polls():
    total = 0
    for i in range (0, 6):
        for t in range (0, 2):
            total = total + polls[i][t]
        while total > 100:#makes each seat have 100 votes
            if polls[i][0] > polls[i][1] and polls[i][0] > polls[i][2]:
                polls[i][0] = polls[i][0] - 1
            elif polls[i][1] > polls[i][0] and polls[i][1] > polls[i][2]:
                polls[i][1] = polls[i][1] - 1
            else:
                polls[i][2] = polls[i][2] - 1
            total = total - 1


validate_polls()



def check(output, a, b):
    ans = input(output)
    is_valid = ans.isdigit()
    # while input is not a number
    
    while not is_valid:
        # get another input
        print('Please enter an integer')
        ans = input('__')
        is_valid = ans.isdigit()
        while ans < a or ans > b:
            print(f"Make sure to enter a number between {a} and {b}")

    ans = int(ans)
    return ans

def UkPinc():
    print("Welcome to Uk Politics Pre-Alpha")
    print("Please select a party:")
    ans = check("1. Conservative 2. Labour 3. Liberal Democrats", 1, 3)
    #if ans == 1:
        

UkPinc()