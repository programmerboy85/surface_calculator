import turtle
loc_x = []
loc_y = []
x = ""
y = ""
bp = 0
locl = int(input("enter the number of locations:"))
for i in range(locl):
	xys = True
	loc = input("enter the location x_y:")
	for j in range(len(loc)):
		l = loc[j]
		if l == "_":
			xys = False
		if l != "_" and xys == True:
			x = x + l
		if l != "_" and xys == False:
			y = y + l
	loc_x.append(x)
	loc_y.append(y)
	y = ""
	x = ""
for i in range(len(loc_x)):
	loc_x[i] = int(loc_x[i])
for i in range(len(loc_y)):
	loc_y[i] = int(loc_y[i])		
for xx in range(max(loc_x)):
	for yy in range(max(loc_y)):
		if xx > min(loc_x):
			if xx < max(loc_x):
				if yy > min(loc_y):
					if yy < max(loc_y):
						bp = bp + 1
for i in range(len(loc_x)):
	turtle.setpos(loc_x[i]*10,loc_y[i]*10)
turtle.setpos(loc_x[0],loc_y[0])
turtle.mainloop()
s = (locl/2)+bp-1
print(s)