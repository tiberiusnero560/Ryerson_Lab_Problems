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



def is_left_handed(pips):
        left_hand_combos = [(1,2,3)]
        right_hand_combos = []
        result = []
        for i in pips:
                result.append(i)
        print(result)

is_left_handed((1, 2, 3))




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
#         for item in items:
#                 list = (itertools.permutations(items))

#         print(list.__eq__)


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
#         animals_dict = dict()
#         for animal in enumerate(animals):
#                 print(animal[1])
          
                        
#         print(count)
#         print(animals[0])
#         print(animals_dict)
                


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
        
        


#         # for item in res_dict.values():
#         #         print(item)
                
#         # return result
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

# def sum_of_two_squares(n):
#         if n < 2:
#                 result = 1                      # base case
#         else:
#                 result = n * sum_of_two_squares(n - 1)   # linear recursive call

#         print(result)       
#         return result


# sum_of_two_squares(2)

# -------------------------------------------------------------------------------------------------------------------------#

# def is_zigzag(n):
#         fact = [0 for i in range(n + 1)]
#         zig = [0 for i in range(n + 1)]

#         fact[0] = 1
#         for i in range(1, n + 1):
#                 fact[i] = fact[i - 1] * i
                
#         zig[0] = 1
#         zig[1] = 1

#         print("zig zag numbers ", end = '')

#         print(zig[0], zig[1], end = " ")

#         for i in range(2, n):
#                 sum = 0

#                 for k in range(0, i):
#                         sum += ((fact[i - 1] // (fact[i - 1 - k] * fact[k])) * zig[k] * zig[i - 1 - k])

#                 zig[i] = sum // 2

#                 print(sum // 2, end = " ")

# is_zigzag(25391)


               
# -------------------------------------------------------------------------------------------------------------------------#








# -------------------------------------------------------------------------------------------------------------------------#

# import decimal
# import math

# def fibonacci_word( k ):
#     decimal.getcontext().prec = 165
#     root_5 = decimal.Decimal( 5 ).sqrt()
#     phi = ( 1 + root_5 ) / 2
#     r = phi / ( 1 + ( phi * 2 ) )

#     return math.floor(  ( k + 2 ) * r ) - math.floor( ( k + 1 ) * r )






# -------------------------------------------------------------------------------------------------------------------------#









# -------------------------------------------------------------------------------------------------------------------------#


