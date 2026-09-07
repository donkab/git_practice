try:
    number = int(input("整数を1つ入力してください: "))
except ValueError:
    print("整数を入力してください")
else:
    if number % 2 == 0:
        print("偶数です")
    else:
        print("奇数です")
