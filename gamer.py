print('Hello, welcome to true talk')
ans = input('Are you ready to play ? (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. What is the best programming language ? ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('2. What is 1 + 2 + 3 + 4 ? ')
    if ans == '10':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('3. What is my age ? ')
    if ans == '23':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('4. What is the approximate value of PI ')
    if ans == '3.142':
        score += 1
        print('Correct')
    else:
        print('Wrong')

    ans = input('5. Where do I stay ? ')
    if ans.lower() == 'sinchu' or ans.lower() == 'Sinchu alagi':
        score += 1
        print('Correct')
    else:
        print('Wrong')

    print('Thank your for playing, you got', score, 'questions correct')
    mark = (score/total_q) * 100
    print('Mark: ', mark)
print('GoodBye')
