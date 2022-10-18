import re
def number_phone_br(number_phone):
    if type(number_phone) == int:
        number_phone = str(number_phone)
    number_phone =  re.sub("[^0-9]+","", number_phone)
    if len(number_phone)<9:
        raise TypeError
    if len(number_phone)== 9  :
        number_phone = "21"+number_phone
    if len(number_phone)>9:
        number_phone =  number_phone[-11:]
    
    number_phone = int(number_phone)
    return number_phone

