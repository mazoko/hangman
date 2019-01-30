# (1)モジュールをインポートして使ってみる
import statistics

list = [1, 55, 33, 12, 46, 33, 2]
low = statistics.median_low(list)
high = statistics.median_high(list)

print("median_low: " + str(low))
print("median_high: " + str(high))