color_dictionary = {
	"red": (255, 0, 0),
	"green": (0, 255, 0),
	"blue": (0, 0, 255),
	"magenta": (255, 0, 255),
	"cyan": (0, 255, 255),
	"yellow": (255, 255, 0)
}

tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141, 125, 83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35, 22, 19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}

print("The red channel of Clay Creek is: ")
print(tineye_sample["result"][0]["color"][0])
print("the blue channel of Seal Brown is: ")
print(tineye_sample["result"][1]["color"][2])

# print("The blue channel of magenta has a value" + str(color_dictionary["magenta"][2]))
# print("The green channel of yellow has a value" + str(color_dictionary["yellow"][1]))
# print("The red channel of cyan has a value" + str(color_dictionary["cyan"][0]))

# print("The value of every color with an 'e' is: ")
# for color, value in color_dictionary.items():
# 	if 'e' in color:
# 		print(color + ":" + str(value))
