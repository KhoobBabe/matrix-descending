#we made a modular program cuz the question asked
def mat_desc(orig_matrix):
    #the matrix was sorted using sort function by adding the...
    #...numbers in each row separately and sorting the rows in..
    #..descending order
    orig_matrix.sort(key = sum, reverse = True)

    print("The sorted matrix is: ", orig_matrix)


#the input was taken here 
orig_matrix = eval(input("Enter the matrix: "))

#we called the function here
mat_desc(orig_matrix)
