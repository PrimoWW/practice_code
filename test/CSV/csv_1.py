"""
practice save data in csv
from page 64
为了防止出现空行情况，open要加上newline=""这个参数
完美解决
"""
import csv

csvFile = open("test.csv", "w+", newline='')
try:
    writer = csv.writer(csvFile)
    writer.writerow(['number', 'number plus 2', 'number times 2'])
    for i in range(10):
        writer.writerow((i, i+2, i*3))
finally:
    csvFile.close()