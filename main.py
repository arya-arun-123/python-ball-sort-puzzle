

max_capacity = 4                                # maximum balls allowed in a tube

tubes = [                                       # initial tube status
    ['Y','B','G','R'],
    ['B','Y','R','G'],
    ['G','R','Y','B'],
    ['R','G','B','Y'],
    []
]


def display_tubes():
    print('\n Current State:\n')

    for i, tube in enumerate(tubes):                # display each tube with tube number
        print(f"Tube {i+1}: {tube}")



def valid_move(source,destination):

    if source == destination:  # movement from same tube
        return False

    if len(tubes[source]) == 0:     # empty source
        return False
    
    if len(tubes[destination]) >= max_capacity:     # destination overflow
        return False
    

    if len(tubes[destination]) == 0:        # empty destination
        return True
    
    moving_ball = tubes[source][-1]         # top ball of source to be moved
    top_ball = tubes[destination][-1]       # top ball of destination

                            
    if top_ball == moving_ball:             # same balls then can be inserted
        return True
    

    return False



def move_ball(source,destination):

    if valid_move(source,destination):
        ball = tubes[source].pop()          # pop the top ball from source
        tubes[destination].append(ball)     # append the popped ball to destination tube
        print(f"\n Moved {ball} from Tube {source+1} to Tube {destination+1} ")

    else:
        print("\n Invalid Move!!!")



def check_win():
    for tube in tubes:
        if len(tube) == 0:                   # empty tube is allowed
            continue
        if len(tube) != max_capacity:        # tube must be completely filled
            return False
        if len(set(tube)) != 1:              # tube contains all balls of same color
            return False
    return True                              # all tubes obeys winning condition



while True:

    display_tubes()

    if check_win():
        print("\n YOU WIN !!!!!!!")
        break
    try:
        source = int(input("\n Enter source tube:")) - 1               # to take the source from which ball is to be moved
        destination = int(input("\n Enter destination tube:")) - 1     # to take destination column to which ball is needed to be added

        if not (0 <= source < len(tubes)):                             # validate source tube index
            print("\nInvalid source tube!")
            continue

        if not (0 <= destination < len(tubes)):                        # validate destination tube index
            print("\nInvalid destination tube!")
            continue


        move_ball(source,destination)

    except:
        print("Invalid Input")
