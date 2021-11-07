
def fibbonaci(loop_times):
    num1 = 0
    num2 = 1
    fibbonaci_nums = []
    for num in range(int(loop_times)):
        num3 = num1 + num2
        fibbonaci_nums.append(num3)
        num1 = num2
        num2 = num3
    print(fibbonaci_nums)


fibbonaci(50)