#a piece of code to give even and odd num bet a range of numbers
lowlim = 0
highlim = 0
evenorodd = ""
client_response = ""

even_num = []
odd_num = []


def first_number():
    return int(input("Please enter your first lower limit number: "))


def second_number():
    return int(input("Please enter your first upper limit number: "))


def call_number():
    return str(input("Do you want odd or even numbers printed: (type Even/Odd)"))


lowlim = first_number()
highlim = second_number()
evenorodd = call_number()


def calculate_number():
    for i in range(lowlim, highlim+1):
        if (i % 2 == 0):
            even_num.append(i)
        else:
            odd_num.append(i)
    if evenorodd == "Even":
        print(f'Even numbers of limit listed:{even_num}')
    else:
        print(f'Odd numbers of limit listed: {odd_num}')


calculate_number()


def ask_client():
    return str(input("Do you want to enter new limits? (type Yes/No ) "))


client_response = ask_client()


while (client_response == "Yes"):
    first_number()
    second_number()
    call_number()
    calculate_number()
    ask_client()
    client_response = ""

else:
    print("Thank you for playing this game!!")
    client_response = ""
