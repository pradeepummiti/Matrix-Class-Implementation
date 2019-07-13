import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        # Check for a 1x1 matrix
        if self.h == 1:
            det = self.h[0][0]
        # Check for a 2x2 matrix
        else:
            det = (self.g[0][0] * self.g[1][1]) - (self.g[1][0] * self.g[0][1])
            
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        
        sum_diag = 0;  
        
        for i in range(self.h):  
            sum_diag += self.g[i][i];  
            
        return sum_diag;  

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here      
        
        
        inverse_matrix = zeroes(self.h, self.w)
        
        # Check the dimensions of the matrix
        if self.h == 1:
            inverse_matrix[0][0] = 1 / self.g[0][0]
            #([1 / self.g[0][0]])
        else:
            # Check if the matrix is inverted
            if (self.g[0][0] * self.g[1][1]) == (self.g[0][1] * self.g[1][0]):
                raise(ValueError, "Matrix cannot be inverted")
            else:
                # Calculate the inverse of a 2x2 matrix
                r0c0 = self.g[0][0]
                r0c1 = self.g[0][1]
                r1c0 = self.g[1][0]
                r1c1 = self.g[1][1]
                
                factor = 1 / (r0c0 * r1c1 - r0c1 * r1c0)
                
                inverse_matrix = Matrix([[r1c1, -r0c1],[-r1c0, r0c0]])
                
                #Matrix(inverse_matrix)
                
                for i in range(inverse_matrix.h):
                    for j in range(inverse_matrix.w):
                        inverse_matrix[i][j] = factor * inverse_matrix[i][j]
        
        return inverse_matrix

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here

        transpose_matrix = zeroes(self.w, self.h)
        
        # Loop through columns 
        for j in range(self.w):         
            # Loop thorugh rows
            for i in range(self.h):
                transpose_matrix[j][i] = self.g[i][j]
                #new_row.append(self.g[j][i])
            #transpose_matrix.append(new_row)
            
        return transpose_matrix

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        sum_matrix = zeroes(self.h, self.w)
        
        # Nested 'for' loop to iterate over the rows and columns
        for i in range(self.h):
            # Reset the row
            row = zeroes(self.h, self.w)
            for j in range(self.w):
                sum_matrix[i][j] = self.g[i][j] + other.g[i][j]
                #row.append(self.g[i][j] + other.g[i][j])
            #sum_matrix.append(row)
            
        return sum_matrix

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        neg_matrix = zeroes(self.h, self.w)
        
        for i in range(self.h):
            row = self.g[i]
            for j in range(len(row)):
                neg_matrix[i][j] = -(self.g[i][j])
                #new_row.append(-1 * self.g[i][j])
            #neg_matrix.append(new_row)
        neg_matrix
            
        return neg_matrix

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        diff_matrix = zeroes(self.h, self.w)
        
        # Nested 'for' loop to iterate over the rows and columns
        for i in range(self.h):
            for j in range(self.w):
                diff_matrix[i][j] = self.g[i][j] - other.g[i][j]
            #diff_matrix.append(row)
            
        return diff_matrix

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        if self.w != other.h:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        matrix_mul = zeroes(self.h, other.w)
        
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    matrix_mul[i][j] += self.g[i][k] * other.g[k][j]
                    #product += self.g[i][k] * other.g[k][j]
        #matrix_mul.append(product) 
                
        return matrix_mul

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
                        
            result_mat = zeroes(self.h, self.w)
            
            for i in range(self.h):
                row = self.g[i]
                for j in range(len(row)):
                    result_mat[i][j] = other * self.g[i][j]
                    #new_row.append(other * self.g[i][j])
                #result_mat.append(new_row)                
            result_mat
         
        return result_mat