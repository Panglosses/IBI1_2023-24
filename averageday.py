#Create the dictionary containing the average time of students
dic1={"sleeping":8,"classes":6,"studying":3.5,"TV":2,"music":1,"others":3.5}
import matplotlib.pyplot as plt
#Set the labels of the graph
activity_labels=["sleeping","classes","studying","TV","music","others"]
#Ensure that the data and graph can change correctly with the dictionary change.
time_week=[dic1["sleeping"],dic1["classes"],dic1["studying"],dic1["TV"],dic1["music"],dic1["others"]]
plt.figure()

plt.pie(time_week,labels=activity_labels,startangle=90)
plt.show()

plt.clf()
