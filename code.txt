import math
from colorama import *

init()
dead = False
def main():
    def dead_print(message=''):
        print(Fore.RED+message)
        print(Style.BRIGHT + "\n --- # ENDING PROGRAM # --- " + Style.RESET_ALL)
        print(Fore.RESET)
        return None

    def inputing(message=''):
        global dead

        values = input(Fore.GREEN + message + ": \n")
        
        print(Fore.RESET)

        x = []
        try:
            x = list(map(float, values.split()))
        except ValueError:
            dead_print("You have put something except numbers. Please restart program, writing only numbers. If number is decimal, use '.'")
            dead = True

        return x

    def round_to_point(num, point):
        num *= (10**point)
        num = num // 1
        num = num / (10**point)
        return num

    def squared_list(a=[]):
        x = []
        for e in a:
            x.append(e**2)
        return x

    def avarage_in_list(a=[]):
        sum = 0
        for e in a:
            sum+=e
        return sum/len(a)

    def multiplied_lists(a=[], b=[]):
        x = []
        for i in range(len(a)):
            x.append(a[i]*b[i])
        return x

    print(Style.BRIGHT + "\n  --- # STARTING PROGRAM # --- " + Style.RESET_ALL)
    print(Fore.BLACK + Back.WHITE +"\nThis program will find linear dependency between variables X and Y with help of Smallest Squares Method\n"+ Back.RESET + Fore.RESET)

    x = inputing("Input values of X-s with spaces")
    if dead: return
    x_num = len(x)
    if x_num==0: 
        dead_print("You did not put any numbers. Please restart")
        return
    y = inputing("Input values of Y-s with spaces")
    if dead: return
    y_num = len(y)
    if y_num==0: 
        dead_print("You did not put any numbers. Please restart")
        return

    if x_num!=y_num: 
        dead_print("Number of values of X and Y must be equal. Please restart")
        return

    try:
        rounding = int(input(Fore.YELLOW+"Input the number of decimal places for dependency coefficients: \n"))
        print(Fore.RESET)
    except ValueError:
        dead_print("Inputted value is not a whole positive number")
        return

    dev_mod = 0
    try:
        dev_mod = int(input(Fore.CYAN+"For absolute and relative errors X and Y, enter 1:\n"))
        print(Fore.RESET)
    except ValueError:
        print(Fore.RED+"\nError in call, program will continue without computing errors\n"+Fore.RESET)

    S_X2 = avarage_in_list(squared_list(x)) - avarage_in_list(x)**2 #Dispersions
    S_Y2 = avarage_in_list(squared_list(y)) - avarage_in_list(y)**2

    R_XY = avarage_in_list(multiplied_lists(x, y)) - avarage_in_list(x)*avarage_in_list(y) 

    alpha_coef = R_XY/S_X2
    beta_coef = avarage_in_list(y) - alpha_coef*avarage_in_list(x) 

    if dev_mod!=1:

        a_coef = round_to_point(alpha_coef, rounding)
        b_coef = round_to_point(beta_coef, rounding)

        print(Fore.BLUE+ Back.BLACK+"Your dependency between X and Y formula is: "+ Fore.RESET+ Back.RESET)
        print(Style.BRIGHT+Fore.LIGHTCYAN_EX+"Y = "+ str(a_coef) + " * X + " + str(b_coef) + "\n"+Style.RESET_ALL+Fore.RESET)

        print(Fore.YELLOW+"Hope this was helpfull."+Fore.RESET)
        print(Style.BRIGHT + Fore.RED + "\n --- # ENDING PROGRAM # --- " + Style.RESET_ALL)
        print(Fore.RESET)
    if dev_mod==1:
        delta_a = round_to_point(2*math.sqrt((S_Y2/S_X2 - alpha_coef**2)/(x_num-2)), rounding)
        delta_b = round_to_point(delta_a*math.sqrt(S_X2 + avarage_in_list(x)**2), rounding)
        epsilon_a = 0
        epsilon_b = 0
        if alpha_coef!=0:
            epsilon_a = round_to_point(abs(delta_a/alpha_coef)*100, rounding)
        if alpha_coef==0:
            epsilon_a = 100
        if beta_coef!=0:
            epsilon_b = round_to_point(abs(delta_b/beta_coef)*100, rounding)
        if beta_coef==0:
            epsilon_b = 0
        
        r_cov = round_to_point(R_XY/((S_Y2*S_X2)**0.5), rounding)
        alpha_coef = round_to_point(alpha_coef, rounding)
        beta_coef = round_to_point(beta_coef, rounding)

        print(Fore.BLUE+ Back.BLACK+"Your dependency between X and Y formula is: "+ Fore.RESET+ Back.RESET)
        print(Style.BRIGHT+Fore.LIGHTCYAN_EX+"Y = "+ str(alpha_coef) + " * X + " + str(beta_coef) + "\n" + Style.RESET_ALL + Fore.RESET)

        print(Back.BLACK+"Absolute errors of A coefficient and B coefficient: \n"+Back.RESET)
        print(Style.BRIGHT+"A: " + str(delta_a) + "; B: " + str(delta_b) + "\n" + Style.RESET_ALL)
        print(Back.BLACK+"Relative errors of A coefficient and B coefficient: \n" +Back.RESET)
        print(Style.BRIGHT+"A: " + str(epsilon_a) + "%; B: " + str(epsilon_b) + "%\n"+ Style.RESET_ALL)
        print(Back.BLACK+"Covariation coefficient:\n"+Back.RESET)
        print(Style.BRIGHT+Fore.RED+"r = " + str(r_cov)+Style.RESET_ALL+Fore.RESET)
        print("")

        print(Fore.YELLOW+"Hope this was helpfull."+Fore.RESET)
        print(Style.BRIGHT + Fore.RED + "\n --- # ENDING PROGRAM # --- " + Style.RESET_ALL)
        print(Fore.RESET)
main()
input()