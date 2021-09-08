
import psycopg2 as pg2
import time
import numpy as np

#conn = pg2.connect(database='rental', user='postgres',password='password1')
conn = pg2.connect(user="postgres",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="rental")
cur = conn.cursor()
cur.execute("SELECT * FROM payment")
cur.fetchone()
data = cur.fetchmany(10)
#print(data)
start_time = time.time()
sum = 0;
for num in range(100000000):
    sum = sum+num

print("sum =",sum)
end_time = time.time()
pyhton_time = end_time - start_time
print("Time Taken with Pyhton = ", pyhton_time)

start_time1 = time.time()
sum1 = 0;
number = np.arange(100000000)
sum1 = np.sum(number, dtype=np.uint64)


print("sum1 =",sum1)
end_time1 = time.time()
np_time = end_time1 - start_time1
print("Time Taken with numpy = ", np_time)
def add(num1, num2):
    return num1+num2

print(add(3,4))