graph= {} 
ans = []
def check_descendents(arr, val = 0):
    for des in graph[arr[0]]:
        if des == arr[1]:
            ans.append('YES '+str(val+1))
            return True
        else:
            return check_descendents([des, arr[1]], val+1)
    
    

if __name__ == "__main__":
    num = None
    while True:
        person = input().strip().split()
        descendents = int(person[1])
        if person[0] == 'STOP':
            num = descendents
            break
        if descendents:
            nextgen = input().strip().split()
            if person[0] not in graph:
                graph[person[0]] = []
            for des in  nextgen:
                graph[des] = []
                graph[person[0]].append(des)
    i = 0
    # print(graph)
    while i < num:
        t = input().strip().split()
        check_descendents(t)
        i+=1
        if len(ans) == i:
            print(ans[-1])
        else:
            ans.append('NO')
            print(ans[-1])

