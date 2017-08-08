import toml
import sys

def checkingToml():
    if sys.argv.count == 1:
        print("比較したいTOMLファイル名を引数に入力")
    a_path = sys.argv[1]
    b_path = sys.argv[2]
    print("File A path: "+a_path)
    print("File B path: "+b_path)
    print("Checking...")
    ta = toml.load(a_path)
    tb = toml.load(b_path)
    team_list = ta["groups"].keys()
    print(team_list)

    for team in team_list:
        fg = False
        print("Chekking Group: "+team)
        for user_a in ta["groups"][team]["users"]:
            print(team+" user: " + user_a)
            for user_b in tb["groups"][team]["users"]:
                if user_a == user_b:
                    #print("found")
                    fg = True
                    break
            if fg:
                fg = False
                continue
            else:
                print("not found: " + user_a)
                return 1
        
        fg = False
        for user_a2 in tb["groups"][team]["users"]:
            #print(team+" user: " + user_a)
            for user_b2 in ta["groups"][team]["users"]:
                if user_a2 == user_b2:
                    #print("found")
                    fg = True
                    break
            if fg:
                fg = False
                continue
            else:
                print("not found: " + user_a2)
                return 1
    return 0

if __name__ == "__main__":
    if checkingToml() == 0:
        print("Succeed")
    else:
        print("Failed")
        pass