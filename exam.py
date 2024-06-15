########## CHECKER_BOARD ######

# table = []

# for i in range(10):
#     table += [[0] * 10]
    
# for i in range(10):
#     for j in range(10):
#         if (i+j) % 2 == 0:
#             table[i][j] = 1

# for i in range(10):
#     print(table[i], end=" ")
#     print()



##### MATRIX ######

def matrixSum(arr1, arr2):
    result = []
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
        print("이 행렬 합은 수행할 수 없습니다.")
        return None
    
    
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        result.append(row)
            
    return result


array1 = [
    [1,2],
    [2,3]
]

array2 = [
    [3,4],
    [5,6]
]

sum = []
sum = matrixSum(array1,array2)
print(sum)