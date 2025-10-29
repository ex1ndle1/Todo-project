from collections import namedtuple





###############1#####
Cars = namedtuple(
    'Car', ['brand', 'model', 'year'])
car1 = Cars('Ford', 'f3',  1904)
car2 = Cars('Niva', 'Model 1983', 1983)


print(car1.brand)

#####################2####################


city = namedtuple ('City',['name','population','country'])


city1 = city('Moscow', 11000000,'Russia')
city2 = city('Amsterdam',1200000,'Netherlands')

print(city2.country)
########################3#############

courses =  namedtuple('Courses',['name','payment','teacher'])

corse1 = courses('Java',2400000,'Bob')
course2 = courses('Python',1400000,'Jasur')

print(course2.payment)