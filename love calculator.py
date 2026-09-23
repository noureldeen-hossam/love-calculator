print("""
██╗      ██████╗ ██╗   ██╗███████╗
██║     ██╔═══██╗██║   ██║██╔════╝
██║     ██║   ██║██║   ██║█████╗
██║     ██║   ██║╚██╗ ██╔╝██╔══╝
███████╗╚██████╔╝ ╚████╔╝ ███████╗
╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝

        💕 LOVE CALCULATOR 💕
        ❤️ Find Your Love Score ❤️
""")
name_1 = input("what is your name?\n").lower()
name_2 = input("what is your lover name?\n").lower()
def calculate_love_score(name_1, name_2):
    name = name_1 + name_2
    test_1 = "true"
    test_2 = "love"
    total_true = 0
    total_love = 0
    for latter in name:
        if latter in test_1:
            total_true += 1
        if latter in test_2:
            total_love += 1
    print(f"your love score is {total_true}{total_love}%")
calculate_love_score(name_1, name_2)