import itertools
import decimal
import math

def is_ascending(items):
    result = all( i < j for i, j in zip(items, items[1:]))
    return(str(result))




def riffle(items, out=False):
        middle_index = len(items) // 2
        first_half = items[:middle_index]               # 1 2 3 4
        second_half = items[middle_index:]              # 5 6 7 8
        if (out):
                result = [*sum(zip(first_half, second_half), ())]
        else:
                result = [*sum(zip(second_half, first_half), ())]
        return(result)
                        




def only_odd_digits(n):
       return set(str(n)) - set('13579') == set()




def is_cyclops(n):
        str_converted = str(n)        

        if(len(str_converted) % 2 == 0):
                return False
        else:
                middle_index = len(str_converted) // 2
                if str_converted[middle_index] != "0": return False 
                if str_converted.count("0") > 1: return False  
                return True






def domino_cycle(tiles):
        x = 0
        if len(tiles) == 0:
                return True
        if len(tiles) == 1:
                return tiles[0][0] == tiles [0][1]      
        else:
                while x <= (len(tiles) - 2):
                        if (tiles[x][1] == tiles[x + 1][0]):
                                x += 1
                        else:
                                return False
                if tiles[0][0] == tiles[-1][1]:
                        return True
                else:
                        return False





def count_dominators(items):
    dominators = 0
    for index,item in enumerate(items):
        dominator = True
        for right_item in items[index + 1:]:
            if item <= right_item:
                dominator = False
                break
        if dominator:
            dominators = dominators + 1        
    return dominators





def pancake_scramble(text):
        for i in range(1, len(text)):
                text = text[i::-1] + text[(i + 1) ::]
        return text





def taxi_zum_zum(moves):
    directions = ['N','E','S','W']      
    dir = 0                           

    x = 0
    y = 0
    for i in moves:
        if i == 'L':
            dir -= 1
            if dir < 0:
                dir = 3
        elif i== 'R':
            dir += 1
            if dir > 3:
                dir = 0
        elif i == 'F':
            if directions[dir]=='N':
                y += 1 
            elif directions[dir]=='S':
                y -= 1 
            elif directions[dir]=='E':
                x += 1 
            elif directions[dir]=='W':
                x -= 1 
    return (x,y)




def is_left_handed(pips):
        left_hand_combos = [[1,2,3], [2,3,1], [3,1,2], [1,4,2], [2,1,4], [4,2,1], [1,3,5], [3,5,1], [5,1,3], [1,5,4], [4,1,5], [5,4,1], [2,6,3], [3,2,6], [6,3,2], [2,4,6], [4,6,2], [6,2,4], [3,6,5], [5,3,6], [6,5,3], [4,5,6], [5,6,4], [6,4,5]]
        pips_list = []
        for i in pips:
                pips_list.append(i)
        if pips_list[:] in left_hand_combos[:]:
                return True
        else:
                return False







def give_change(amount, coins):
        result = []
        return give_change_memoization(amount, coins, result)

def give_change_memoization(amount, coins, result):
        if amount == 0:
                return result
        while len(coins) > 0 and amount >= coins[0]:
                amount = amount - coins[0]
                result.append(coins[0])
        if len(coins) > 0:
                coins = coins[1:]
        else:
                return result
        return give_change_memoization(amount, coins, result)








def count_carries(a, b):
    a = str(a)
    b = str(b)
    carry = 0;
    count = 0;
    len_a = len(a);
    len_b = len(b);
 
    while (len_a != 0 or len_b != 0):
        x = 0;
        y = 0;
        if (len_a > 0):
            x = int(a[len_a - 1]) + int('0');
            len_a -= 1;
         
        if (len_b > 0):
            y = int(b[len_b - 1]) + int('0');
            len_b -= 1;

        sum = x + y + carry;
        if (sum >= 10):
            carry = 1;
            count += 1;
        else:
            carry = 0;
    return count;





def pyramid_block(n, m, h):
        a = 0
        for index in range(h):
                a = a + (n * m)
                n = n + 1
                m = m + 1
        return a





    
def reverse_vowels(text):
        vowels = ''
        for char in text:
                if char in "aeiouAEIOU":
                        vowels += char
        string = ""
        for char in text:
                if char in "aeiouAEIOU":
                        if char.isupper()==True:
                                string += str(vowels[-1].upper())
                                vowels = vowels[:-1]
                        else:
                                string += str(vowels[-1].lower())
                                vowels = vowels[:-1]
                else:
                        string += char
        return string







def knight_jump(knight, start, end):
        result = []
        for i in range(0, len(start)):
                result.append(abs(start[i] - end[i]))
        if set(knight) == set(result):
                return True
        return False








def fibonacci_word( k ):
    decimal.getcontext().prec = 165
    root_5 = decimal.Decimal( 5 ).sqrt()
    phi = ( 1 + root_5 ) / 2
    r = phi / ( 1 + ( phi * 2 ) )

    return math.floor(  ( k + 2 ) * r ) - math.floor( ( k + 1 ) * r )







def count_consecutive_summers(n):
        if n <= 2:
                return 1
        count = 0
        if (n % 2) == 1:
                count += 1
                
        if (n // 2) % 2 == 1:
                m = n // 2
        else: 
                m = (n // 2) - 1
        while m > 1:
                if (n / m) == int(n / m):
                        count += 1
                m -= 2
        return count + 1



  
 
























































































# import itertools

#         #### COMPLETE #####   1 / 55
# def is_ascending(items):
    
#     result = all( i < j for i, j in zip(items, items[1:]))
#     return(str(result))
#         #### COMPLETE #####
# # -------------------------------------------------------------------------------------------------------------------------#

#         #### COMPLETE #####   2 / 55
# def riffle(items, out=False):
#         middle_index = len(items) // 2
#         first_half = items[:middle_index]               # 1 2 3 4
#         second_half = items[middle_index:]              # 5 6 7 8
#         if (out):
#                 result = [*sum(zip(first_half, second_half), ())]
#         else:
#                 result = [*sum(zip(second_half, first_half), ())]
#         return(result)
# # -------------------------------------------------------------------------------------------------------------------------#
                        
#         #### COMPLETE #####   3 / 55
# def only_odd_digits(n):
#        return set(str(n)) - set('13579') == set()
# # -------------------------------------------------------------------------------------------------------------------------#

#         #### COMPLETE #####    4 / 55
# def is_cyclops(n):
#         str_converted = str(n)        

#         if(len(str_converted) % 2 == 0):
#                 return False
#         else:
#                 middle_index = len(str_converted) // 2
#                 if str_converted[middle_index] != "0": return False # check if middle number is zero
#                 if str_converted.count("0") > 1: return False  # No Zeros
#                 return True
# # -------------------------------------------------------------------------------------------------------------------------#

#         #### COMPLETE #####    5 / 55
# tiles2 = [(3, 5), (5, 2), (2, 3)]
# tiles = [(1, 3), (3, 2), (2, 5), (5, 2), (2, 1)]
# def domino_cycle(tiles):
#         x = 0
#         # print(len(tiles) -2)
#         if len(tiles) == 0:
#                 return True
#         if len(tiles) == 1:
#                 return tiles[0][0] == tiles [0][1]      
#         else:
#                 while x <= (len(tiles) - 2):
#                         if (tiles[x][1] == tiles[x + 1][0]):
#                                 x += 1
#                         else:
#                                 return False
#                 if tiles[0][0] == tiles[-1][1]:
#                         return True
#                 else:
#                         return False
# # -------------------------------------------------------------------------------------------------------------------------#

#         #### COMPLETE #####    6 / 55
# def count_dominators(items):
#     dominators = 0
#     for index,item in enumerate(items):
#         dominator = True
#         for right_item in items[index + 1:]:
#             if item <= right_item:
#                 dominator = False
#                 break
#         if dominator:
#             dominators = dominators + 1        
#     return dominators
# # Runs in 310 seconds in VScode which would run in under 300 seconds locally or in replit likely
# count_dominators([42, 7, 12, 9, 2, 5])
# # -------------------------------------------------------------------------------------------------------------------------#

# def pancake_scramble(text):
#         for i in range(1, len(text)):
#                 text = text[i::-1] + text[(i + 1) ::]
#         return text
# # -------------------------------------------------------------------------------------------------------------------------#

#         #### COMPLETE #####    7 / 55
# def taxi_zum_zum(moves):
#     directions = ['N','E','S','W']      
#     dir = 0                           

#     x = 0
#     y = 0
#     for i in moves:
#         if i == 'L':
#             dir -= 1
#             if dir < 0:
#                 dir = 3
#         elif i== 'R':
#             dir += 1
#             if dir > 3:
#                 dir = 0
#         elif i == 'F':
#             if directions[dir]=='N':
#                 y += 1 #going up/north
#             elif directions[dir]=='S':
#                 y -= 1 #going down/south
#             elif directions[dir]=='E':
#                 x += 1 #going east/right
#             elif directions[dir]=='W':
#                 x -= 1 #going west/left
#     return (x,y)

# # -------------------------------------------------------------------------------------------------------------------------#

#        ##### COMPLETE ##### (0.064s VSCode)
# def is_left_handed(pips):
#         left_hand_combos = [[1,2,3], [2,3,1], [3,1,2], [1,4,2], [2,1,4], [4,2,1], [1,3,5], [3,5,1], [5,1,3], [1,5,4], [4,1,5], [5,4,1], [2,6,3], [3,2,6], [6,3,2], [2,4,6], [4,6,2], [6,2,4], [3,6,5], [5,3,6], [6,5,3], [4,5,6], [5,6,4], [6,4,5]]
#         pips_list = []
#         for i in pips:
#                 pips_list.append(i)
#         if pips_list[:] in left_hand_combos[:]:
#                 return True
#         else:
#                 return False

# is_left_handed((5, 4, 1))

# # -------------------------------------------------------------------------------------------------------------------------#


# #### COMPLETE But look at another way of doing it later #####  8 / 55
# def give_change(amount, coins):
#         result = []
#         return give_change_memoization(amount, coins, result)

# def give_change_memoization(amount, coins, result):
#         if amount == 0:
#                 return result
#         while len(coins) > 0 and amount >= coins[0]:
#                 amount = amount - coins[0]
#                 result.append(coins[0])
#         if len(coins) > 0:
#                 coins = coins[1:]
#         else:
#                 return result
#         return give_change_memoization(amount, coins, result)

# # give_change(64, [50, 25, 10, 5, 1])
# # -------------------------------------------------------------------------------------------------------------------------#

#         #### COMPLETE #####  (0.1666 seconds)
# def count_carries(a, b):
#     a = str(a)
#     b = str(b)
#     carry = 0;
#     count = 0;
#     len_a = len(a);
#     len_b = len(b);
 
#     while (len_a != 0 or len_b != 0):
#         x = 0;
#         y = 0;
#         if (len_a > 0):
#             x = int(a[len_a - 1]) + int('0');
#             len_a -= 1;
         
#         if (len_b > 0):
#             y = int(b[len_b - 1]) + int('0');
#             len_b -= 1;

#         sum = x + y + carry;
#         if (sum >= 10):
#             carry = 1;
#             count += 1;
#         else:
#             carry = 0;
#     return count;
# # print(count_carries(9555,555))
# #--------------------------------------------------------------------------------------------------------------------#
        
#         #### COMPLETE #####    (0.538s)
# def reverse_vowels(text):
#         vowels = ''
#         for char in text:
#                 if char in "aeiouAEIOU":
#                         vowels += char
#         string = ""
#         for char in text:
#                 if char in "aeiouAEIOU":
#                         if char.isupper()==True:
#                                 string += str(vowels[-1].upper())
#                                 vowels = vowels[:-1]
#                         else:
#                                 string += str(vowels[-1].lower())
#                                 vowels = vowels[:-1]
#                 else:
#                         string += char
#         return string
# # -------------------------------------------------------------------------------------------------------------------------#

#         #### COMPLETE #####    (0.653s)
# def knight_jump(knight, start, end):
#         result = []
#         for i in range(0, len(start)):
#                 result.append(abs(start[i] - end[i]))
#         if set(knight) == set(result):
#                 return True
#         return False
# # -------------------------------------------------------------------------------------------------------------------------#

# import decimal
# import math

#         ##### COMPLETE #####
# def fibonacci_word( k ):
#     decimal.getcontext().prec = 165
#     root_5 = decimal.Decimal( 5 ).sqrt()
#     phi = ( 1 + root_5 ) / 2
#     r = phi / ( 1 + ( phi * 2 ) )

#     return math.floor(  ( k + 2 ) * r ) - math.floor( ( k + 1 ) * r )

# #-------------------------------------------------------------------------------------------------------------------------#

#         ##### COMPLETE #####
# def count_consecutive_summers(n):
#         if n <= 2:
#                 return 1
#         count = 0
#         if (n % 2) == 1:
#                 count += 1
                
#         if (n // 2) % 2 == 1:
#                 m = n // 2
#         else: 
#                 m = (n // 2) - 1
#         while m > 1:
#                 if (n / m) == int(n / m):
#                         count += 1
#                 m -= 2
#         return count + 1



# #-------------------------------------------------------------------------------------------------------------------------#

#   # Takes forever up to 400 something seconds, try and fix
#         ##### COMPLETE but not complete #####
# def eliminate_neighbours(items):

#         maximum = max(items)
#         counter = 0

#         if len(items) == 1:
#                 return 1

#         for i in range(len(items)):
#                 if maximum in items:
#                         i = min(items)
#                         if len(items) == 1:
#                                 if items[0] == maximum:
#                                         counter += 1
#                                         break
#                                 else:
#                                         break
#                         elif len(items) == 2:
#                                 counter += 1
#                                 break
#                         elif items.index(i) == 0:
#                                 items.remove(items[items.index(i) + 1])
#                                 counter += 1
#                         elif items.index(i) == len(items) - 1:
#                                 items.remove(items[items.index(i) - 1])
#                                 counter += 1
#                         else:
#                                 a = items[items.index(i) + 1]
#                                 b = items[items.index(i) - 1]
#                                 if a > b:
#                                         items.remove(a)
#                                         counter += 1
#                                 else:
#                                         items.remove(b)
#                                         counter += 1
#                         items.remove(i)
#         return counter





#   # same taking a forever time to complete. 
# def sum_of_two_squares(n) :
#         i = 1
#         while i * i <= n :
#                 j = 1
#                 while(j * j <= n) :
                
#                         if (i * i + j * j == n) :
                                
#                                 if i > j:        
#                                         return (i, j)
#                                 else:
#                                         return (j, i)
#                         j += 1
#                 i += 1
         
#         return None
  
# sum_of_two_squares(85)




# def prime_factors(n):
#         i = 2
#         factors = []
#         while i * i <= n:
#                 if n % i:
#                         i += 1
#                 else:
#                         n //= factors.append(i)
#         if n > 1:
#                 factors.append(n)
#         return factors
                
# def balanced_centrifuge(n,k):
#         k1 = n - k
#         if k == 1:
#                 return False
#         factors = prime_factors(n)
#         for factor in factors:
#                 if (k % factor == 0 or k % factor in factors) or (k1 % factor == 0 or k1 % factor in factors):
#                         return True
#         return False




