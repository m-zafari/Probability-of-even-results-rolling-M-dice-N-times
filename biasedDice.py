# Mohammad Zafari
# mhdzafari80@gmial.com

import random, math
def b_dice(N,M, probDice):
    result = list()
    even_count = 0
    for i in range(M):
        temp_arry = list()
        odd_test = False
        for j in range(N):
            rand_dice_value = None
            rand_definder = random.uniform(0, 1)

            if rand_definder < probDice[0]:
                rand_dice_value = 1
                odd_test = True

            elif rand_definder < sum(probDice[:2]):
                rand_dice_value = 2

            elif rand_definder < sum(probDice[:3]):
                rand_dice_value = 3

                odd_test = True
            elif rand_definder < sum(probDice[:4]):
                rand_dice_value = 4

            elif rand_definder < sum(probDice[:5]):
                rand_dice_value = 5
 
                odd_test = True
            else: # rand_definder <= 100 / 100:
                rand_dice_value = 6

            temp_arry.append(rand_dice_value)
        result.append(temp_arry)
        if not odd_test:
            even_count += 1 
    return result, even_count / M

#example
if __name__ == "__main__":
    #dice number     1     2     3     4     5     6
    prob_dice_num = [0.05, 0.15, 0.30, 0.30, 0.15, 0.06 ]
    reslt, even_prob = b_dice(3,  5, prob_dice_num)
    print(f"Even propability: {even_prob}")
    for ans in reslt:
        print(ans)
