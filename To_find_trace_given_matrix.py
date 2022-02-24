# Q:To find the trace of the given matrix 
# matrix=[[1,2,3,4],[1,2,3,4],[2,3,4,5]]
sum=0;
def matrix_var(matrix,n):
    for i in range(n):
        sum = matrix[i][i];
    return sum
print(matrix_var([[1,2,3,4],[1,2,3,4],[2,3,4,5]],3))
    