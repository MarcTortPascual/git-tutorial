import json

item_base=input("indique el item base en ingles: ")
modelo=input("itroduzca el directorio del modelo: ")
num_cmd=input("introduzca el valor de custom model data: ")

item=f"item/{item_base}"

print(item)


cmd={
	"parent": "item/handheld",
	"textures": {
		"layer0": item
	},
	"overrides": [
		{ "predicate": { "custom_model_data": num_cmd}, "model": modelo }
	
	]
}

with open(f"{item_base}.json","w") as volcado:
    json.dump(cmd,volcado,indent=3)