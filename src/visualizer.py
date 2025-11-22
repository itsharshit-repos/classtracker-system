import matplotlib.pyplot as plt

def plot_gpa_graph(gpa_result, student_name):

    if not gpa_result:
        print("No data available to plot")
        return

    # Sorting our data by semester
    semester = sorted(gpa_result.keys())

    gpas = [gpa_result[s] for s in semester]
    
    plt.figure(figsize=(8, 5))
    
    # Plotting the line
    plt.plot(semester, gpas, marker='o', color='#2c3e50', linestyle='-', linewidth=2, label=student_name)
    
    # Adding a reference line for difference
    plt.axhline(y=8.5, color='green', linestyle='--', alpha=0.3, label='Distinction (8.5)')
    
    plt.title(f'Academic Performance Trend: {student_name}')
    plt.xlabel('Semester')
    plt.ylabel('GPA')
    plt.ylim(0, 10)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    print("Displaying personal growth graph...")
    plt.show()

def plt_compare(student_gpa, cls_avg_gpa):

    if not student_gpa:
        print("No data to compare.")
        return

    sems = sorted(student_gpa.keys())
    
    s_vals = [] 
    for s in sems:
        s_vals.append(student_gpa[s])

    # getting class average for this semester (default to 0 if missing)
    c_vals = []
    for s in sems:
        val = cls_avg_gpa.get(s, 0)
        c_vals.append(val)

    x = range(len(sems))
    
    plt.figure(figsize=(10, 6))
    
    # Bar for Student
    plt.bar([i - 0.2 for i in x], s_vals, width=0.4, label='You', color='skyblue')
    # Bar for Class Average
    plt.bar([i + 0.2 for i in x], c_vals, width=0.4, label='Class Avg', color='gray', alpha=0.7)
    
    plt.xticks(x, [f"Sem {s}" for s in sems])
    plt.title('Performance Comparison: You vs Class Average')
    plt.ylabel('GPA')
    plt.ylim(0, 10)
    plt.legend()
    
    print("Displaying class comparison chart...")
    plt.show()

def plt_peer_compare(my_gpa, friend_gpa, my_name, friend_name):
    # Combining semester from both to make sure the graph captures everything
    all_sems = sorted(set(list(my_gpa.keys()) + list(friend_gpa.keys())))
    
    if not all_sems:
        print("No common semester found to compare.")
        return
    
    my_val_list = []
    for s in all_sems:
        val = my_gpa.get(s, None)
        my_val_list.append(val)
        
    frnd_val_list = []
    for s in all_sems:
        val = friend_gpa.get(s, None)
        frnd_val_list.append(val)

    plt.figure(figsize=(9, 5))
    
    # Ploting Your Line 
    plt.plot(all_sems, my_val_list, marker='o', linewidth=2, color='blue', label=f"{my_name} (You)")
    
    # Ploting Friends Line
    plt.plot(all_sems, frnd_val_list, marker='s', linewidth=2, color='orange', linestyle='--', label=friend_name)
    
    plt.title(f'Head-to-Head Analysis: {my_name} vs {friend_name}')
    plt.xlabel('Semester')
    plt.ylabel('GPA')
    plt.ylim(0, 10)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    print(f"Displaying comparison graph: You vs {friend_name}...")
    plt.show()