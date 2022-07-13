# employee50000

python3 manage.py runserver 8050


первая часть полностью создано
с 5 уровнями
owner(1)
|   
admin(1)---------------
|                      \
co-admin(1)          tech-admin(1)
|                       |
manger(1)              tech-worker(25.000)
|
worker(25.000)

во втором части созданы пункты 1,2,3,4,5
6&7 пункты сделать не было времени(
when search -------> on URL
http://127.0.0.1:8050/search/?search=John


в 8 части получиться с помощью, api.views -> class EmployeeList/Search 
поменять значении generics.ListCreateAPIView
вместо generics.ListAPIView
