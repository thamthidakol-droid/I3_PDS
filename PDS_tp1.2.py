total_seconds = 9875
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = (total_seconds % 3600) % 60
print(hour,"h",minute,"min",second,"s")

print("check:", (hour * 3600) + (minute * 60) + second == total_seconds)
