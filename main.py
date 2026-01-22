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

def add_matrix(matrix1, matrix2):
    assert len(matrix1) == len(matrix2)
    assert len(matrix1[0]) == len(matrix2[0])

    result_matrix = []
    for row1, row2 in zip(matrix1, matrix2, strict = True):
        row = []
        for element1, element2 in zip(row1, row2, strict = True):
            row.append(element1 + element2)
        result_matrix.append(row)

    return result_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    m1 = get_matrix()
    print_matrix(m1)
    print()

    m2 = get_matrix()
    print_matrix(m2)
    print()

    m3 = add_matrix(m1, m2)
    print_matrix(m3)
    print()


if __name__ == "__main__":
    main()
#get_martix(): creates and returns a matrix from user input such that the size and dimension is determined by the user. This should be a hybrid of the fixed-sized and the sentinel model we discussed in class. The user should be prompted for the number or rows and columns before entering values to fill the matrix.

#add_matrix(matrix1, matrix2): takes two matrices as parameters, verifies that they can be added together, adds them together, and returns the sum.