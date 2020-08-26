def computepay(h,r):
    if h > 40:
        pay = 40 * r
        pay += (h - 40) * 1.5 * r
    else:
        pay = h * r
    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print("Pay",p)