# LOOPS - TASK

import random
otp = str(random.randint(1000,9999))
print(f"actual otp:{otp}")
attempt = 3
while attempt > 0:
    user_otp = input("Enter OTP:")
    if len(user_otp) != 4:
        print("OTP must be 4 digit number only")
    else:
        if user_otp != otp:
            print("❌ INCORRECT OTP")
            attempt -= 1
        else:
            print("✅ CORRECT OTP - SUCCESS")
            break
else:
    print("Maximum attempts reached, try again after 24 hours")
