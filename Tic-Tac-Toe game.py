# Tic-Tac_Toe with numbers and any player have
# by:Abd-Elhamid Mahmoud Ahmed


# first draw the table and the lists
import copy


list1 = [0, 2, 4, 6, 8]
list2 = [1, 3, 5, 7, 9]
print(list1)
print(list2)
name_1 = str(input("enter the name how want to play with even list: "))
name_2 = str(input("enter the name how want to play with odd list: "))
print("the list of ", name_1, " is -->", list1)
print("the list of", name_2, " is -->", list2)
print("----------------------------------------------------------------------------------------------------------")
print("\\\\","--> the important rule of game <-- //")
print("**if any one enter number out of own list his turn will canceled and he will stay one round with out playing**")
print("if you entered the number of index was exist your turn well canceled")
print("--------------------------------------------------------------------------------------------------------------")
print("the index of table is: ")
print("[(1,1) , (1,2) , (1,3)]")
print("[(2,1) , (2,2) , (2,3)]")
print("[(3,1) , (3,2) , (3,3)]")
print("------------------------")


# the function to draw the tabel of game
def draw():
    """
to make the list of game
    """
    global game  # to make game shown in all program
    game = [['', '', ''], ['', '', ''], ['', '', '']]
    for i in game:
        print(i)


# this function to make player one to play
def player_1(index1, index2):
    """
    :param index1: for the index in first list or second or thread
    :param index2: for the index in the list what the user will choose in first time
    :return: True
    """

    print("the list of ", name_1, end='')
    print(list1)
    x = int(input("enter the number of list: "))

    if x not in list1:
        return print("try again in next time because you entered number out of your list!!")
        quit()

    list1.remove(x)

    game[index1 - 1][index2 - 1] = x

    for x in game:  # to enter the number in game list by user
        print(x)


# this function to make player 2 play
def player_2(index3, index4):
    """
    :param index3: for the index in first list or second or thread
    :param index4:for the index in the list what the user will choose in first time
    :return:
    """

    print("the list of ", name_2 , end='')
    print(list2)
    y = int(input("enter the number of list:"))
    if y not in list2:
        return print("try again in next time because you entered number out of your list!!")
        quit()

    list2.remove(y)

    game[index3 - 1][index4 - 1] = y

    for y in game:
        print(y)


# function to check if any player is win in this game
def test():

    game_check = copy.deepcopy(game)        # make list of the main list to check the next steps was true of not
    for idx, i in enumerate(game_check):    # because when the computer make any empty place in lists = 16, I want to \
        for idx2, j in enumerate(i):        # change in the another list not the main list it's could game
            if j == '':
                game_check[idx][idx2] = 16      # to make any empty index stored by integer


    if game_check[0][0] + game_check[0][1] + game_check[0][2] == 15 or\
            game_check[1][0] + game_check[1][1] + game_check[1][2] == 15 or\
            game_check[2][0] + game_check[2][1] + game_check[2][2] == 15 or\
             game_check[0][0] + game_check[1][0] + game_check[2][0] == 15 or\
            game_check[0][1] + game_check[1][1] + game_check[2][1] == 15 or\
             game_check[0][2] + game_check[1][2] + game_check[2][2] == 15 or\
            game_check[0][0] + game_check[1][1] + game_check[2][2] == 15 or\
            game_check[0][2] + game_check[1][1] + game_check[2][0] == 15:
        return True
    

#function to check if the index was empty or not
def check_index_for_player1() :
    """
    :return: True if the index was empty
    """

    if game [index1-1][index2 - 1] == '':
        return True

    else:
        return False


#this function to check if the index user input was empty or not
def check_index_for_player2():
    """
    :return: True if the index was empty
    """

    if game[index3 - 1][index4 - 1] == '':
        return True
    else:
         return False

def no_one_is_win():
    
    for idx, i in enumerate(game):    
        for idx2, j in enumerate(i):       
            if j == '':
                return False
    return True


def check_if_input_is_intger_of_first_player(index, indexx):
    try:
        int(index)
        int(indexx)
        return True
    except :
        return False


# this lines to start the game
draw()


while True:
    print(name_1, " play please and enter the numbers of index : ")
    index1 = input("enter the number of the first index 1:3--> ")
    index2 = input("enter the number of the second index 1:3--> ")

    while not check_if_input_is_intger_of_first_player(index1,index2):
        index1 = input("please don't enter leter and enter number btween 1:3--> ")
        index2 = input("please don't enter leter and enter number btween 1:3--> ")

    index1 = int(index1)
    index2 = int(index2)
    

    if 1 <= index1 <= 3 and 1 <= index2 <= 3 and  check_index_for_player1() :
        player_1(index1, index2)
    else:
        print(name_1, " please try in the next time and enter the number between 1 : 3 please!!")
        print("this round for ", name_1)


    if test() :  # to check who was won
        print(name_1, " is winner!")
        print("hard luck for ", name_2, " and try again in the next time")
        break

    print(name_2, "play please and enter the numbers of index --> ")
    index3 = input("enter the number of the first index 1:3--> ")
    index4 = input("enter the number of he second index 1:3--> ")

    while not check_if_input_is_intger_of_first_player(index3,index4):
        index3 = input("please don't enter leter and enter number btween 1:3--> ")
        index4 = input("please don't enter leter and enter number btween 1:3--> ")
    index3 = int(index3)
    index4 = int(index4)


    if 1 <= index3 <= 3 and 1 <= index4 <= 3 and check_index_for_player2():
        player_2(index3, index4)
    else:
        print(name_2, "please try in the next time and enter the number between 1 : 3 please!!")
        print("this round for ", name_1)

    if test():   # to check how was won
        print(name_2, " is winner")
        print("hard luck for ", name_1, " and try again in the next time")
        break

    
    if no_one_is_win():
        print("The game is end and no one if won please try agian in later time")
        break

