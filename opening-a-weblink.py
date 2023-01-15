# I'm not sure why the if elif statements arent working correctly
# maybe it is just the VSC codespace on github thats acting up
import time
import webbrowser
print('This is a test to open a link in the default web browser.')
second = 10
while True:
    print('Are you ready?')
    print('Y/N')
    ready = input()
    if ready == 'Y' or 'y':
        print('Excellent!')
        for seconds in range(11):
            print('Opening link in ' + str(second) + ' seconds...')
            second -= 1
            time.sleep(1)
            if second == 0:
                # link is to YouTube "Never Gonna Give You Up" by Rick Astley
                webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                break
    elif ready == 'N' or 'n':
        print('That was pretty sus')
        # link is to Among Us video of "Never Gonna Give You Up" by Rick Astley
        webbrowser.open('https://www.youtube.com/watch?v=WD16oVf5eGE')
        break
    else:
        print('Please enter a valid input')
        continue