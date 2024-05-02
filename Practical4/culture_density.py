# represents a varying density changing by days
density=5   
# represents the day I can leave the lab
date=0
# Execute a finite loop within a limited range to satisfy the condition and output a time value that allows for departure      
while density<=90:
    density=2*density
    date+=1  # the same as "date= date+1", to recursive to calculate the ultimate date
print(date)
    
    
    
