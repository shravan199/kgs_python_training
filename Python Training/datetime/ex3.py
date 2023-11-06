print('Start hacking.......')

import random
import time

total_perc = 0
for num in range(1, 101):
    rand_int = random.randint(1, num)
    total_perc += rand_int
    if total_perc <=99:
        print(f'Hacking NASA {total_perc}%')
        time.sleep(2)
    else:
        print(f'Hacking NASA 100%')
        print('NASA hacked successfully')
        break

        
