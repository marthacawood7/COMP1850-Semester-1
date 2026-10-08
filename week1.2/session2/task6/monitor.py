# Week 1.2, Session 2: Task 6


  
temperature = int(input("Input temperature: "))
pressure = int(input("Input pressure"))
status = int(input("Input operational status - 1/0"))
       

if temperature >= 80:
    temperatureResult = "High"
    #status = "Shut down machine"
elif 50 < temperature < 80 :
    temperatureResult = "Safe"
    #status = "No action required"
else:
    temperatureResult = "Low"
    #status = "No action required"
     

if pressure > 100:
    pressureResult = "High"
    #status = "Maintenance required"

elif 70 < pressure < 101:
    pressureResult = "Stable"
    #status = "No action required"

else:
    pressureResult = "Low"
    status = "Operating normally"


if status == 1:
    if temperatureResult == "High" or pressureResult == "High":
        print("Machine is running in unsafe conditions and its recommended to shut it down")

    else:
        print("Machine is running normally")

elif status == 0:
    print("The machine is stopped and no immediate action is needed")

else:
    print("Enter either 1 or 0")
