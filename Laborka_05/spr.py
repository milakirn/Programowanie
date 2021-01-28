from pip._vendor.distlib.compat import raw_input

x = raw_input("Put a number: ")
l = list(str(x))
print(l)
l.reverse()
x = int(''.join(l))
print (x)

print(f"Coś dodaję")