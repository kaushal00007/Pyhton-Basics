import pandas as pd
import numpy as np
#df= pd.read_csv("C:\\Pyhton-course\\Admission_Predict.csv")
df= pd.read_csv("C:\\Pyhton-course\\Assignment-2\\assets\\NISPUF17.csv")

#Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than
# high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

#This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

#    {"less than high school":0.2,
#    "high school":0.4,
#    "more than high school but not college":0.2,
#    "college":0.2}
def proportion_of_education():
    import pandas as pd
    import numpy as np
    df = pd.read_csv(r'assets/NISPUF17.csv',index_col=0)
    result = {"less than high school": 0,
        "high school": 0,
        "more than high school but not college": 0,
        "college": 0}
    EDUS = df['EDUC1']
    edus = np.sort(EDUS.values)
    n = len(edus)
    result["less than high school"] = np.sum(edus == 1)/n
    result["high school"] = np.sum(edus == 2)/n
    result["more than high school but not college"] = np.sum(edus == 3)/n
    result["college"] = np.sum(edus == 4)/n
    return result
    raise NotImplementedError()

#df['proportion_of_education'] = df.apply(proportion_of_education,axis = 1)
    # your code goes here
    # YOUR CODE HERE
    #raise NotImplementedError()
#if 'EDUC1' in df.columns:
#    print('found')
#else:
#    print("Not found")
#print(df.columns)
#print(df.head(20))
#def average_influenza_doses():
cbf_flu = df[['CBF_01', 'P_NUMFLU']]
cbf_flu1 = cbf_flu[cbf_flu['CBF_01']==1].dropna()
cbf_flu2 = cbf_flu[cbf_flu['CBF_01']==2].dropna()
flu1 = cbf_flu1['P_NUMFLU']
f1 = flu1.sum()/flu1.size
flu2 = cbf_flu2['P_NUMFLU']
f2 = flu2.sum()/flu2.size
#print(cbf_flu)
#print(cbf_flu1)
#print(cbf_flu2)
#sex_cpox = df[['SEX', 'HAD_CPOX','DVRC1', 'DVRC2','DVRC3','DVRC4','DVRC5','DVRC6','DVRC7','DVRC8','DVRC9']]
male_df = df[df['SEX'] == 1]
vac_m = male_df[male_df['P_NUMVRC'] >= 1]
cp_m = vac_m[vac_m['HAD_CPOX'] == 1]
counts_cp_m = cp_m['SEX'].count()
ncp_m = vac_m[vac_m['HAD_CPOX'] == 2]
counts_ncp_m = ncp_m['SEX'].count()
male = counts_cp_m / counts_ncp_m
female_df = df[df['SEX'] == 2]
vac_f = female_df[female_df['P_NUMVRC'] >= 1]
cp_f = vac_f[vac_f['HAD_CPOX'] == 1]
counts_cp_f = cp_f['SEX'].count()
ncp_f = vac_f[vac_f['HAD_CPOX'] == 2]
counts_ncp_f = ncp_f['SEX'].count()
female = counts_cp_f / counts_ncp_f
ratio_dict = {"male": male, "female": female}
#return ratio_dict
print(cp_m)
    #raise NotImplementedError()

def average_influenza_doses():
    import pandas as pd
    import numpy as np
    df = pd.read_csv(r'assets/NISPUF17.csv',index_col=0)
    cbf_flu = df[['CBF_01','P_NUMFLU']]
    cbf_flu1 = cbf_flu[cbf_flu['CBF_01']==1].dropna()
    cbf_flu2 = cbf_flu[cbf_flu['CBF_01']==2].dropna()
    flu1 = cbf_flu1['P_NUMFLU']
    f1 = flu1.sum()/flu1.size
    flu2 = cbf_flu2['P_NUMFLU']
    f2 = flu2.sum()/flu2.size
    return (f1,f2)
    raise NotImplementedError()




def chickenpox_by_sex():
    import pandas as pd
    import numpy as np
    df = pd.read_csv(r'assets/NISPUF17.csv',index_col=0)
    male_df=df[df['SEX']==1]
    vac_m=male_df[male_df['P_NUMVRC']>=1]
    cp_m=vac_m[vac_m['HAD_CPOX']==1]
    counts_cp_m=cp_m['SEX'].count()
    ncp_m=vac_m[vac_m['HAD_CPOX']==2]
    counts_ncp_m=ncp_m['SEX'].count()
    male=counts_cp_m/counts_ncp_m
    female_df=df[df['SEX']==2]
    vac_f=female_df[female_df['P_NUMVRC']>=1]
    cp_f=vac_f[vac_f['HAD_CPOX']==1]
    counts_cp_f=cp_f['SEX'].count()
    ncp_f=vac_f[vac_f['HAD_CPOX']==2]
    counts_ncp_f=ncp_f['SEX'].count()
    female=counts_cp_f/counts_ncp_f
    ratio_dict={"male":male,"female":female}
    return ratio_dict
    raise NotImplementedError()