import sys
print(sys.argv)

# Calculates cost of meal with tax and tip

def calculateTip(meal,tip):
    meal = float(meal)
    tip = float(tip)
    tax = 0.075

    meal += meal * tax
    total = meal + meal * tip

    return total


meal = float( sys.argv[1])
tax = 0.075
tip = float( sys.argv[2] )

meal += meal * tax
total1 = meal + meal * tip
print("%.2f" % total1)


total2 = calculateTip(sys.argv[1],sys.argv[2])
print("%.2f" % total2)


