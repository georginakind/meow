create_player_list = []
accepted_pretty_names = {'gk', 'george', 'G', "George"}
pete_names = {"pete", "Pete"}
enter_player = input("Enter your player name: ")
create_player_list.append(enter_player)
if enter_player in accepted_pretty_names:
    print("omg she's so pretty")
elif enter_player in pete_names:
    print("WOOF who let the dogs out!!") 
else: print(enter_player)

while enter_player != "done":
    enter_player = input("Enter your player name: ")
    create_player_list.append(enter_player)
    if enter_player in accepted_pretty_names:
        print ("omg shes so pretty")
    elif enter_player in pete_names:
        print("WOOF who let the dogs out!!")
    else: print(enter_player)   

create_player_list.remove("done")
print("PLAYERZ:", (create_player_list))