# Vyber dáta zo súboru Prevalence of mental health disorders
    # 1.Posledny dostupny rok v databaze
    # 2. Od posledneho dostupneho roku v databaze, vyber rok 10 rokov spat
import pandas as pd
from scipy.stats import shapiro
from scipy.stats import wilcoxon
from scipy.stats import ttest_rel
import statistics as st


results = []

# returns the right choice of statistical test parametric/non-parametric
def the_right_test(input_list):
    for list in input_list:
        if list[1] < 0.05 or list[2] < 0.05:
            if list[0] == "Schizophrenia":
                r1 = wilcoxon(schizophrenia_10, schizophrenia_h)
                results.append(r1)
            elif list[0] == "Bipolar disorders":
                r2 = wilcoxon(bipolar_10, bipolar_h)
                results.append(r2)
            elif list[0] == "Eating disorders":
                r3 = wilcoxon(eating_disorders_10, eating_disorders_h)
                results.append(r3)
            elif list[0] == "Anxiety":
                r4 = wilcoxon(anxiety_10, anxiety_h)
                results.append(r4)
            elif list[0] == "Drugs":
                r5 = wilcoxon(drugs_10, drugs_h)
                results.append(r5)
            elif list[0] == "Depression":
                r6 = wilcoxon(depression_10, depression_h)
                results.append(r6)
            else:
                r7 = wilcoxon(alcohol_10, alcohol_h)
                results.append(r7)
                return results
        else:
            if list[0] == "Schizophrenia":
                e1 = ttest_rel(schizophrenia_10, schizophrenia_h)
                results.append(e1)
            elif list[0] == "Bipolar disorders":
                e2 = ttest_rel(bipolar_10, bipolar_h)
                results.append(e2)
            elif list[0] == "Eating disorders":
                e3 = ttest_rel(eating_disorders_10, eating_disorders_h)
                results.append(e3)
            elif list[0] == "Anxiety":
                e4 = ttest_rel(anxiety_10, anxiety_h)
                results.append(e4)
            elif list[0] == "Drugs":
                e5 = ttest_rel(drugs_10, drugs_h)
                results.append(e5)
            elif list[0] == "Depression":
                e6 = ttest_rel(depression_10, depression_h)
                results.append(e6)
            elif list[0] == "Alcohol":
                e7 = ttest_rel(alcohol_10, alcohol_h)
                results.append(e7)
                return results

# reading CSV data and renaming the column names
input_list = []
df = pd.read_csv("prevalence-by-mental-and-substance-use-disorder.csv", skiprows=0, usecols=[0,2,3,4,5,6,7,8,9])
df = df.rename(columns={'Entity': 'Country',
                        'Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized': 'Schizophrenia',
                        'Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized':'Bipolar disorders',
                        'Eating disorders (share of population) - Sex: Both - Age: Age-standardized': 'Eating disorders',
                        'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized': 'Anxiety',
                        'Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)': 'Drugs',
                        'Depressive disorders (share of population) - Sex: Both - Age: Age-standardized': 'Depression',
                        'Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)':'Alcohol'
                        })
#get the columns with the highest year in the data and 10 years before
highest_year = df[df['Year'] == df['Year'].max()]
ten_years_before = df[df['Year'] == df['Year'].max() -10]
#get the column of each disease from the latest possible year and 10 years before (currently 2009, 2019)
#fill the missing values with 0
#schizophrenia shapiro test
schizophrenia_h = highest_year["Schizophrenia"].fillna(0)
schizophrenia_10 = ten_years_before["Schizophrenia"].fillna(0)
shapiro_1_result_s = shapiro(schizophrenia_10)
shapiro_2_result_s = shapiro(schizophrenia_h)
s_p_1 = shapiro_1_result_s.pvalue
s_p_2 = shapiro_2_result_s.pvalue
input_list.append(["Schizophrenia", s_p_1, s_p_2])
#bipolar disorder shapiro test
bipolar_h = highest_year["Bipolar disorders"].fillna(0)
bipolar_10 = ten_years_before["Bipolar disorders"].fillna(0)
shapiro_1_result_b = shapiro(bipolar_10)
shapiro_2_result_b = shapiro(bipolar_h)
b_p_1 = shapiro_1_result_b.pvalue
b_p_2 = shapiro_2_result_b.pvalue
input_list.append(["Bipolar disorders", b_p_1, b_p_2])
#eating disorders shapiro test
eating_disorders_h = highest_year["Eating disorders"].fillna(0)
eating_disorders_10 = ten_years_before["Eating disorders"].fillna(0)
shapiro_1_result_ea = shapiro(eating_disorders_10)
shapiro_2_result_ea = shapiro(eating_disorders_h)
ea_p_1 = shapiro_1_result_ea.pvalue
ea_p_2 = shapiro_2_result_ea.pvalue
input_list.append(["Eating disorders", ea_p_1, ea_p_2])
#anxiety shapiro
anxiety_h = highest_year["Anxiety"].fillna(0)
anxiety_10 = ten_years_before["Anxiety"].fillna(0)
shapiro_1_result_a = shapiro(anxiety_10)
shapiro_2_result_a = shapiro(anxiety_h)
a_p_1 = shapiro_1_result_a.pvalue
a_p_2 = shapiro_2_result_a.pvalue
input_list.append(["Anxiety", a_p_1, a_p_2])
#drugs shapiro
drugs_h = highest_year["Drugs"].fillna(0)
drugs_10 = ten_years_before["Drugs"].fillna(0)
shapiro_1_result_dr = shapiro(drugs_10)
shapiro_2_result_dr = shapiro(drugs_h)
dr_p_1 = shapiro_1_result_dr.pvalue
dr_p_2 = shapiro_2_result_dr.pvalue
input_list.append(["Drugs", dr_p_1, dr_p_2])
#depression shapiro
depression_h = highest_year["Depression"].fillna(0)
depression_10 = ten_years_before["Depression"].fillna(0)
shapiro_1_result_de = shapiro(depression_10)
shapiro_2_result_de = shapiro(depression_h)
de_p_1 = shapiro_1_result_de.pvalue
de_p_2 = shapiro_2_result_de.pvalue
input_list.append(["Depression", de_p_1, de_p_2])
#alcohol shapiro
alcohol_h = highest_year["Alcohol"].fillna(0)
alcohol_10 = ten_years_before["Alcohol"].fillna(0)
shapiro_1_result_al = shapiro(alcohol_10)
shapiro_2_result_al = shapiro(alcohol_h)
al_p_1 = shapiro_1_result_al.pvalue
al_p_2 = shapiro_2_result_al.pvalue
input_list.append(["Alcohol", al_p_1, al_p_2])


#formating Shapiro test results for table creation
table_shapiro_result = (
    (format(s_p_1, ".3f"), format(b_p_1, ".3f"), format(ea_p_1, ".3f"), format(a_p_1, ".3f"), format(dr_p_1, ".3f"), format(de_p_1, ".3f"), format(al_p_1, ".3f")),
    (format(s_p_2, ".3f"), format(b_p_2, ".3f"), format(ea_p_2, ".3f"), format(a_p_2, ".3f"), format(dr_p_2, ".3f"), format(de_p_2, ".3f"), format(al_p_2, ".3f")))
# formating Wilcoxon test results for table creation
list_1 = []
list_2 = []
table_wilcoxon_result_tu = []

for res in the_right_test(input_list):
    p_values = res.pvalue
    list_1.append(format(p_values, ".3f"))
    stats = res.statistic
    list_2.append(stats)

table_wilcoxon_result_tu.append(tuple(list_1))
table_wilcoxon_result_tu.append(tuple(list_2))


# formating descriptive statistics for table creation
table_descriptive_stats = (("max", "Latest year avaliable", round(max(schizophrenia_h), 3), round(max(bipolar_h), 3), round(max(eating_disorders_h), 3), round(max(anxiety_h), 3), round(max(drugs_h), 3), round(max(depression_h), 3), round(max(alcohol_h), 3)),
                            ("", "Ten years before", round(max(schizophrenia_10), 3), round(max(bipolar_10), 3), round(max(eating_disorders_10), 3), round(max(anxiety_10), 3), round(max(drugs_10), 3), round(max(depression_10), 3), round(max(alcohol_10), 3)), 
                           ("min", "Latest year avaliable", min(schizophrenia_h), min(bipolar_h), min(eating_disorders_h), min(anxiety_h), min(drugs_h), min(depression_h), min(alcohol_h)),
                           ("", "Ten years before", min(schizophrenia_10), min(bipolar_10), min(eating_disorders_10), min(anxiety_10), min(drugs_10), min(depression_10), min(alcohol_10)),
                           ("SD", "Latest year avaliable", round(st.stdev(schizophrenia_h), 3), round(st.stdev(bipolar_h), 3), round(st.stdev(eating_disorders_h), 3), round(st.stdev(anxiety_h), 3), round(st.stdev(drugs_h), 3), round(st.stdev(depression_h), 3), round(st.stdev(alcohol_h), 3)),
                           ("", "Ten years before", round(st.stdev(schizophrenia_10), 3), round(st.stdev(bipolar_10), 3), round(st.stdev(eating_disorders_10), 3), round(st.stdev(anxiety_10), 3), round(st.stdev(drugs_10), 3), round(st.stdev(depression_10), 3), round(st.stdev(alcohol_10), 3))
                           )

