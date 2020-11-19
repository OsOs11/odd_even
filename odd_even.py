def numbers(args, *vartuple):
    odd_numbers=[]
    dobl_numbers=[]
    for number in vartuple:
        if number % 2 != 0:
            odd_numbers.append(number)
        else:
            dobl_numbers.append(number)
    print(odd_numbers,"الاعداد الفردية هي")
    print(dobl_numbers,"لاعداد الزوجية هي")
numbers(1,2,3,4,5,6,7,8,9,10,15)
