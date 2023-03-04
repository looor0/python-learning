import pandas as pd
import os

"""
Purpose to scan multiple CSV in one folder, and then put them into a dataframe, and then filter the dataframe to the version needed
"""

directory_path = '/Users/xxx/Documents/'
df_all = pd.DataFrame()

#Loop over the csv file
for file_name in os.listdir(directory_path):
    try:
        # find the file end in csv
        if file_name.endswith('.csv'):
            df = pd.read_csv(os.path.join(directory_path, file_name), encoding="latin-1")
            df_all = pd.concat([df_all, df], axis=0)
    except Exception as e:
        print("Error during merging dataframe")
print("Dataframe merge completed")

#Just in case columns include any space, it will get removed
df_all.columns = df_all.columns.str.replace(" ", '')

#Method 1 > return the dataframe into a list as all the input, and then will export the csv
group_df=df_all.groupby(["id", "type"])["note"].apply(list).reset_index()
pivoted_df=group_df.pivot_table(index="id",columns="type",values="note", aggfunc=lambda x:x)
pivoted_df.columns = pivoted_df.columns.str.replace(" ","")
pivoted_df.to_csv("Updated_file.csv", index=True)

#Method 2 > return under original type
filtered_df=df_all.set_index("ID")[["type","note"]]
filtered_pivoted_df=filtered_df.pivot(columns="type",values="note")
filtered_pivoted_df.columns=filtered_pivoted_df.columns.str.replace(" ","")
filtered_pivoted_df.to_csv("Updated_file2.csv", index=True)
