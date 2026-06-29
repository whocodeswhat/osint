from modules.username import (
    check_github,
    check_reddit,
    check_gitlab,
    check_hackerone
)

username = input("Enter username: ")

print(f"GitHub:    {check_github(username)}")
print(f"Reddit:    {check_reddit(username)}")
print(f"GitLab:    {check_gitlab(username)}")
print(f"HackerOne: {check_hackerone(username)}")