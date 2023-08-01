def ch_gender(username):
    no_repe_chars = len(set(username))
    if no_repe_chars % 2 == 0:
        return "Girl"
    else:
        return "Boy"

username = input("Enter the username: ")
gender = ch_gender(username)
print("The gender is:", gender)