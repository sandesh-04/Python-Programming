birth_year = input("Birth year: ")
print(type(birth_year))    # String

# age = 2019 - birth_year   # it will give error because we are - int an str val

# type conversion => converting the string val to integer
age = 2019 - int(birth_year)
print(type(age))
print(age)    # 37


# whenever we take input value from user that val is treated as integer

#convert the weight from pound to kilogram
weight_lbs = input("Weight(lbs): ")
weight_kgs = float(weight_lbs) * 0.45
print("weight in kgs is : " + weight_kgs)