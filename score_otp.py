import argparse
from scipy.spatial.distance import hamming

parser = argparse.ArgumentParser(description="Simple code to score the difficulty of an OTP.")
parser.add_argument('-o', '--otp', required=True, help="Enter the One-time Password")

args = parser.parse_args()

otp = [int(x) for x in list(args.otp)]

# print (pdist(otp))
print (otp)

print (hamming(otp))