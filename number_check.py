try:
    number = int(input("整数を1つ入力してください: "))
except ValueError:
    print("整数を入力してください")
else:
    if number % 2 == 0:
        print("偶数です")
    else:
        print("奇数です")
    if number % 3 == 0:
        print("3の倍数です")
    else:
        print("3の倍数ではありません")
    if number % 5 == 0:
        print("5の倍数です")
    else:
        print("5の倍数ではありません")
    if number % 15 == 0:
        print("15の倍数です")
