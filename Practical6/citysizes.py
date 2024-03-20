uk_cities=[0.56,0.62,0.04,9.7]
chn_cities=[0.58,8.4,29.9,22.2]
uk_name=["Edinburgh","Glasgow","Stirling","Longdon"]
chn_name=["Haining","Hangzhou","Shanghai","Beijing"]
import matplotlib.pyplot as plt
plt.figure()
plt.bar(chn_name,chn_cities,width=0.8)
plt.ylabel("Population")
plt.xlabel("Cities")
plt.title("cities'population of CHN")
plt.show()

plt.clf()

plt.figure()
plt.bar(uk_name,uk_cities,width=0.8)
plt.ylabel("Population")
plt.xlabel("Cities")
plt.title("cities'population of UK")
plt.show()

plt.clf()
