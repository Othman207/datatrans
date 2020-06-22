import pandas as pd
import numpy as np

# reading csv
df = pd.read_csv('/Users/Directory/Where/File/is/Located/exportedfile.csv')

# create dummies for columns with multiple options
df1 = pd.get_dummies(df, columns=["Column 1", "Column 2", "Column 3", "Column 4",
                                  "Column 5", "Column 6",
                                  "Column 7", "Column 8",
                                  "Column 9", "Column 10"])

df1.groupby(["Date Column", "State", "LGA", "Sex", "Age group",
             "Column 1_option1", "Column 1_option2",
             "Column 2_option1", "Column 2_option2",
             "Column 3_option1", "Column 3_option2",
             "Column 4_option1", "Column 4_option2",
             "Column 5_option1", "Column 5_option2",
             "Column 6_option1", "Column 6_option2",
             "Column 7_option1", "Column 7_option2",
             "Column 8_option1", "Column 8_option2",
             "Column 9_option1", "Column 9_option1",
             "Column 10_option1", "Column 10_option1"]).aggregate(np.sum)

# selecting subset if not all the columns are useful
df2 = df1[["Date Column", "State", "LGA", "Sex", "Age group",
           "Column 1_option1", "Column 1_option2",
           "Column 2_option1", "Column 2_option2",
           "Column 3_option1", "Column 3_option2",
           "Column 4_option1", "Column 4_option2",
           "Column 9_option1", "Column 9_option1",
           "Column 10_option1", "Column 10_option1"]]

# Date conversion to YYYY-MM-DD
df2['Date Column'] = pd.to_datetime(df2['Date Column'])

# Replace NaN with text in relevant columns (SEX)
df2['Sex'].fillna('Unknown Sex', inplace=True)

# Age group fill NAN values
df2['Age group'].fillna('Unknown age group', inplace=True)

# Renaming dimension columns and slugify where necessary
df2.rename(columns={'Date Column': 'date', 'State': 'state', 'LGA': 'lga',
                    'Sex': 'sex',
                    'Age group': 'Age_group'}, inplace=True)

# Renaming other columns to slugify
df2.rename(columns={'Column 1_option1': 'Column_1_option1', 'Column 1_option2': 'Column_1_option2',
                    'Column 2_option1': 'Column_2_option1', 'Column 2_option2': 'Column_2_option2',
                    'Column 3_option1': 'Column_3_option1', 'Column 3_option2': 'Column_3_option2',
                    'Column 4_option1': 'Column_4_option1', 'Column 4_option2': 'Column_4_option2',
                    'Column 9_option1': 'Column_9_option1', 'Column 9_option2': 'Column_9_option2',
                    'Column 10_option1': 'Column_10_option1', 'Column 10_option2': 'Column_10_option2'}, inplace=True)

df3 = df2

# Create zone dictionary to insert a new column with its appropriate zone
zonedic = {'Kano': 'NW', 'Kaduna': 'NW', 'Sokoto': 'NW', 'Kebbi': 'NW', 'Jigawa': 'NW', 'Katsina': 'NW',
           'Zamfara': 'NW',
           'Bauchi': 'NE', 'Borno': 'NE', 'Yobe': 'NE', 'Gombe': 'NE', 'Taraba': 'NE', 'Adamawa': 'NE',
           'Kwara': 'NC', 'Kogi': 'NC', 'Fct ': 'NC', 'Niger': 'NC', 'Benue': 'NC', 'Plateau': 'NC',
           'Lagos': 'SW', 'Oyo': 'SW', 'Ogun': 'SW', 'Ondo': 'SW', 'Ekiti': 'SW', 'Osun': 'SW',
           'Enugu': 'SE', 'Imo': 'SE', 'Anambra': 'SE', 'Abia': 'SE', 'Ebonyi': 'SE',
           'Rivers': 'SS', 'Akwa-Ibom': 'SS', 'Cross River': 'SS', 'Bayelsa': 'SS', 'Delta': 'SS', 'Edo': 'SS'}

# Map zones to states using zonedic by inserting new column
df3['zone'] = df3['state'].map(zonedic)

# Reorder columns
neworder = ['date', 'zone', 'state', 'lga', 'sex', 'Age_group',
            'Column_1_option1', 'Column_1_option2',
            'Column_2_option1', 'Column_2_option2',
            'Column_3_option1', 'Column_3_option2',
            'Column_4_option1', 'Column_4_option2',
            'Column_9_option1', 'Column_9_option2',
            'Column_10_option1', 'Column_10_option2', ]

df3 = df3.reindex(columns=neworder)

# Export csv
df3.to_csv("/Location/Where/File/Will/Export/df3.csv")
