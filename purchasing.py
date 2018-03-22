sup = []
sups_mark = []
total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0

while True:
    stop = input("enter stop if you want to stop: ")
    if stop.lower() != "stop":
        criteria = input("please enter your criteria: ")
        weight = int(input("please enter the weight of the criteria: "))
        bench = int(input("please enter the score(pt. scale): "))
        while True:
            sup_name = input("enter supplier name or q to go to other criteria: ")
            if sup_name.lower() != "q":
               score = int(input("enter score: "))
               res = (weight * score)/bench
               x = res
               sups_mark.append(x)
               sup.append(sup_name)
               total[i] += x
               i += 1
               print(sup_name,x)
            else:
                max_value = max(sups_mark)
                indx = sups_mark.index(max_value)
                name = sup[indx]
                sups_mark = []
                i = 0
                print("supplier:",name,"\n","has the highest value for this criteria:",max_value)
                break
    else:
        maxima = max(total)
        inx = total.index(maxima)
        nam = sup[inx]
        print("supplier:",nam,"is the best supplier with a total value of:",maxima)
        break
