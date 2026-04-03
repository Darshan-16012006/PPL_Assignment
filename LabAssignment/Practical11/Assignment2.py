import matplotlib.pyplot as plt
import numpy as np

# Dataset (Number of new recruitments)
companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','ATOS','Amdocs']
recruitments = [120, 150, 180, 100, 130, 160, 90, 110]

# -------- a) Bar Chart --------
plt.figure(figsize=(8,5))
plt.bar(companies, recruitments)
plt.title('New Recruitments in Companies')
plt.xlabel('Companies')
plt.ylabel('Number of Recruitments')
plt.xticks(rotation=30)
plt.show()

# -------- b) Pie Chart --------
plt.figure(figsize=(7,7))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title('Recruitment Distribution')
plt.show()

# -------- c) Customized Pie Chart --------
explode = [0.1 if c == 'Amazon' else 0 for c in companies]  # highlight Amazon

plt.figure(figsize=(7,7))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        explode=explode, shadow=True, startangle=140)
plt.title('Customized Recruitment Pie Chart')
plt.show()

# -------- d) Doughnut Chart --------
plt.figure(figsize=(7,7))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Doughnut Chart of Recruitments')
plt.show()

# -------- Comparison: IBM vs Amdocs --------
compare_companies = ['IBM','Amdocs']
compare_values = [100, 110]

plt.figure(figsize=(6,5))
plt.bar(compare_companies, compare_values)
plt.title('Comparison of IBM vs Amdocs Recruitments')
plt.ylabel('Number of Recruitments')
plt.show()