from tkinter import *

class calculator():

    def __init__(self):
        #Establish main window parameters
        self.main = Tk()
        self.main.title("Scientific Calculator")
        #self.main.geometry("310x400")    #note to lecturer, please uncomment if using mac os
        self.main.geometry("400x600")    #note to lecturer, please comment this line if using mac os
        self.main.config(bg="grey40")
        #self.main.activebackground("black")
        #Establish input window parameters
        self.inputwindow = Entry(self.main)
        self.inputwindow.grid(row = 0, column = 0, columnspan = 6)
        self.inputwindow.config(font=("Roboto", 22))
        self.inputwindow.focus_set()
        #Establish function Buttons
        #Row 1
        #Square Root Button
        self.button_sqrt = Button(self.main, text="sqrt", width=4, height=2, command=lambda:self.sqrt())    #lambda command used to indicate the parenthesis for tying a function to a command.
        self.button_sqrt.grid(row = 1, column = 0, padx = 1, pady = 1)    #Positioning of the button on the grid, padding space between buttons
        self.button_sqrt.config(font=("Roboto", 22))    #Text style and size for button text

        #Base 10 Button
        self.button_base10 = Button(self.main, text="10^x", width=4, height=2, command=lambda:self.ins("10**"))    #Insert operator for power
        self.button_base10.grid(row = 1, column = 1, padx = 1, pady = 1)    #x axis padding 1 unit, y axis padding 1 unit
        self.button_base10.config(font=("Roboto", 22))

        #Log Button
        self.button_log = Button(self.main, text="log", width=4, height=2, command=lambda:self.log())    #log function used, tied to command by lambda
        self.button_log.grid(row = 1, column = 2, padx = 1, pady = 1)
        self.button_log.config(font=("Roboto", 22))

        #Exponent Button
        self.button_exp = Button(self.main, text="exp", width=4, height=2, command=lambda:self.ins('*10**'))
        self.button_exp.grid(row = 1, column = 3, padx = 1, pady = 1)
        self.button_exp.config(font=("Roboto", 22))

        #Modulo Button
        self.button_mod = Button(self.main, text="mod", width=4, height=2, command=lambda:self.ins('%'))
        self.button_mod.grid(row = 1, column = 4, padx = 1, pady = 1)
        self.button_mod.config(font=("Roboto", 22))
        #Row 2
        #X^2 Button
        self.button_xsqr = Button(self.main, text="x^2", width=4, height=2, command=lambda:self.xsquare())
        self.button_xsqr.grid(row = 2, column = 0, padx = 1, pady = 1)
        self.button_xsqr.config(font=("Roboto", 22))

        #X^Y Button
        self.button_indice = Button(self.main, text="x^y", width=4, height=2, command=lambda:self.ins('**'))
        self.button_indice.grid(row = 2, column = 1, padx = 1, pady = 1)
        self.button_indice.config(font=("Roboto", 22))

        #C Button
        self.button_cancel = Button(self.main, text='C', width=4, height=2, command=lambda:self.cancel())
        self.button_cancel.grid(row = 2, column = 2, padx = 1, pady = 1)
        self.button_cancel.config(font=("Roboto", 22))

        #Delete / Backspace Button
        self.button_delete = Button(self.main, text="Del", width=4, height=2, command=lambda:self.delete())
        self.button_delete.grid(row = 2, column = 3, padx = 1, pady = 1)
        self.button_delete.config(font=("Roboto", 22))

        #Division Button
        self.button_divide = Button(self.main, text="/", width=4, height=2, command=lambda:self.ins('/'))
        self.button_divide.grid(row = 2, column = 4, padx = 1, pady = 1)
        self.button_divide.config(font=("Roboto", 22))
        #Row 3
        #Pi Button
        self.button_pi = Button(self.main, text="pi", width=4, height=2, command=lambda:self.ins('3.14159265'))
        self.button_pi.grid(row = 3, column = 0, padx = 1, pady = 1)
        self.button_pi.config(font=("Roboto", 22))

        #7 Button
        self.button_7 = Button(self.main, text="7", width=4, height=2, command=lambda:self.ins('7'))
        self.button_7.grid(row = 3, column = 1, padx = 1, pady = 1)
        self.button_7.config(font=("Roboto", 22))

        #8 Button
        self.button_8 = Button(self.main, text="8", width=4, height=2, command=lambda:self.ins('8'))
        self.button_8.grid(row = 3, column = 2, padx = 1, pady = 1)
        self.button_8.config(font=("Roboto", 22))

        #9 Button
        self.button_9 = Button(self.main, text="9", width=4, height=2, command=lambda:self.ins('9'))
        self.button_9.grid(row = 3, column = 3, padx = 1, pady = 1)
        self.button_9.config(font=("Roboto", 22))

        #Multiply Button
        self.button_multiply = Button(self.main, text="x", width=4, height=2, command=lambda:self.ins('*'))
        self.button_multiply.grid(row = 3, column = 4, padx = 1, pady = 1)
        self.button_multiply.config(font=("Roboto", 22))
        #Row 4
        #n! Button
        self.button_nfact = Button(self.main, text="n!", width=4, height=2, command=lambda:self.factorial())
        self.button_nfact.grid(row = 4, column = 0, padx = 1, pady = 1)
        self.button_nfact.config(font=("Roboto", 22))

        #4 Button
        self.button_4 = Button(self.main, text="4", width=4, height=2, command=lambda:self.ins('4'))
        self.button_4.grid(row = 4, column = 1, padx = 1, pady = 1)
        self.button_4.config(font=("Roboto", 22))

        #5 Button
        self.button_5 = Button(self.main, text="5", width=4, height=2, command=lambda:self.ins('5'))
        self.button_5.grid(row = 4, column = 2, padx = 1, pady = 1)
        self.button_5.config(font=("Roboto", 22))

        #6 Button
        self.button_6 = Button(self.main, text="6", width=4, height=2, command=lambda:self.ins('6'))
        self.button_6.grid(row = 4, column = 3, padx = 1, pady = 1)
        self.button_6.config(font=("Roboto", 22))

        #Subtract Button
        self.button_subtract = Button(self.main, text="-", width=4, height=2, command=lambda:self.ins('-'))
        self.button_subtract.grid(row = 4, column = 4, padx = 1, pady = 1)
        self.button_subtract.config(font=("Roboto", 22))
        #Row 5
        #Plus/Minus Button
        self.button_plusminus = Button(self.main, text="+/-", width=4, height=2, command=lambda:self.plusminus())
        self.button_plusminus.grid(row = 5, column = 0, padx = 1, pady = 1)
        self.button_plusminus.config(font=("Roboto", 22))

        #1 Button
        self.button_1 = Button(self.main, text="1", width=4, height=2, command=lambda:self.ins('1'))
        self.button_1.grid(row = 5, column = 1, padx = 1, pady = 1)
        self.button_1.config(font=("Roboto", 22))

        #2 Button
        self.button_2 = Button(self.main, text="2", width=4, height=2, command=lambda:self.ins('2'))
        self.button_2.grid(row = 5, column = 2, padx = 1, pady = 1)
        self.button_2.config(font=("Roboto", 22))

        #3 Button
        self.button_3 = Button(self.main, text="3", width=4, height=2, command=lambda:self.ins('3'))
        self.button_3.grid(row = 5, column = 3, padx = 1, pady = 1)
        self.button_3.config(font=("Roboto", 22))

        #Add Button
        self.button_add = Button(self.main, text="+", width=4, height=2, command=lambda:self.ins('+'))
        self.button_add.grid(row = 5, column = 4, padx = 1, pady = 1)
        self.button_add.config(font=("Roboto", 22))
        #Row 6
        #( Left Bracket Button
        self.button_lbracket = Button(self.main, text="(", width=4, height=2, command=lambda:self.ins('('))
        self.button_lbracket.grid(row = 6, column = 0, padx = 1, pady = 1)
        self.button_lbracket.config(font=("Roboto", 22))

        #) Right Bracket Button
        self.button_rbracket = Button(self.main, text=")", width=4, height=2, command=lambda:self.ins(')'))
        self.button_rbracket.grid(row = 6, column = 1, padx = 1, pady = 1)
        self.button_rbracket.config(font=("Roboto", 22))

        #0 Button
        self.button_0 = Button(self.main, text="0", width=4, height=2, command=lambda:self.ins('0'))
        self.button_0.grid(row = 6, column = 2, padx = 1, pady = 1)
        self.button_0.config(font=("Roboto", 22))

        #Period Button
        self.button_period = Button(self.main, text=".", width=4, height=2, command=lambda:self.ins('.'))
        self.button_period.grid(row = 6, column = 3, padx = 1, pady = 1)
        self.button_period.config(font=("Roboto", 22))

        #Equals Button
        self.button_enter = Button(self.main, text="=", width=4, height=2, command=lambda:self.enter())
        self.button_enter.grid(row = 6, column = 4, padx = 1, pady = 1)
        self.button_enter.config(font=("Roboto", 22))

        #Loop to keep the GUI open
        self.main.mainloop()

    '''MAIN CALCULATOR FUNCTIONS'''

    #Insert function for input window
    def ins(self, value):
        self.inputwindow.insert(END, value)    #END of string, insert value on input window

    #Function for n!
    def factorial(self):
        #Recursive sub-function to calculate n!
        def nfact(n):
            if n == 0:
                return 1
            else:
                return n*nfact(n-1)    #recursive function, will multiply n by n-1 until n=1

        #Processing function
        grab = int(self.inputwindow.get())    #grab input value and convert to integer for sub-function
        answer = str(nfact(grab))    #Apply sub-funct and convert answer back to string
        self.inputwindow.delete(0, 'end')    #Clear display
        self.inputwindow.insert(0, answer)    #Insert calculated value

    #Plus/Minus function
    def plusminus(self):
        #Sub function to change plus minus
        def splusminus(n):
            change = -1*n    #convert number sign
            return change

        #Processing function
        grab = int(self.inputwindow.get())    #grab input value and convert to integer for sub-function
        answer = str(splusminus(grab))    #Apply sub-funct and convert answer back to string
        self.inputwindow.delete(0, 'end')    #Clear display
        self.inputwindow.insert(0, answer)    #Insert calculated value

    #Square function
    def xsquare(self):
        #Sub function to square number
        def sxsquare(n):
            sq = n*n    #calculate square, n x n
            return sq

        #Processing function
        grab = int(self.inputwindow.get())    #grab input value and convert to integer for sub-function
        answer = str(sxsquare(grab))    #Apply sub-funct and convert answer back to string
        self.inputwindow.delete(0, 'end')    #Clear display
        self.inputwindow.insert(0, answer)    #Insert calculated value

    #Square root function
    def sqrt(self):
        #Sub function for calculating square root
        def ssqrt(n):
            x = n    #establish answer variable x as starting at n
            y = 1    #establish counting variable
            while (x > y):    #while x is greater than y
                x = (x + y) / 2    #x equals x+y divided by 2
                y = n / x    #y equals n/x. Function repeats while x is greater than y
            return x

        #Processing function
        grab = int(self.inputwindow.get())    #grab input value and convert to integer for sub-function
        answer = str(ssqrt(grab))    #Apply sub-funct and convert answer back to string
        self.inputwindow.delete(0, 'end')    #Clear display
        self.inputwindow.insert(0, answer)    #Insert calculated value

    #Log Function
    def log(self):
        #Sub function for calculating log10()
        def slog(n):
            r = 10    #log base 10
            if (n > 1):    #Condition if n greater than 1
                return 1 + slog(n/r)    #Recursive function calculate log
            else:
                return 0

        #Processing function
        grab = int(self.inputwindow.get())    #grab input value and convert to integer for sub-function
        answer = str(slog(grab))    #Apply sub-funct and convert answer back to string
        self.inputwindow.delete(0, 'end')    #Clear display
        self.inputwindow.insert(0, answer)    #Insert calculated value

    #C cancel function
    def cancel(self):
        self.inputwindow.delete(0, 'end')    #Window is cleared

    #Delete function
    def delete(self):
        grab = self.inputwindow.get()
        self.inputwindow.delete(0, 'end')    #window is cleared
        refresh = grab[:-1]    #list is refreshed on screen less the last index value
        self.inputwindow.insert(0, refresh)

    #Equals Button Processing function
    def enter(self):
        grab = self.inputwindow.get()
        answer = eval(grab)    #Use of pythons basic evaluate function
        self.inputwindow.delete(0, 'end')
        self.inputwindow.insert(0, answer)

if __name__ == "__main__":
    calculator()
