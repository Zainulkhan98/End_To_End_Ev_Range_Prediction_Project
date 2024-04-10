from ydata_profiling import ProfileReport
import pandas as pd

# Load the data
df = pd.read_csv('F:\\Users\DELL\PycharmProjects\End_To_End_Ev_Range_Prediction_Project\Data\Electric_Vehicle_Population_Data.csv')
df = pd.DataFrame(df)

# Generate the report
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
profile.to_file("EDA_Report.html")
# Open the report in the browser
#Just drag and drop the EDA_Report.html file to the browser
# OR download the file from github and open it in the browser

