# def fun_name(parameter):
#     statements
#     [return epression]


#defining
def hello():
    print('Hello')
    print('Optimus')

#calling
hello()




def greetings(message):
    print("Hello",message)

greetings("Ashu")





def calc_area(w, h):
    area = w * h
    print('area =',area)

calc_area(10,20)
calc_area(4,25)






def calc_area_v2(w, h):
    area = w * h
    return area

res = calc_area_v2(4,25)     #storing return value in variable
print(res)

res = calc_area_v2(4,25) + calc_area_v2(4,25)      #using return value in an expression
print(res)

print(calc_area_v2(4,25))       #display

