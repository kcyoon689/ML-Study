# Notation
    # y = actual value
    # y_hat = predicted value
    # n = number of samples

# Error
    # y_hat = w * x + b
    # error = y_hat - y
        #   = (w * x + b) - y

# Cost Function
    # MSE = 1/n * sum((y - y_hat)^2)


X =[2.0, 4.0, 6.0, 8.0]
Y =[3.0, 4.0, 5.0, 6.0]
error_square = []

w = -0.1
b = 4.0

for i in range(0, 4):
    y_hat = w * X[i] + b
    error = (y_hat - Y[i])
    error_square.append(error**2)

mse = sum(error_square)/len(error_square)

print(mse)