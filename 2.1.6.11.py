hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
new_mins = (mins + dura)% 60
new_hour = ((mins + dura) // 60 + hour) % 24

print(' New Hour is : ' ,new_hour ,':' ,new_mins,sep='')