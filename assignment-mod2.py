'''2.	An App for Mobile hosting provider charges- $0.51 per hour how much does it cost to operator per day, per week, per month? how many days can i operate one server with$918?'''
a=0.51
d=24*a
w=24*7*a
m=24*30*a
k=918/a
print(f"it cost ${a} for an hour for the operator.")
print(f"it cost ${d} for a day for the operator.")
print(f"it cost ${w} for a week for the operator.")
print(f"it cost ${m} for a month for the operator.")
print(f"you can operate for {k} days with $918.")