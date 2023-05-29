def sigma(function, start, end):

  for i in range(start, end +1):

    result += function(1)

    return result

def triangle(b, h):

  area = (b * h) / 2

  return area

def square(l):

  area = l * l

  return area

def rectangle(b, h):

  area = b * h

  return area

def product(sequence):

    result = 1

    for term in sequence:

        result *= term

    return result

def delta(*args):

    result = []

    for i in range(1, len(args)):

        delta = args[i] - args[i-1]

        result.append(delta)

    return result

def perc(n):

    result = n / 100

    return str(result) + "%"

def matrix(row1,row2,*row3):

    listmatrix = []

    listmatrix.append(row1)

    listmatrix.append(row2)

    if row3:

        listmatrix.append(row3)

    return listmatrix

def add_matrix(matrix1,matrix2):

    result = [x + y for x,y in zip(matrix1,matrix2)]

    return result

def sub_matrix(matrix1,matrix2):

    result = [x - y for x,y in zip(matrix1,matrix2)]

    return result

def mult_matrix(matrix1,matrix2):

    result = [x * y for x,y in zip(matrix1,matrix2)]

    return result

def div_matrix(matrix1,matrix2):

    result = [x / y for x,y in zip(matrix1,matrix2)]

    return result

def percof(perc,num):

    result = (perc/100)*num

    return result

g_ratio = 1.61803398875

tau = 6.2831853070
