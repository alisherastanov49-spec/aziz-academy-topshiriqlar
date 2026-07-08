login = input().strip()
parol = input().strip()
natija = login == "admin" and len(parol) >= 6 and login not in parol
print(natija)