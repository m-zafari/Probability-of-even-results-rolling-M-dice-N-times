# Mohammad Zafari
# mhdzafari80@gmial.com

import random, math

def dice(N, M):
    result = list()
    even_count = 0
    for i in range(M):
        temp_arry = list()
        odd_test = False
        for j in range(N):
            # rand_tas_value = math.floor(1 + 6 * random.uniform(0, 1))
            rand_dice_value = random.randint(1, 6)
            temp_arry.append(rand_dice_value)
            if rand_dice_value % 2 == 1:
                odd_test = True
        result.append(temp_arry)
        if not odd_test:
            even_count += 1 
    return result, even_count / M

#example
if __name__ == "__main__":
    reslt, even_prob = dice(10,  50)
    print(f"Even propability: {even_prob}")
    for ans in reslt:
        print(ans)
