
Glbx = 100

def fun(y):                     # y - local variable
    global Glbx                 # do not assign any value in this line
    print(f"y :{y}")
    Glbx = 500
    print(f"Glbx Inside :{Glbx}")


print(f"Glbx Before :{Glbx}")

fun(50)

print(f"Glbx After :{Glbx}")
