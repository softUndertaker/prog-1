
X = []
print("Digite os 10 elementos do vetor X:")
for i in range(10):
    elemento = int(input(f"Elemento {i + 1} de X: "))
    X.append(elemento)

Y = []
print("Digite os 10 elementos do vetor Y:")
for i in range(10):
    elemento = int(input(f"Elemento {i + 1} de Y: "))
    Y.append(elemento)

R = []

for i in range(10):
    R.append(X[i]) 
    R.append(Y[i]) 

print("Vetor R:", R)