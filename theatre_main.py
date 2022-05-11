import theatre_module
theatre_module.price(3)
theatre_module.price_morning(4)
theatre_module.price_soldier(10)

import theatre_module as tm #클래스명에 별명 가능
tm.price(3)
tm.price_morning(4)
tm.price_soldier(10)

from theatre_module import * #별도의 클래스명 없이 함수를 바로 쓸 수 있음
price(4)
price_morning(2)
price_soldier(10)

from theatre_module import price_morning, price #원하는 함수만 사용 가능
price(3)
price_morning(20)

from theatre_module import price_soldier as sp
sp(5)