number = 23
running = True
# 1. while and if...elif...else
while running:
    guess = int(input('Enter an integer :'))
    if guess == number:
        print('You guessed it.')
        running = False
    elif guess < number:
        print('Too big!')
    else:
        print('Too small')

print('Done')

# 2. for...in
for i in range(1,5):
    print(i)
else:
    print('else is optional, it always run after end of for circle \
    except there is a break within for circle \
    or there is an exception throw from for circle')

# 3. break
while True:
    cmd = input('Enter "quit" cmd: ')
    if cmd == 'quit':
        break
    if cmd == 'hello':
        print(cmd)
        continue
    print('new circle begin!')
