from datetime import datetime

age = input("How old are you?")
futureAge = int(age) + (2050 - datetime.now().year)
print("In 2050, you will be ",futureAge, " years old.")