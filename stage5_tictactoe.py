def show_matrix(state):
    entries = list(state)
    print('---------')
    print('|', entries[0], entries[1], entries[2], '|')
    print('|', entries[3], entries[4], entries[5], '|')
    print('|', entries[6], entries[7], entries[8], '|')
    print('---------')

def solution(state):
    '''Check for solution.
    Cool Docstring.'''
    x_count = state.count('X')
    o_count = state.count('O')

    matrix = list(state)

    a, b, c = matrix[:3], matrix[3:6], matrix[6:]

    p = [a[0], b[0], c[0]]
    q = [a[1], b[1], c[1]]
    r = [a[2], b[2], c[2]]

    test = list()
   
    # checking diagonals
    if a[0] == b[1] == c[2] or a[2] == b[1] == c[0]:
        return f'{b[1]} wins'

    # impossible condition
    '''if abs(x_count - o_count) > 1:
        return 'Impossible'
    '''
    
    # checking rows
    for i in range(3):
        if p[i] == q[i] == r[i]:
            test.append(f'{p[i]} wins')

    # checking columns
    for i in range(3):
        if a[i] == b[i] == c[i]:
            test.append(f'{a[i]} wins')

    '''
    if len(test) > 1:
        return 'Impossible'
    elif len(test) == 1:
        return test[0]
    
    # checking draw
    if x_count + o_count == 9:
        return 'Draw'

    return 'Game not finished'
    '''


def add_coordinates(coords, state):
    global turn
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
    matrix = list(state)

    a, b, c = matrix[:3], matrix[3:6], matrix[6:]

    nested_state = [c, b, a]
    
    if nested_state[coords[1] - 1][coords[0] - 1] in ('X', 'O'):
        return 'This cell is occupied! Choose another one!'
    else:
        nested_state[coords[1] - 1][coords[0] - 1] = turn
    c, b, a = nested_state
    matrix[:3], matrix[3:6], matrix[6:] = a, b, c
    state = ''.join(matrix)
    return state


string = ' ' * 9
turn = 'O'

show_matrix(string)

while True:
    while True:
        try:
            coordinates = [int(x) for x in input('Enter the coordinates: ').split()]
        except ValueError:
                print('You should enter numbers!')
        else:
            if coordinates[0] > 0 and coordinates[0] < 4:
                if coordinates[1] > 0 and coordinates[1] < 4:
                    break
                else:
                    print('Coordinates should be from 1 to 3!')
            else:
                print('Coordinates should be from 1 to 3!')

    string = add_coordinates(coordinates, string)

    while string == 'This cell is occupied! Choose another one!':
        print('This cell is occupied! Choose another one!')
        while True:
            try:
                coordinates = [int(x) for x in input('Enter the coordinates: ').split()]
            except ValueError:
                print('You should enter numbers!')
            else:
                if coordinates[0] > 0 and coordinates[0] < 4:
                    if coordinates[1] > 0 and coordinates[1] < 4:
                        break
                    else:
                        print('Coordinates should be from 1 to 3!')
                else:
                    print('Coordinates should be from 1 to 3!')
        string = add_coordinates(coordinates, string)
    show_matrix(string)
    sol = solution(string)
    if sol == 'X wins':
        print(sol)
        break
    elif sol == 'O wins':
        print(sol)
        break
    elif sol == 'Draw':
        print(sol)
        break
