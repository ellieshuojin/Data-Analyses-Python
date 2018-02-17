import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
aardissData = pd.read_csv('aardiss.csv')

# Plot subjective stress as a function of cortisol reactivity across drug conditions
g = sns.lmplot(x='cortreact3',
               y='strs_auci7',
               hue='drug',
               data=aardissData,
               truncate=False,
               legend=False,
               palette=['grey', 'blue'],
               size=8,
               scatter_kws={'facecolors':'none', 's':60, 'linewidth':2},
               line_kws={'linewidth':3, "alpha":0.5})

# Styling
sns.set_style('white')
sns.set_context('talk')
g.set_axis_labels('Cortisol Reactivity', 'Subjective Stress')
g.despine(right=False, top=False)
plt.tight_layout(pad=1.5)
plt.legend(['Placebo', 'Testosterone'], loc='lower right')
plt.title('Cortisol Reactvity and Subjective Stress across Drug Conditions')
plt.xlim(-170, 170)
plt.ylim(-30, 25)
plt.show()
