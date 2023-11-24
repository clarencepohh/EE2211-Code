# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 18:05:21 2023

@author: Clarence
"""
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from numpy.linalg import inv 

def regression():
    print("\n Are the input values for matrix X integers or floats (i for integers, f for floats)?")
    input_type_X = input()

    print("\n Input the size of the matrix X starting with number of rows")
    num_rows = int(input())
    print("\n Input the number of columns.")
    num_cols = int(input())

    if input_type_X == 'i':
        # populate the matrix X with integers
        print("\n Input the matrix row by row.")
        matrix_X = np.zeros((num_rows, num_cols))
        for i in range(num_rows):
            for j in range(num_cols):
                print("\n Input the element at position ", i+1, j+1)
                matrix_X[i][j] = int(input())

    elif input_type_X == 'f':
        # populate the matrix X with floats
        print("\n Input the matrix row by row.")
        matrix_X = np.zeros((num_rows, num_cols))
        for i in range(num_rows):
            for j in range(num_cols):
                print("\n Input the element at position ", i+1, j+1)
                matrix_X[i][j] = float(input())

    print("\n Are the input values for vector Y integers or floats (i for integers, f for floats)?")
    input_type_Y = input()
    print("\n Is one-hot encoding used? (y for yes, any other character otherwise)")
    input_one_hot = input()
    
    if input_one_hot == 'y':
        onehot = True
        
    if onehot:
        print("\n If one-hot encoding is to be done,")
        print("\n rows = # of variables,")
        print("\n cols = # of classes.")
        print("\n Input the number of variables (# of rows in class matrix)")
        vect_rows = int(input())
        print("\n Input the number of classes (# of cols in class matrix)")
        vect_cols = int(input())
    
    else: 
        print("\n Input the size of the vector Y starting with number of rows.")
        vect_rows = int(input())
        print("\n Input the number of columns.")
        vect_cols = int(input())

    if input_type_Y == 'i':
        # populate the vector Y with integers
        print("\n Input the vector Y row by row.")
        vector_Y = np.zeros((vect_rows, vect_cols))
        for i in range(vect_rows):
            for j in range(vect_cols):
                print("\n Input the element at position ", i + 1, j + 1)
                vector_Y[i][j] = int(input())

    elif input_type_Y == 'f':
        # populate the vector Y with floats
        print("\n Input the vector Y row by row.")
        vector_Y = np.zeros((vect_rows, vect_cols))
        for i in range(vect_rows):
            for j in range(vect_cols):
                print("\n Input the element at position ", i + 1, j + 1)
                vector_Y[i][j] = float(input())

    print("\n Input the order of the polynomial to be used for regression.")
    print("\n Input 1 for linear regression.")
    order = int(input()) 
    poly = PolynomialFeatures(order)
    polynomial_X = poly.fit_transform(matrix_X)

    print ("\n Is regularization being used? (y for yes, any other character otherwise)")
    regularization = input()
    if (regularization == 'y'):
        reg = True
        print("\n Input the value of lambda.")
        test_lambda = float(input())
    else:
        test_lambda = 0
        
    if polynomial_X.shape[0] > polynomial_X.shape[1]: # primal form 
        w = inv(polynomial_X.T @ polynomial_X + test_lambda*np.eye(polynomial_X.shape[1])) @ polynomial_X.T @ vector_Y

    else: # dual form
        w = polynomial_X.T @ inv(polynomial_X @ polynomial_X.T + test_lambda*np.eye(polynomial_X.shape[0])) @ vector_Y
        
    print("\n w is:\n", w)
    
    print("\n Input the test values of X starting with number of rows")
    num_rows_testX = int(input())
    print("\n Input the number of columns.")
    num_cols_testX = int(input())

    if input_type_X == 'i':
        # populate the test matrix with integers
        print("\n Input the matrix row by row.")
        test_matrix_X = np.zeros((num_rows_testX, num_cols_testX))
        for i in range(num_rows_testX):
            for j in range(num_cols_testX):
                print("\n Input the element at position ", i + 1, j + 1)
                test_matrix_X[i][j] = int(input())

    elif input_type_X == 'f':
        # populate the test matrix with floats
        print("\n Input the matrix row by row.")
        test_matrix_X = np.zeros((num_rows_testX, num_cols_testX))
        for i in range(num_rows_testX):
            for j in range(num_cols_testX):
                print("\n Input the element at position ", i + 1, j + 1)
                test_matrix_X[i][j] = float(input())
                
    polytest2 = test_matrix_X[:,0].reshape(len(test_matrix_X[:,0]),1)
    polytest = PolynomialFeatures(order)
    polynomial_testX = polytest.fit_transform(test_matrix_X)
    predicted_Y = polynomial_testX @ w
    print("\n Predicted Y is:\n", predicted_Y)
        
    if onehot:
        class_predicted_Y = np.zeros((predicted_Y.shape[0], predicted_Y.shape[1]))
        for rows in range(predicted_Y.shape[0]):
            max_value = predicted_Y[rows][0]
            max_col = 0
            for cols in range(1, predicted_Y.shape[1]):
                if max_value < predicted_Y[rows][cols]:
                    max_value = predicted_Y[rows][cols]
                    max_col = cols
            class_predicted_Y[rows][max_col] = 1
            
        print("\n Predicted Y classes are:\n", class_predicted_Y)