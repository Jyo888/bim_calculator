# 
weight = 0;
height = 0;
bmi = 0;


print("Enter your height(m)\n");
height = input()

print("Enter your weight(kg)\n")
weight = input()

bmi = float(weight)/float(height)**2
bmi_cal = int(bmi);
print(bmi_cal)
