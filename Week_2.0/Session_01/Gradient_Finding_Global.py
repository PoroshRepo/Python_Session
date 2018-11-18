
#The function that we get from the graph is -
# y = (x+5)^2
#dy/dx = 2*(x+5)

gradient_func = lambda x: 2*x + 10

X_0 = 3

#initially X_old is X_init, that's the point we start from
X_old = X_0

#Learning rate to do the shifting of slope
learning_rate = 0

#Diff between X_old and X_new
threshold = 100

iteration_no = 0

while threshold > 0.0000001:
    X_new = X_old - (learning_rate * gradient_func(X_old))
    
    threshold = abs(X_new - X_old)
    
    X_old = X_new
    
    iteration_no += 1
    
    print("Iteration no: "+str(iteration_no)+", Value of X = "+str(X_new))
    
    
    
    
    
    
    