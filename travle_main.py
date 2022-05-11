'''from tokenize import triple_quoted
import travle.tailand
trip_to = travle.tailand.ThailandPackage()
trip_to.detail()

from travle.tailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travle.vietnam import VietnamPackage
trip_to = VietnamPackage()
trip_to.detail()'''

'''from travle import *
trip_to = vietnam.VietnamPackage()  # __init__ 파일에 등록해주어야 사용 가능
trip_to.detail()

trip_to2 = thailand.ThailandPackage()
trip_to2.detail()'''

from travle import *
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))