# write your code here
string = input('Enter cells:')
x_count = string.count('X')
o_count = string.count('O')

entries = list(string)

a, b, c = entries[:3], entries[3:6], entries[6:]

print('---------')
print('|', entries[0], entries[1], entries[2], '|')
print('|', entries[3], entries[4], entries[5], '|')
print('|', entries[6], entries[7], entries[8], '|')
print('---------')

p = [a[0], b[0], c[0]]
q = [a[1], b[1], c[1]]
r = [a[2], b[2], c[2]]

test = list()


def solution():
    # checking diagonals
    if a[0] == b[1] == c[2] or a[2] == b[1] == c[0]:
        return f'{b[1]} wins'

    # impossible condition
    if abs(x_count - o_count) > 1:
        return 'Impossible'

    # checking rows
    for i in range(3):
        if p[i] == q[i] == r[i]:
            test.append(f'{p[i]} wins')

    # checking columns
    for i in range(3):
        if a[i] == b[i] == c[i]:
            test.append(f'{a[i]} wins')

    if len(test) > 1:
        return 'Impossible'
    elif len(test) == 1:
        return test[0]

    # checking draw
    if x_count + o_count == 9:
        return 'Draw'


p = solution()
if p is None:
    print('Game not finished')
else:
    print(p)
