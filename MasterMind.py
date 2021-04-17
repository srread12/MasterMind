import csv
from random import randrange
from datetime import datetime


def user_comp_num(comp_num2):

    comp_num2.clear()
    while True:
        print("What is the number you want the ai to solve.")
        num = input()
        if num.isdigit() and len(num) == 3:
            break
        elif len(num) != 3 and num.isdigit():
            print("Please enter a three digit number.")
        else:
            print("That is not a number")
    num1 = int(num[0])
    num2 = int(num[1])
    num3 = int(num[2])
    comp_num2.insert(0, num1)
    comp_num2.insert(1, num2)
    comp_num2.insert(2, num3)
    return comp_num2


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if int(arr[j][2]) > int(arr[j+1][2]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def ai_hard(num):
    print("Do want to enter a number for the computer to solve?")
    do = input()
    if do.startswith("y"):
        num = user_comp_num(num)
    print("Target number " + str(num))
    start_time = datetime.now()
    counter_2 = 0
    while True:
        counter_2 += 1
        comp_numbers_1 = [randrange(0, 10), randrange(0, 10), randrange(0, 10)]
        if correct(num, comp_numbers_1) == 1:
            break
    print("Ai number " + str(comp_numbers_1))
    print("It took the ai #" + str(counter_2-1) + " to find the numbers.")
    print("It took " + str(datetime.now() - start_time) + " to find the number.")


def check_ai(hue, computer):
    for j in range(3):
        if hue[j] == computer:
            return 1
    return -1


def ai(target):
    print("Do want to enter a number for the computer to solve?")
    do = input()
    if do.startswith("y"):
        target = user_comp_num(target)
    print("Target number " + str(target))
    good = False
    counter_1 = 0
    good_nums = []
    comp_num = []
    nums_check = []
    for i in range(0, 10):
        nums_check.clear()
        counter_1 += 1
        nums_check.append(i)
        nums_check.append(i)
        nums_check.append(i)
        if check_ai(target, i) == 1:
            good_nums.append(i)
            if correct(target, nums_check) == 1 or len(good_nums) == 3:
                good = True
                break
    if good and correct(target, nums_check) == 1:
        comp_num.clear()
        comp_num = nums_check
    else:
        if len(good_nums) == 2:
            for x in range(3):
                counter_1 += 1
                if target[x] == good_nums[0]:
                    comp_num.append(good_nums[0])
                else:
                    comp_num.append(good_nums[1])
        else:
            for i in range(3):
                counter_1 += 1
                if target[i] == good_nums[0]:
                    comp_num.append(good_nums[0])
                elif target[i] == good_nums[1]:
                    comp_num.append(good_nums[1])
                else:
                    comp_num.append(good_nums[2])
    print("AI numbers " + str(comp_num))
    print("It took the ai " + str(counter_1-1) + " attempts to find the numbers.")


def read_file():
    with open("data/NamesAndScores.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            names_score.append(line)
    return names_score


def add_name_score(num):
    read_file()
    print("What is your first name.")
    name1 = input()
    print("What is your last name.")
    name2 = input()
    names_score.append([name1, name2, nums])
    to_save = name1 + "," + name2 + "," + str(num)
    f = open("data/NamesAndScores.csv", "a")
    f.write("\n")
    f.write(to_save)
    f.close()


def check(goo, guess_1):
    yellows = 0
    greens = 0
    computer = []
    user_temp = []
    for i in range(3):
        computer.append(goo[i])
        user_temp.append(guess_1[i])

    answer = []
    for i in range(3):
        if goo[i] == guess_1[i]:
            greens += 1
            computer[i] = ""
            user_temp[i] = "   "
    for i in range(3):
        for j in range(3):
            if computer[i] == user_temp[j] and i != j:
                yellows += 1
                computer[i] = " "
                user_temp[j] = "  "

    for i in range(greens):
        answer.append("Green")
    for i in range(yellows):
        answer.append("Yellow")

    if greens == 0 and yellows == 0:
        answer.append("Red")

    return answer


def correct(num, numbers):
    if num[0] == numbers[0] and num[1] == numbers[1] and num[2] == numbers[2]:
        return 1
    else:
        return -1


while True:
    counter = 0
    names_score = []
    nums = [randrange(10), randrange(10), randrange(10)]
    print("Welcome to the Joshua Ellis mastermind game.")
    print("1: Play the game.")
    print("2: Seeing top scores.")
    print("3: Ai solve.")
    print("4: Very dumb Ai solver.")
    print("5: Exit the game.")
    want = int(input())

    if want == 5:

        print("Bye for now.")
        break

    elif want == 4:
        ai_hard(nums)
        print()

    elif want == 3:
        ai(nums)
        print()

    elif want == 2:
        names_score.clear()
        names = read_file()
        names_sorted = bubble_sort(names)
        print("What do you want to see.")
        print("1: Lowest attempt number.")
        print("2: Highest attempt number.")
        print("3: All attempt numbers.")
        score = int(input())

        if score == 3:
            len_max = 0
            for p in names_sorted:
                length = len(p[0]) + len(p[1])
                if len_max < length:
                    len_max = length
            for name in names_sorted:
                space = len(name[0]) + len(name[1])
                line_space = len_max - space
                blank = " "*line_space
                print("Name: " + name[1] + ", " + name[0] + blank + "       Number of attempts it took #" + name[2])

        elif score == 1:
            low = "The lowest attempt was achieved by "
            attempt = ". With a attempt number of #"
            print(low + names_sorted[0][1] + ", " + names_sorted[0][0] + attempt + str(names_sorted[0][2]))
        else:
            high = "The highest attempt was achieved by "
            attempt_h = ". With a attempt number of #"
            print(high + names_sorted[-1][1] + ", " + names_sorted[-1][0] + attempt_h + str(names_sorted[-1][2]))
        print("")

    else:

        while True:
            counter += 1
            if counter > 10:
                print("Do you want to stop guessing numbers?")
                hugo = input()
                if hugo.startswith("y"):
                    print("You are lazy!")
                    print("")
                    break
            print("What is the number.")
            while True:
                number = input()
                if number.isdigit() and len(number) == 3:
                    break
                elif len(number) != 3 and number.isdigit():
                    print("Please enter a three digit number.")
                else:
                    print("Please enter a number.")

            userNum1 = int(number[0])
            userNum2 = int(number[1])
            userNum3 = int(number[2])
            user = [userNum1, userNum2, userNum3]

            if correct(nums, user) != -1:
                print("['Green', 'Green', 'Green']")
                print("You got all correct.")
                print("It took you " + str(counter-1) + " attempts to crack the code.")
                print("")
                add_name_score(counter-1)
                print("")
                break

            else:

                print(check(nums, user))
                print("")
