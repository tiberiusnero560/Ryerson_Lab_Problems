
#         #### COMPLETE #####   1 / 55
# def is_ascending(items):
#     print("List Items : " + str(items))
#     result = all( i < j for i, j in zip(items, items[1:]))
#     return(str(result))
#         #### COMPLETE #####


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
       
                        
      
#         #### COMPLETE #####   3 / 55
# def only_odd_digits(n):
#        return set(str(n)) - set('13579') == set()
#         #### COMPLETE #####  



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



tiles = [(3, 5), (5, 2), (2, 3)]

def domino_cycle(tiles):
        for j, k in tiles:
                # print ("j is " + str(j))
                # print ("k is "+ str(k))
                if (j == k ):
                        print (k)

        # print(data)

domino_cycle(tiles)


# def count_dominators(items):
#         if (items) == []:
#                 return 0
#         else: 
#                 dominators = 1
#                 for num in range(1, len(items)):
#                         if items[num] < items[num - 1]:
#                                 dominators = dominators + 1
#                         else: 
#                                 dominators = dominators + 0
#                         return dominators



# def extract_increasing_integers_from_digit_string
# def extract_increasing(digits):
#         result = []
#         converted = str(digits)
#         for i in converted:
# extract_increasing(245349)


