def first_ok(i,activities,cranky):
    for t in cranky:
        if t<activities[i][0]:
            return False
    return True

def compatible(j,i,activities,cranky):
    if activities[j][1]>activities[i][0]:
        return False
    for t in cranky:
        if t>activities[j][1] and t<activities[i][0]:
            return False
    return True

def last_ok(i,activities,cranky):
    for t in cranky:
        if t>activities[i][1]:
            return False
    return True

def schedule_activities(activities,cranky):
    if len(cranky)==0:
        return 0
    
    activities=sorted(activities, key=lambda a: a[1])
    n=len(activities)
    INF=float('inf')
    f=[INF]*n
    ans=INF

    for i in range(n):
        if first_ok(i,activities,cranky):
            best= 0
        else:
            best=INF
            
        for j in range(i):
            if compatible(j,i,activities,cranky):
                best=min(best,f[j])
        f[i]=activities[i][2]+best

        if last_ok(i,activities,cranky):
            ans=min(ans,f[i])
            
    return ans

activities=[(480,600,5),(510,570,3),(630,690,4),(480,720,20),(690,750,1)]
cranky=[540,660]

print(schedule_activities(activities,cranky))
print(schedule_activities([(8, 9, 2), (10, 11, 3), (12, 13, 4)],[8.5, 10.5, 12.5]))
print(schedule_activities([(8, 9, 2), (10, 11, 3), (12, 13, 4)],[]))