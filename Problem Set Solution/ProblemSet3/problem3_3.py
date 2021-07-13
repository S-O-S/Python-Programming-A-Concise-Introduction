def problem3_3(month, day, year):
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
    month_list=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month_input=int(month)-1
    print(month_list[month_input], str(day) + ",", year)