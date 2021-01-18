# Blok 1:
import tkinter as tk

calc_expr = "" 

# Blok 2:	
def btn_pressed(num): 
	global calc_expr 
	calc_expr = calc_expr + str(num) 
	disp_expr.set(calc_expr) 

#Blok 3:
def btn_eq_pressed(): 
	try: 
		global calc_expr 
		total = str(eval(calc_expr)) 
		disp_expr.set(total) 
		calc_expr = disp_expr.get() 
	except: 
		disp_expr.set(" ERROR ") 
		calc_expr = ""
		display.configure(fg='red')

# Blok 4:
def btn_AC_pressed(): 
	global calc_expr 
	calc_expr = "" 
	disp_expr.set("")
	display.configure(fg='black')

# Blok 5:
def btn_DEL_pressed(): 
	global calc_expr 
	calc_expr = calc_expr[0:-1]
	disp_expr.set(calc_expr) 

# Blok 6:
win = tk.Tk() 
win.configure(background="LightSlateGray")
win.title('Simple Calculator for "blind" people') 
win.resizable(width=False, height=False)
win.option_add('*Font', 'Verdana 20 bold')

# Blok 7:
disp_expr = tk.StringVar() 
display = tk.Entry(win, textvariable=disp_expr, justify="right", bg="khaki") 
display.grid(columnspan=4, sticky="WE") 
disp_expr.set('enter your expression') 

# Blok 8:
btn_1 = tk.Button(win, text=' 1 ', fg='white', bg='gray', 
		command = lambda:  btn_pressed(1), height=1, width=7) 
btn_1.grid(row=4, column=0) 

btn_2 = tk.Button(win, text=' 2 ', fg='white', bg='gray', 
		command = lambda: btn_pressed(2), height=1, width=7) 
btn_2.grid(row=4, column=1) 

btn_3 = tk.Button(win, text=' 3 ', fg='white', bg='gray', 
		command = lambda: btn_pressed(3), height=1, width=7) 
btn_3.grid(row=4, column=2) 

btn_4 = tk.Button(win, text=' 4 ', fg='white', bg='gray', 
		command = lambda: btn_pressed(4), height=1, width=7) 
btn_4.grid(row=3, column=0) 

btn_5 = tk.Button(win, text=' 5 ', fg='white', bg='gray', 
		command = lambda: btn_pressed(5), height=1, width=7) 
btn_5.grid(row=3, column=1) 

btn_6 = tk.Button(win, text=' 6 ', fg='white', bg='gray', 
		command = lambda: btn_pressed(6), height=1, width=7) 
btn_6.grid(row=3, column=2) 

btn_7 = tk.Button(win, text=' 7 ', fg='white', bg='gray', 
		command = lambda: btn_pressed(7), height=1, width=7) 
btn_7.grid(row=2, column=0) 

btn_8 = tk.Button(win, text=' 8 ', fg='white', bg='gray', 
		command = lambda: btn_pressed(8), height=1, width=7) 
btn_8.grid(row=2, column=1) 

btn_9 = tk.Button(win, text=' 9 ', fg='white', bg='gray', 
		command = lambda: btn_pressed(9), height=1, width=7) 
btn_9.grid(row=2, column=2) 

btn_0 = tk.Button(win, text=' 0 ', fg='white', bg='gray',
		command = lambda: btn_pressed(0), height=1, width=7) 
btn_0.grid(row=5, column=0) 

btn_plus = tk.Button(win, text=' + ', fg='white', bg='DarkSlateGray', 
		command = lambda: btn_pressed("+"), height=1, width=7) 
btn_plus.grid(row=5, column=3) 

btn_minus = tk.Button(win, text=' - ', fg='white', bg='DarkSlateGray', 
		command = lambda: btn_pressed("-"), height=1, width=7) 
btn_minus.grid(row=4, column=3) 

btn_multiply = tk.Button(win, text=' * ', fg='white', bg='DarkSlateGray', 
		command = lambda: btn_pressed("*"), height=1, width=7) 
btn_multiply.grid(row=3, column=3) 

btn_divide = tk.Button(win, text=' / ', fg='white', bg='DarkSlateGray', 
		command = lambda: btn_pressed("/"), height=1, width=7) 
btn_divide.grid(row=2, column=3) 

btn_equal = tk.Button(win, text=' = ', fg='white', bg='DarkSlateGray', 
		command = lambda: btn_eq_pressed(), height=1, width=7) 
btn_equal.grid(row=5, column=2) 

btn_Clear = tk.Button(win, text=' AC ', fg='white', bg='red', 
		command = lambda: btn_AC_pressed(), height=1, width=7) 
btn_Clear.grid(row=1, column='0') 

btn_point= tk.Button(win, text='.', fg='white', bg='gray', 
		command = lambda: btn_pressed('.'), height=1, width=7) 
btn_point.grid(row=5, column=1)

btn_left_brck= tk.Button(win, text='(', fg='white', bg='DarkSlateGray', 
		command = lambda: btn_pressed('('), height=1, width=7)
btn_left_brck.grid(row=1, column=2)
		
btn_right_brck= tk.Button(win, text=')', fg='white', bg='DarkSlateGray', 
		command = lambda: btn_pressed(')'), height=1, width=7) 
btn_right_brck.grid(row=1, column=3)

btn_point= tk.Button(win, text='.', fg='white', bg='gray', 
		command = lambda: btn_pressed('.'), height=1, width=7)

btn_Clear_ent = tk.Button(win, text=' DEL ', fg='white', bg='Orange', 
		command = lambda: btn_DEL_pressed(), height=1, width=7) 
btn_Clear_ent.grid(row=1, column='1') 

win.mainloop() 

