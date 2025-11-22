import data_manager
import grade_analyzer
import visualizer
import sys
import time 

def cal_cls_avg():
    df = data_manager.load_data() 
    
    if df.empty:
        return {}

    # dictionaries to hold calculations
    sem_total_marks = {}
    sem_counts = {}

    # we are doing looping through dataframe rows
    for index, row in df.iterrows():
        s = row['Semester']
        m = row['Marks']

        if s not in sem_total_marks:
            sem_total_marks[s] = 0
            sem_counts[s] = 0
        
        sem_total_marks[s] += m
        sem_counts[s] += 1

    # calculating final avg
    final_avg = {}
    for s in sem_total_marks:
        avg_mark = sem_total_marks[s] / sem_counts[s]
        final_avg[s] = round(avg_mark / 10, 2)
    return final_avg

def main():
    print("\n")
    print("==========================================")
    print(" CLASSTRACK: Academic Management System")
    print("==========================================")
    
    # Login phase
    curr_id = 0
    is_logged_in = False

    while not is_logged_in:
        try:
            raw_in = input("Enter Student ID to Login (e.g., 101): ")

            if len(raw_in) == 0:
                continue 
            
            curr_id = int(raw_in)
            is_logged_in = True
            
        except ValueError:
            print("Error: Please enter a valid numeric ID.")

    # finding student details
    print("Verifying ID...")
    time.sleep(0.5) 
    
    student_name = data_manager.get_st_name(curr_id)
    
    if student_name == "Unknown":
        print("Error: Student ID not found in database")
        return

    print(f"\nLogin Successful! Welcome, {student_name}.")
    
    app_running = True
    
    while app_running:
        print("\n" + "-"*30)
        print(f" Dashboard: {student_name}")
        print("-"*30)
        print("1. View my Report Card")
        print("2. Visualize my Growth")
        print("3. Compare with Class Average")
        print("4. Compare with a Friend")
        print("5. Predict future GPA")
        print("6. Add New Marks")
        print("7. Exit")
        
        choice = input("Select Option (1-7): ")
        
        # Load user data 
        records = data_manager.get_st_data(curr_id)
        my_gpas = grade_analyzer.cal_gpa(records)

        if choice == '1':
            print(f"\n[Transcript: {student_name}]")
            if len(my_gpas) == 0:
                print("No records found of student")
            
            for sem, gpa in my_gpas.items():
                print(f"Semester {sem}: {gpa} SGPA")

        elif choice == '2':
            if len(my_gpas) > 0:
                print("Generating visual graph...")
                visualizer.plot_gpa_graph(my_gpas, student_name)
            else:
                print("No data to visualize")

        elif choice == '3':
            # using the manual function we wrote above
            cls_avg  = cal_cls_avg()
            visualizer.plt_compare(my_gpas, cls_avg )

        elif choice == '4':
            # Peer Comparison Logic
            try:
                # taking input individually to avoid crash
                fr_input = input("Enter Friend's Student ID: ")
                fr_id = int(fr_input)
                
                if fr_id == curr_id:
                    print("You cannot compare with yourself!")
                else:
                    # getting friend details
                    friend_name = data_manager.get_st_name(fr_id)
                    
                    if friend_name == "Unknown":
                        print(f"Student ID {fr_id} not found.")
                    else:
                        print(f"Fetching data for {friend_name}...")
                        friend_records = data_manager.get_st_data(fr_id)
                        friend_gpas = grade_analyzer.cal_gpa(friend_records)
                        
                        # graph: visualizer
                        visualizer.plt_peer_compare(my_gpas, friend_gpas, student_name, friend_name)

            except ValueError:
                print("Invalid ID format. Please enter numbers only.")

        elif choice == '5':
            pred = grade_analyzer.predict_next_sem(my_gpas)
            print(f"\nBased on your trend, predicted next GPA: {pred}")

        elif choice == '6':
            try:
                print("--- Add New Subject Record ---")
                s = int(input("Semester: "))
                sub = input("Subject Name: ")
                c = int(input("Credits (1-4): "))
                m = int(input("Marks (0-100): "))
                
                if m < 0 or m > 100:
                    print("Marks must be between 0 and 100.")
                else:
                    print("Saving...")
                    data_manager.add_record(curr_id, student_name, s, sub, c, m)
                    print("Record Added Successfully.")
                    
            except ValueError:
                print("Invalid input. Please enter numbers for Sem/Credits/Marks.")

        elif choice == '7':
            print("Logging out... Good luck!")
            app_running = False 
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()