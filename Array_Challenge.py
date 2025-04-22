# Create an array

mySentence = "I love the Land Rover model"

models=["Range Rover", "Velar", "Discovery"]

def model_function():
    print ("{} {}".format(mySentence, models[0])) # The number determines what model is printed based on sequence

model_function()


# Loop

mySentence = "I love the Land Rover model"

models=["Range Rover", "Velar", "Discovery"]

for x in models:
    print(x)

def model_function():
    print("{} {}".format(mySentence, models[1]))

model_function()

# Count() method

thistuple = (1, 5, 9, 3, 8, 9, 1, 3, 7, 3, 3)
x = thistuple.count(3)# It counts the amount of "3's" in the tuple In this case there are 4
print(x)

# Sort() method

models = ["Range Rover", "Velar", "Discovery"]
models.sort()
print(models)
