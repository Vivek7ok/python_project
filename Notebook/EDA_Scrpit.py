import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"D:\Data_set\Data_Set_15\Data\student_mental_health_burnout.csv")

df = df.drop_duplicates()
print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())
print(df.describe())
print(df.columns)

conditions = [
    df['financial_stress_score'] <= 3,
    df['financial_stress_score'].between(3, 7),
    df['financial_stress_score'] >= 7
]

choices = ['Good', 'Avegrage', 'Bad']

df['financial_state'] = np.select(conditions, choices ,default='Unkown')

# print(df['financial_state'].value_counts())
sns.countplot(data=df,x='financial_state')
plt.savefig(r"D:\Data_set\Data_Set_15\python\EDA_output.png", dpi=300, bbox_inches='tight')
plt.show()


print(df['gender'].value_counts())

print(df[['student_id','cgpa']].sort_values(by='cgpa',ascending=False).head(3))

df.groupby('gender')['daily_study_hours'].mean().plot(kind='pie',autopct='%1.1f%%')
plt.title('Avrage study of eaxg gender')
plt.savefig(r"D:\Data_set\Data_Set_15\python\EDA_output\Image_2.png", dpi=300, bbox_inches='tight')
plt.show()

df.groupby('year')['depression_score'].mean().plot(kind='line')
plt.xlabel('Acadmic_year')
plt.ylabel('Depresion_Score')
plt.title('Student_deprison')
plt.savefig(r"D:\Data_set\Data_Set_15\python\EDA_output\Image_3.png", dpi=300, bbox_inches='tight')
plt.show()

df.groupby('year')['physical_activity_hours'].mean().plot(kind='pie',autopct='%1.1f%%')
plt.xlabel('Acadmic_year')
plt.ylabel('Avegrage_physical_activity')
plt.title('Diffrence_btween_year_and_hour_of_physical_activity')
plt.savefig(r"D:\Data_set\Data_Set_15\python\EDA_output\Image_4.png", dpi=300, bbox_inches='tight')
plt.show()
