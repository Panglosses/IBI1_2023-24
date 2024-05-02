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


plt.bar(uk_name,uk_cities,width=0.8)
plt.ylabel("Population")
plt.xlabel("Cities")
plt.title("cities'population of UK")
plt.show()

plt.clf()

uk_cities_sorted = sorted((uk_cities), reverse=True)
print("Sorted UK cities by population:", uk_cities_sorted)

chn_cities_sorted = sorted((chn_cities), reverse=True)
print("Sorted China cities by population:", chn_cities_sorted)