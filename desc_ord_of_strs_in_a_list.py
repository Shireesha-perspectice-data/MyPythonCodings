def fun(cars):
	cars.sort(reverse=True)  # Descending order of the alphabatically
	#cars.sort(reverse=False) # Ascending order of the alphabatically
	return cars
print(fun(["Hyundai Motor","Maruthi","BMW","VM"]))