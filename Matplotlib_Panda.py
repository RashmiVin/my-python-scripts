import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
print(air_quality.head())
plot = air_quality.plot()
plt.show()

air_quality["station_paris"].plot()
plt.show()

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

air_quality.plot.box()
plt.show()

axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()

fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
plt.show()
axs.set_ylabel("NO$_2$ concentration")
plt.show()
fig.savefig("no2_concentrations.png")
plt.show()