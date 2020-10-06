board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}

player = 1          
total_moves = 0 
end_check = 0


def check():
    if board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X':
        print('Player one won !')
        return 1
    if board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
        print('Player One Won!!')
        return 1
    if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
        print('Player One Won!!')
        return 1
 
    if board['7'] == 'X' and board['5'] == 'X' and board['3'] == 'X':
        print('Player One Won!!')
        return 1
    if board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
        print('Player One Won!!')
        return 1
 
    if board['7'] == 'X' and board['4'] == 'X' and board['1'] == 'X':
        print('Player One Won!!')
        return 1
    if board['8'] == 'X' and board['5'] == 'X' and board['2'] == 'X':
        print('Player One Won!!')
        return 1
    if board['9'] == 'X' and board['6'] == 'X' and board['3'] == 'X':
        print('Player One Won!!')
        return 1
   
    if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
        print('Player Two Won!!')
        return 1  # used to end the game
    if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['7'] == 'O' and board['5'] == 'O' and board['3'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['7'] == 'O' and board['4'] == 'O' and board['1'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['8'] == 'O' and board['5'] == 'O' and board['2'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['9'] == 'O' and board['6'] == 'O' and board['3'] == 'O':
        print('Player Two Won!!')
        return 1
    return 0

print('-----')
print('7|8|9')
print('-----')
print('4|5|6')
print('-----')
print('1|2|3')
print('**********')

while True:
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:     
        if player == 1:  
            p1_input = input('PLAYER ONE :')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
          
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('PLAYER TWO :')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else: 
                print('Invalid input, please try again')
                continue
    total_moves += 1
    print('***************************')
    print()

