#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    all_sum = []
    for i in range(len(arr)):

        for j in range(len(arr[i])):


            print(arr[i][j])
    return max(all_sum)

if __name__ == '__main__':
    arr = [
        [-9, -9, -9,  1, 1, 1],
        [ 0, -9,  0,  4, 3, 2],
        [-9, -9, -9,  1, 2, 3],
        [ 0,  0,  8,  6, 6, 0],
        [ 0,  0,  0, -2, 0, 0],
        [ 0,  0,  1,  2, 4, 0]
    ]

    result = hourglassSum(arr)
    print(result)
