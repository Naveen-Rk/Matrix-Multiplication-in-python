import random

matrix=[]
for i in range(10):
    temp=[]
    for j in range(10):
        temp.append(random.randint(1,99))
    matrix.append(temp)
print(matrix)

def diagonal():
    product=1
    a=1
    for i in range(10):
        product*=matrix[i][i]
        a = a * matrix[i][10 - i - 1]
    line1=line2=line3=line4=1
    for i in range(10):
        line1*=matrix[i][1]
    for i in range(10):
        line2*=matrix[1][i]
    for i in range(10):
        line3*=matrix[9][i]
    for i in range(10):
        line4*=matrix[i][9]
    print("The product of the main diagonal elements is ",product)
    print("The product of the off diagonal elements is ",a)
    print("The product of the xaxis elements is ",line1)
    print("the product of the yaxis elements is ",line2)
    print("The product of the last xaxis elements is ",line3)
    print("The product of the last yaxis elements is ",line4)
    return (product,a,line1,line2,line3,line4)


    

diag=diagonal()
maindiag=diag[0]
offdiag=diag[1]
line1=diag[2]
line2=diag[3]
line3=diag[4]
line4=diag[5]

def greatest():
    print(max(diag))

greatest()
