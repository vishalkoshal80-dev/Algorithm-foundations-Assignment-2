
def fractional_knapsack(values, weights, capacity):
    items = sorted([(v/w,v,w) for v,w in zip(values,weights)], reverse=True)
    total=0
    for r,v,w in items:
        if capacity>=w:
            total+=v
            capacity-=w
        else:
            total+=r*capacity
            break
    return total

def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    result=[activities[0]]
    last_finish=activities[0][1]
    for i in activities[1:]:
        if i[0]>=last_finish:
            result.append(i)
            last_finish=i[1]
    return result

if __name__=="__main__":
    print("Knapsack:", fractional_knapsack([60,100,120],[10,20,30],50))
    print("Activities:", activity_selection([1,3,0,5,8,5],[2,4,6,7,9,9]))
