import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')

airport=['대한항공','아시아니항공','제주항공','진에어','이스타항공','에어부산','티웨이항공','에어서울','플라이강원']
interest=[666776, 306331, 211118, 137306, 124339, 95837, 83947, 49593, 16634]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

pos = np.arange(9)
rects = plt.barh(pos, interest, align='center', height=0.5)
plt.yticks(pos, airport)

for i, rect in enumerate(rects):
    ax.text(0.95 * rect.get_width(), rect.get_y() + rect.get_height(), str(interest[i]), ha='right', va='center')

plt.xlabel('관심도')
plt.show()
