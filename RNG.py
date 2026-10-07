#Random Number Generation
import numpy as np

#Create a 1D array of 10 random heart rates between 80 and 150
heart_rates = np.random.randint(80, 151, 10)

print("Heart rates:", heart_rates)

#Get the first 5 minutes
first_5_minutes = heart_rates[:5]
print("First 5 minutes:", first_5_minutes)





















































#Calculate maximum, minimum and average
maximum = np.max(heart_rates)
minimum = np.min(heart_rates)
average = np.mean(heart_rates)

print("Maximum heart rate:", maximum)
print("Minimum heart rate:", minimum)
print("Average heart rate:", average)

#Identify minutes where heart rate exceeded 120 bpm
minutes_exceeded = np.where(heart_rates > 120)[0] + 1

print("Minutes where heart rate exceeded 120 bpm:", minutes_exceeded)