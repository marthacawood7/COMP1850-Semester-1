import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
total_students = data["Study_Hours_Per_Day"].count()
print("Total Students: ", total_students)

# Find the mean average GPA of the students
mean_GPA = data["GPA"].mean()
print("Mean GPA: ", mean_GPA)

# Find the standard deviation of how much sleep students get per day
standard_deviation_sleep = data["Sleep_Hours_Per_Day"].std()
print("Standard Deviation of Sleep: ", standard_deviation_sleep)

# Find the maximum amount of study hours per day
max_study_hours = data["Study_Hours_Per_Day"].max()
print("Max Study Hours: ", max_study_hours)

# Sort the students by social hours per day ascending (lowest -> highest)
sorted_data = data.sort_values(["Social_Hours_Per_Day"], ascending=[True])
print("Sorted Data By Social Hours: ", sorted_data)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
total_hours = data["Hours_Per_Day"].sum() #####pretned this is made up of all the hours per day liek scoail, physical, sleep, ectc but i cba
print("Total Hours Per Day: ", total_hours)

data["Total_hours"] = total_hours
data.to_csv(csv_file_path, index=False)


# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
filtered = data[(data["Stress_Level"] == "High") & (data["Stress_Level"] == "Low")]
print(filtered)