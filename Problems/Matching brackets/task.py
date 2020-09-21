# put your python code here
br = []
inp = input()
for char in inp:
    if char == '(' or char == ')':
        br.append(char)
nah = False
while br:
    current = br.pop()
    if current != ')':
        nah = True
        print('ERROR')
        break
    else:
        try:
            br.pop(br.index('('))
        except ValueError:
            nah = True
            print('ERROR')
            break
if not nah:
    print('OK')


