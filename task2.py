#create a dictionary with student data
import pandas as pd
student_data ={
    "name":     ["akash","bala","cherry","dam","evoke","fresh"],
    "age":      [20,21,19,22,23,20],
    "major":    ["cs","math","phy","eco","bio","chem"],
    "score":    [85,92,78,95,88,90],
    "twon":     ["hyd","rr","wnp","ngknl","knl","gdwl"],
    "pass out": [22,23,24,25,21,25],
}
#Create a data frame from the dictionary
df = pd.DataFrame(student_data)
#print the data frame
print(df)