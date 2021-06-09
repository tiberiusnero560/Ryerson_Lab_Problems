
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

        ##### Still Working On #####
# tiles2 = [(3, 5), (5, 2), (2, 3)]
# tiles = [(1, 3), (3, 2), (2, 5), (5, 2), (2, 1)]
# def domino_cycle(tiles):
#         if len(tiles) == 0:
#                 return True
#         if len(tiles) == 1:
#                 return tiles[0][0] == tiles [0][1]      # Returns False
#         for i in range(len(tiles) - 1):
#                 if tiles[i][0] == tiles[i + i][0]:
#                         return True
#                 return False

#         # if tiles[i][0] which is the right digit of a tuple, is == to tiles[i + 1][0]
# domino_cycle(tiles)

# -------------------------------------------------------------------------------------------------------------------------#

        ##### COMPLETE #####
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

        ##### Some Reason still working on... #####
# def extract_increasing(digits):
#         current = digits[0]
#         previous = -1
#         # digits_list = digits.split()
#         for d in digits:
#                 print(d)
# extract_increasing('045349')

# -------------------------------------------------------------------------------------------------------------------------#

# wordlist = open("words_sorted.txt", "r")
# new_words = {}

# def words_with_letters(words, letters):
#         for word in words.read().split():
#                 if letters in word:
#                         print (word)


# words_with_letters(words=wordlist, letters='klore')


# -------------------------------------------------------------------------------------------------------------------------#

        ##### COMPLETE #####
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


        ##### COMPLETE But look at another way of doing it later ##### 
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
