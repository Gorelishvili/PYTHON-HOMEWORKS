seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(hours, "საათი,", minutes, "წუთი,", secs, "წამი")