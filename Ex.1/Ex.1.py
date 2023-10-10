import matplotlib.pyplot as plt


# Pythagorem Theorem

def hypotenuse(a,b):
    c = (a**2 + b**2)**0.5
    return c

a = 33
b = 44
c = hypotenuse(a,b)
print(str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2")



#create a figure and axis
fig, ax = plt.subplots()

#plot the two lines
ax.plot([0,0], [0,a], label="Side a")
ax.plot([0,b], [0,0], label="Side b")

#plot hypotenuse
ax.plot([0,b], [a,0], label = "Hypotenuse")


#Add a Legend
ax.legend()

#Display the Graph
plt.show()
