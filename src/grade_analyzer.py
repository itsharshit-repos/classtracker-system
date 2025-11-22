import numpy as np
# calculating gpa
def cal_gpa(student_record):

    sem_data = {}
    
    for r in student_record:
        sem = r['Semester']
        if sem not in sem_data:
            sem_data[sem] = {'points': 0, 'credits': 0}
            
        gr_point = r['Marks'] / 10
        sem_data[sem]['points'] += gr_point * r['Credits']
        sem_data[sem]['credits'] += r['Credits']
        
    result = {}
    for sem, data in sem_data.items():
        if data['credits'] > 0:
            result[sem] = round(data['points'] / data['credits'], 2)
    return result

def predict_next_sem(gpa_result):
    if not gpa_result:
        return 0.0
    gpas = list(gpa_result.values())
    if len(gpas) >= 3: 
        prediction = np.mean(gpas[-3:])
    else:
        np.mean(gpas)
    return round(prediction, 2)