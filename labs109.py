import itertools


#         #### COMPLETE #####   1 / 55
# def is_ascending(items):
#     print("List Items : " + str(items))
#     result = all( i < j for i, j in zip(items, items[1:]))
#     return(str(result))
#         #### COMPLETE #####

# -------------------------------------------------------------------------------------------------------------------------#

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
       
# -------------------------------------------------------------------------------------------------------------------------#
                        
#         #### COMPLETE #####   3 / 55
# def only_odd_digits(n):
#        return set(str(n)) - set('13579') == set()
#         #### COMPLETE #####  

# -------------------------------------------------------------------------------------------------------------------------#

        ##### COMPLETE #####    4 / 55
# Cyclops Numbers
# def is_cyclops(n):
#         str_converted = str(n)        

#         if(len(str_converted) % 2 == 0):
#                 return False
#         else:
#                 middle_index = len(str_converted) // 2
#                 if str_converted[middle_index] != "0": return False # check if middle number is zero
#                 if str_converted.count("0") > 1: return False  # No Zeros
#                 return True

# -------------------------------------------------------------------------------------------------------------------------#

        ##### COMPLETE #####    5 / 55
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


# -------------------------------------------------------------------------------------------------------------------------#

        ##### COMPLETE #####    6 / 55
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
# Runs in 1.572 seconds in replit
# count_dominators([42, 7, 12, 9, 2, 5])

# -------------------------------------------------------------------------------------------------------------------------#

        #####  #####
# def extract_increasing(digits):
#         current = 0
#         previous = -1
#         result = []
#         # d is  0 4 5 3 4 9
#         for d in digits:
#                 current = d
#                 # print(current)
#                 current = 10 * current + d
#                 print(current)
#         print()
#         # return digits[0] + result

# extract_increasing('045349')

# -------------------------------------------------------------------------------------------------------------------------#

# wordlist = open("words_sorted.txt", "r")
# words = ['booklores', 'folklore','kilocurie', 'kilogramme', 'kilogrammetre', 'kilolitre', 'bronchiectatic', 'bronchiogenic' ]



# def words_with_letters(words, letters):
#         letters = set()
#         result = []
#         for word in words:
#                 word_set = {word}
#                 # print(word_set)
#                 if letters.issubset(word_set):
#                         print("trueeeee")
                

#                 for k in word:
#                         if k in letters:
#                                 print(k)
                        
        
        

  



# words_with_letters(words, letters='klore')


# -------------------------------------------------------------------------------------------------------------------------#

        ##### COMPLETE #####    7 / 55
# def taxi_zum_zum(moves):
#     
#     directions = ['N','E','S','W']    #creating a list of directions    
#     dir = 0                           # dir points the current index of directions

#     #current position
#     x = 0
#     y = 0

#     #looping through each character in moves
#     for i in moves:
#         #if character is L, turning left
#         if i == 'L':
#             #decrementing dir
#             dir -= 1
#             #if dir goes below 0, starting from other side
#             if dir < 0:
#                 dir = 3
#         elif i== 'R':
#             #doing the same for turning right
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
#     #returning a tuple containing final position
#     return (x,y)

# -------------------------------------------------------------------------------------------------------------------------#


        ##### COMPLETE But look at another way of doing it later #####  8 / 55
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

# give_change(64, [50, 25, 10, 5, 1])

# -------------------------------------------------------------------------------------------------------------------------#



# def is_left_handed(pips):
#         left_hand_combos = [(1,2,3)]
#         right_hand_combos = []
#         result = []
#         for i in pips:
#                 result.append(i)
#         print(result)

# is_left_handed((1, 2, 3))




# -------------------------------------------------------------------------------------------------------------------------#

# def winning_card(cards, trump=None):
        # 4 players each play one card from their hand to the trick
        # Committing to their play in clockwise order starting from player who first plays into the trick
        # Winner is determined by the following
        #         If one or more of the cards of the trump suit have been played to the trick, the trick is won by the highest ranking trump card, regardless of the other cards played
        #         If no trump card have been played to the trick, the trick is won by the highest card of the suit of the first card played to the trick. Cards of any other suits regardless of rank, are powerless to win that trick
        

# def winning_card(cards, trump=None):
#         trump_card = False
#         cards_list = []
#         suits = ['hearts', "diamonds", "spades", "clubs"]
#         # Four players of the game
#         for tuple in cards:
#                 cards_list.append(tuple)  

#         print(cards_list)                    

# winning_card([('three', 'spades'), ('ace', 'diamonds'), ('jack', 'spades'), ('eight', 'spades')], trump=None)



# -------------------------------------------------------------------------------------------------------------------------#


        ##### Complete #####
# def pancake_scramble(text):
#         for i in range(1, len(text)):
#                 text = text[i::-1] + text[(i + 1) ::]
#         return text




# -------------------------------------------------------------------------------------------------------------------------#



#                 # rows = 3 cols = 5
# def create_zigzag(rows, cols, start=1):
#         rows = 3
#         cols = 5
#         grid = rows * cols
#         a = [[rows] * cols for i in range(rows)]
#         for row in a:
#                 for elem in row:
#                         print(elem)


       

#         # print(a)
# create_zigzag(3,5, start=1)

# To process 2-dimensional array, you typically use nested loops. The first loop iterates through the row number, the second loop runs through the elements inside of a row.

# -------------------------------------------------------------------------------------------------------------------------#
# import math


        ### Ask about in class #####
        # How do we move through without a loop #
# def count_divisibles_in_range(start, end, n):
#         count = 0
#         range = 
      


# count_divisibles_in_range(start=11, end=15, n=13)


# import itertools
# numbers = [100, 200, 300, 400]

# data = list(zip(itertools.count(0, 10), numbers))

# print(data)




# -------------------------------------------------------------------------------------------------------------------------#


# def count_word_dominators(words):


# -------------------------------------------------------------------------------------------------------------------------#


# def seven_zero(n):
#         x = len(str(n))
#         answer = False
#         number = ""
#         value = 0 
#         d = 0
#         k = 1
#         if (n % 2 == 0) or (n % 5 == 0):
#                 while d <= (x + 1):  # outer loop
#                         k = 1
#                         while k < d:    # inner loop
#                                 number = "7" * (k) + "0" * (d - k)
#                                 k += 1
                               
#                         d += 1
#                 value = int(number)
#                 if value % n == 0:
#                         return value
#         else:
#                 while answer == False:
#                         number = number + "7"
#                         value = int(number)
#                         if (value % n) == 0:
#                                 return value
#         print(value)
#         return value
        

# seven_zero(4)


 # -------------------------------------------------------------------------------------------------------------------------#



# def can_balance(items):
#         fulcrum = 1
#         for item in items:
#                 list_perms = (itertools.permutations(items))
#                 for tuple in list_perms:
#                         middle = len(tuple) / 2
#                         for element in tuple:
#                                 torque = element * fulcrum
#                 # print(element)
                        

       


# can_balance([6,1,10,5,4])



# -------------------------------------------------------------------------------------------------------------------------#



# def oware_move(board, house):
#         middle = len(board) // 2
#         player = [board[:middle]]
#         opponent = [board[middle:]]
#         board = dict()
#         for i in range(len(board)):
#                print(board[house])

#         print((f"middle = {middle}"))
#         print((f"player = {player}"))
#         print((f"opponent = {opponent}"))
    
# oware_move([0, 2, 1, 2], 1)



# -------------------------------------------------------------------------------------------------------------------------#


# def count_growlers(animals):
#         count = 0
#         looking_left = ['cat', 'dog']
#         looking_right = ['tac', 'god']
#         animals_dict = dict()
#         for animal in enumerate(animals):
#                 # print(animal[1] == ''.join(sorted(animal[1])))
#                 if animal[1] == list(animal[1]
#                         print('cat')
#                 elif animal[1] == 'dog' or 'god':
#                         print('dog')
          
                        
#         # print(count)
#         # print(animals[0])
#         # print(animals_dict)
                


# count_growlers(['god', 'cat', 'cat', 'tac', 'tac', 'dog', 'cat', 'god'])






# -------------------------------------------------------------------------------------------------------------------------#


        ##### Ask about in class #####
# def remove_after_kth(items, k=1):
#         res_dict = {}
#         result = []             # Append to this only if the elements count is still at most equal to k
        
#         for i in range(len(items)):
#                 # print(f"i is : {i}")
#                 res_dict[items[i]] = items.count(items[i])
#                 if i not in res_dict.values():
#                         res_dict.update(items[i])
        
        
#         print(f"result dict:  {res_dict}")
#         print(f"result list:  {result}")

        

# remove_after_kth([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1], k=1)

# There's a couple of problems here. First of all, the fact that you're using count()means that the dictionary entry for that item is getting set to its final value instantly. So if for example, you had k=1, and an item appears in the list twice, the first time it's encountered in the loop, its dictionary entry is set to 2. Which means it won't ever be added to result. You need to be updating  the dictionary in a way that allows each key to be appended to the list k times, no more, no less
# -------------------------------------------------------------------------------------------------------------------------#


# def reverse_reversed(items):


# return the items in reverse, but if a list exists inside, reverse the list as well no matter how nested
# suggests recursion
# Base case handles any argument that is not a list
# Should not mutate or change the original list

# good question how to find out if a list exists within the items array
# tip from the prof 

# for in in list
        # if isinstance(i, list):
                #print("This element is a list", i)
        # else:
                # print("The type of this element is". type(i))

        # prints This element is a list (3 times for the 3 lists that exist in example)
        # prints the type of this element is class int, for the final element which is 10 in the example


# -------------------------------------------------------------------------------------------------------------------------#



# def perimeter_limit_split(a,b,p):

        # rectangles are tuples (a,b) where a and b are positive integers
        # rect can be cut into smaller rectangles with the same total area using either a straight hor or vert cut


        # Best solved with recursion again
        # mentions @lru_cache memoization on top of it because we will visit each subcomponent an exponential #
        # define max size of @lru_cache as a * b
        # define recursive function inside main function



# -------------------------------------------------------------------------------------------------------------------------#

        ##### COMPLETE #####  (0.1666 seconds)
# def count_carries(a, b):
#     a = str(a)
#     b = str(b)
#     # Initialise the value of
#     # carry to 0
#     carry = 0;
 
#     # Counts the number of carry
#     # operations
#     count = 0;
 
#     # Initialise len_a and len_b
#     # with the sizes of strings
#     len_a = len(a);
#     len_b = len(b);
 
#     while (len_a != 0 or len_b != 0):
 
#         # Assigning the ascii value
#         # of the character
#         x = 0;
#         y = 0;
#         if (len_a > 0):
#             x = int(a[len_a - 1]) + int('0');
#             len_a -= 1;
         
#         if (len_b > 0):
#             y = int(b[len_b - 1]) + int('0');
#             len_b -= 1;
 
#         # Add both numbers/digits
#         sum = x + y + carry;
 
#         # If sum > 0, increment count
#         # and set carry to 1
#         if (sum >= 10):
#             carry = 1;
#             count += 1;
 
#         # Else, set carry to 0
#         else:
#             carry = 0;
 
#     return count;
        
# print(count_carries(9555,555))

# -------------------------------------------------------------------------------------------------------------------------#


# words = ['tantaras', 'tarantas', 'tartanas', 'university']

# def unscramble(words, word):


# unscramble(words, word='tartnaas')

# -------------------------------------------------------------------------------------------------------------------------#
        
        ##### COMPLETE #####    (0.538s)
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
# reverse_vowels('revorse the vewels')



# -------------------------------------------------------------------------------------------------------------------------#




        ##### COMPLETE #####    (0.653s)
# def knight_jump(knight, start, end):
#         result = []
#         for i in range(0, len(start)):
#                 result.append(abs(start[i] - end[i]))
#         if set(knight) == set(result):
#                 return True
#         return False


# -------------------------------------------------------------------------------------------------------------------------#
# from math import *

# def sum_of_two_squares(n):
#         x = 0
#         y = isqrt(n)
#         sum = y ** 2

#         while x <= y:
#                 if sum < n:
#                         x += 1
#                         sum += 2 * x - 1
#                 elif sum > n:
#                         sum -= 2 * y - 1
#                         y -= 1
#                 else:
#                 # found a match
#                         print(x, y)
#                         x += 1
#                         sum += 2 * (x - y)
#                         y -= 1
             
        

# print(sum_of_two_squares(50))


# def sum_of_two_squares(n):
        
#         i = 2
#         while (i * i <= n):
#                 count = 0
#                 if (n % i == 0 ):
#                         while (n % i == 0):
#                                 count += 1
#                                 n = int(n / i)
#                                 print(n)

                       
#                 i += 1

 
# print(sum_of_two_squares(50))






# -------------------------------------------------------------------------------------------------------------------------#

        #### COMPLETE #####
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


# count_consecutive_summers(42)






# -------------------------------------------------------------------------------------------------------------------------#

# import decimal
# import math

        ##### COMPLETE #####
# def fibonacci_word( k ):
#     decimal.getcontext().prec = 165
#     root_5 = decimal.Decimal( 5 ).sqrt()
#     phi = ( 1 + root_5 ) / 2
#     r = phi / ( 1 + ( phi * 2 ) )

#     return math.floor(  ( k + 2 ) * r ) - math.floor( ( k + 1 ) * r )






# -------------------------------------------------------------------------------------------------------------------------#

# def josephus(n, k):
#         result = []
#         if (n == 1 and k == 1):
#                 return 1
#         elif (n > 1 and k == 1):
#                 return 2
#         elif (josephus(n - 1, k - 1) == n - 1):
#                 return 1
#         else:
#                 result.append(josephus(n - 1, k - 1) + 2)
#         return list(result)
        
               

# print(josephus(n = 4, k= 1))


# def josephus(n, k):
#         p, i, seq = list(range(n)), 0, []
# 	while p:
# 	        i = (i+k-1) % len(p)
# 	        seq.append(p.pop(i))
# 	return 'Prisoner killing order: %s.\nSurvivor: %i' % (', '.join(str(i) for i in seq[:-1]), seq[-1])


# print(josephus(5, 2))



# -------------------------------------------------------------------------------------------------------------------------#


# def count_growlers(animals):
#         left = ['cat', 'dog']
#         right = ['tac', 'god']
#         CAT = 'cat'
#         DOG = 'dog'
#         growler_count = 0

#         for index, animal in enumerate(animals):
#                 if animal in left:
#                         if animals[index] == DOG:
#                                 print("its a dog")
#                                 growler_count += 1
                        
#                 elif animal in right:
#                         print("right")
#         print(growler_count)



# count_growlers(['god', 'cat', 'cat', 'tac', 'tac', 'dog', 'cat', 'god'])





# def winning_card(cards, trump=None):
#         suits = ['clubs', 'diamonds', 'hearts', 'spades']
#         ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11,
#                 'queen': 12, 'king': 13, 'ace': 14 }


#         temp = []
#         if trump!= None:
#                 s = trump
#                 for card in cards:
#                         if card[1] == s:
#                                 temp.append(card)
#                 winner = 0
#                 for i in range(len(temp)):
#                         if ranks[temp[i][0]] > ranks[temp[winner][0]]:
#                                 winner = i
#                 return temp[winner]
#         if trump == None:
#                 s = cards[0][1]
#                 for card in cards:
#                         if card[1] == s:
#                                 temp.append(card)
#                 winner = 0
#         for i in range(len(temp) - 1):
#                 if ranks[temp[i][0]] > ranks[temp[winner][0]]:
#                         winner = i
#                 return temp[winner]

# cards = [('three', 'spades'), ('ace', 'diamonds'), ('jack', 'spades'), ('eight', 'spades')]
# print(winning_card(cards, None))
                        






        # Complete 63s VS code, but try and use pop not remove to speed up
# def eliminate_neighbours(items):

#         maximum = max(items)
#         counter = 0

#         if len(items) == 1:
#                 return 1

#         for i in range(len(items)):
#                 if maximum in items:
#                         pointer = min(items)
                       
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
#                                 items.pop(i + 1)
#                                 counter += 1
#                         elif items.index(i) == len(items) - 1:
#                                 items.pop(i - 1)
#                                 counter += 1
#                         else:
#                                 a = items[items[items.index(pointer)] + 1]
#                                 b = items[items[items.index(pointer)] - 1]
#                                 if a > b:
#                                         items.remove(a)
#                                         counter += 1
#                                 else:
#                                         items.remove(b)
#                                         counter += 1
#                         items.pop(i)
#         return counter



# print(eliminate_neighbours([8, 5, 3, 1, 7, 2, 6, 4]))



# def crag_score(dice):

#         scorecard = { 'crag': 50, 'thirteen': 26, 'three-of-a-kind': 25, 'low straight': 20, 'high straight': 20, 'odd straight': 20,
#                     'even straight': 20 }
#         temp = []
#         print(dice[1])
                


# print(crag_score([1,2,3]))




# def three_summers(items, goal):


# def two_summers(items, goal, i=1, j=None):
#     j = j if j is not None else len(items)-1
#     while i < j:
#         x = items[i] + items[j]
#         if x == goal:
#             return True
#         elif x < goal:
#             i += 1
#         else:
#             j -= 1
#     return False


# print(two_summers([10, 11, 16, 18, 19], 40, i=0, j=19))


def arithmetic_progression(items, n):

        for j in (items):
                i, k = j - 1, j + 1
                while i > -1 and k < n:
                        if set_[i] + set_[k] == 2 * set_[j]:
                                return set_[i] + set_[k] == 2 * set_[j]
                        elif set_[i] + set_[k] < 2 * set_[j]:
                                i -= 1
                        else:
                                k += 1

        return False


print(arithmetic_progression([2,4,5,7,8,12,17]))















































































































































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