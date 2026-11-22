def analyze_scores(*scores) :
    if len(scores)!=0 :
        print("Сумма ",sum(scores)," Количество ",len(scores)," Среднее ",sum(scores)/len(scores))
        return sum(scores),len(scores),sum(scores)/len(scores)
    else : 
        print("Сумма ",sum(scores)," Количество ",len(scores)," Среднее ",0)
        return sum(scores),len(scores),0
def print_report(team_name,**info):
    print(team_name,info)
analyze_scores(8,10,7,9)
analyze_scores(5,5)
analyze_scores()
a = {"Coach":"Boneca Ambalabu","City":"Malaya Tokmachka"}
print_report("Комета",**a)