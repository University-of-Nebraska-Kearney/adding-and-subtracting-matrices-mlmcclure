# Create your own code here
def get_matrix():

    row_count = int(input("Enter Row count: "))
    column_count = int(input("Enter Column count: "))
    matrix = []
    for _ in range(row_count):
        row = []
        for _ in range(column_count):
            row.append(int(input("Enter a value: ")))
        matrix.append(row)
    return matrix










#get_martix(): creates and returns a matrix from user input such that the size and dimension is determined by the user. This should be a hybrid of the fixed-sized and the sentinel model we discussed in class. The user should be prompted for the number or rows and columns before entering values to fill the matrix.

#add_matrix(matrix1, matrix2): takes two matrices as parameters, verifies that they can be added together, adds them together, and returns the sum.