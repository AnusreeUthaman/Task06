#Fitness
calories_burned=[2000,3000,4000,5000,2000,1000.2000]
calories_intake=[1500,2000,1800,2500,1500,1400,1800]
D=[]
day=["Monday","Tuesday","Wednesday","Thursday","Friday","saturday","Sunday"]
print("Monday-Nil-First Reading")
for i in range(len(calories_burned)):
    D.append(calories_burned[i]-calories_intake[i])
x=D[0]
for i in range(1,len(D)):
    if D[i]<x:
        print(f"{day[i]}-decreased")
    if D[i]>x:
        print(f"{day[i]}-increased")
    x=D[i]
most={"Monday":2000,
      "Tuesday":3000,
      "Wednesday":4000,
      "Thursday":5000,
      "Friday":2000,
      "saturday":1000,
      "Sunday":2000}
max_day=max(most,key=most.get)
print(f"Most Active Day of the Week:{max_day}")
