# ATTENDANCE ANALYSIS

import numpy as np
#CREATING A RANDOM ATTENDANCE RECORD FOR 30 DAYS
attendance=np.random.randint(0,2,size=30)
#CALCULATING ATTENDANCE PERCENTAGE
attendace_mean=np.mean(attendance)
percentage=attendace_mean*100
print(f"Attendence percentage: {percentage}%")
#CALCULATING TOTAL ABSENT DAYS
Total_absent=np.count_nonzero(attendance==0)
print(f"Total absent days: {Total_absent}")
#CALCUL\ LONGEST STREAK OF PRESENT DAYS
max_streak = 0
current_streak = 0
for day in attendance:
    if day == 1:
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0

print("Longest Present Streak:", max_streak)
penalty=attendance.copy()
penalty[penalty==0]=-1
total_penalty=np.sum(penalty)
print(f"Total penalty points: {total_penalty}")

