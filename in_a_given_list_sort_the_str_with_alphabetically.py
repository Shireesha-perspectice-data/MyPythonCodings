def fun(str):
	return len(str)

cars=["Wagon","Vivo","BMW","Tata","Maruthi Suzuki"]
cars.sort(key=fun)
print(cars)