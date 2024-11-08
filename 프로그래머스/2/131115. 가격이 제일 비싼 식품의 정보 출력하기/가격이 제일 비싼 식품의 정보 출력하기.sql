SELECT *
from FOOD_PRODUCT
where PRICE = (select max(price)
              from FOOD_PRODUCT);