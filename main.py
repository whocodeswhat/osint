from modules.username import check_profile

username = input("Enter username: ")

print(check_profile("GitHub", f"https://github.com/{username}"))
print(check_profile("Reddit", f"https://reddit.com/user/{username}"))
print(check_profile("GitLab", f"https://gitlab.com/{username}"))
print(check_profile("HackerOne", f"https://hackerone.com/{username}"))
