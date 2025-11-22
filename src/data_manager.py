import pandas as pd
import os

data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'student_marks.csv')

def load_data():
    # loading our dataset here
    if not os.path.exists(data_file):
        return pd.DataFrame()
    return pd.read_csv(data_file)

def get_st_data(student_id):
    # here we are returning marks only for specified students
    df = load_data()
    if df.empty:
        return []
    
    # genrating student id
    student_record = df[df['Student_ID'] == student_id]
    return student_record.to_dict('records')

def get_st_name(student_id):
    # with this we can get student name and info using student id
    df = load_data()
    if df.empty: 
        return "Unknown"
    
    result = df[df['Student_ID'] == student_id]['Name'].unique()

    if len(result) > 0:
        return result[0]
    else:
        "Unknown"

def add_record(student_id, name, sem, sub, cred, marks):
    # here we can add new record for the existing student
    nw_row = pd.DataFrame([[student_id, name, sem, sub, cred, marks]], 
                           columns=["Student_ID", "Name", "Semester", "Subject", "Credits", "Marks"])
    # here we are removing the header 
    nw_row.to_csv(data_file, mode='a', header=not os.path.exists(data_file), index=False)
    return True