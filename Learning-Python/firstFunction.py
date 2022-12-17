hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

def computepay(h, r):
    if h > 40 :
        reg = h * r
        otp = (h - 40.0) * (r * 0.5)

        xp = reg + otp
    else :
        xp = h * r
    return xp

p = computepay(h, r)

print("Pay", p)