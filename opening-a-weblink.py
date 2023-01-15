import time #using time to add a little flair
import webbrowser #using webbrowser to open two different links to youtube
print('This is a test to open a link in the default web browser.')
second = 10
while True:
    print('Are you ready?')
    print('Y/N')
    ready = input().lower() # using '.lower()' helped to keep the code from breaking if an uppercase input is used by modifying any input to lowercase
    if ready == 'y':
        print('Excellent!')
        for seconds in range(11): #using the time.sleep with the loop to add a little flair with a countdown to opening the link
            print('Opening link in ' + str(second) + ' seconds...')
            second -= 1
            time.sleep(1)
            if second == 0:
                # link is to YouTube "Never Gonna Give You Up" by Rick Astley
                webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                second = 10
                break
    elif ready == 'n':
        print('That was pretty sus')
        time.sleep(2)
        # link is to Among Us video of "Never Gonna Give You Up" by Rick Astley
        webbrowser.open('https://www.youtube.com/watch?v=WD16oVf5eGE')
        break
    else:
        print('Please enter a valid input')
        continue # restarts the loop so the program does not end while accounting for unexpected inputs
