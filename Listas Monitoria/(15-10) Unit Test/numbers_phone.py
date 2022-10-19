import re
def number_phone_br(number_phone):
    number_phone = str(number_phone)
    number_phone =  re.sub("[^0-9]+","", number_phone)
    if len(number_phone)<9:
        raise TypeError
        
    if len(number_phone)== 9  or len(number_phone)== 8:
        number_phone = "21"+number_phone

    if number_phone[-11:-9] == "21":
        number_phone =  number_phone[-11:]
    if number_phone[-10:-8] == "21":
        number_phone =  number_phone[-10:]
    
    number_phone = int(number_phone)
    return number_phone

