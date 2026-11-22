def ticket_total(price=12,**count) :
    return count["Количество"]*price
def final_price(is_school_group=False,**count) :
    if is_school_group==True :
        return ticket_total(**count) - (ticket_total(**count)*0.25)
    if is_school_group==False :
        return ticket_total(**count)
a = {"Количество":3}
b = {"Количество":2}
c = {"Количество":4}
print("Цена за 3 обычных билета : ",final_price(**a),"руб. Цена за 4 школьных билета : ",final_price(is_school_group=True,**c),"руб. Цена за 2 обычных билета с ценой 15 : ",ticket_total(price = 15,**b),"руб.")