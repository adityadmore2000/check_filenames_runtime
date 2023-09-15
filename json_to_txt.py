# import json
# import os

# current_script = os.path.basename(__file__)

# def json_to_txt():
    
#     for file_name in os.listdir("."):
#         if file_name == current_script:
#             continue

#         basename= os.path.basename(file_name).split(".")[0]
#         output_dir = "C:\\Users\\sez5954\\source\\repos\\projects\\Rameshwar_Sir_tasks\\duct_rectangular\\txt_labels"
#         output_file = r"{}.txt".format(basename)

#         f = open(file_name,"r")
#         data = json.load(f)

#         # shapes stored in array
#         for i in range(len(data["shapes"])):
#             # every polygon has label
#             label = data["shapes"][i]["label"]
#             index = 0

#             width = data["imageWidth"]
#             height = data["imageHeight"]

#             points = data["shapes"][i]["points"]

#             # x/height, y/width
#             normalized = []

#             for i in range(len(points)):
#                 x = points[i][0]
#                 y = points[i][1]
#                 x_normalized = x/height
#                 y_normalized = y/width

#                 normalized.append(x_normalized)
#                 normalized.append(y_normalized)
#             if label=="elbow_rect":
#                 index=1
#             elif label=="fittings_rect":
#                 index = 2
#             elif label=="duct_rect":
#                 label = 3
#             normalized.insert(0,index)
#             with open(r"{}\\{}".format(output_dir,output_file),"a") as output:
#                 output.writelines("\n{}".format(str(normalized)))

# json_to_txt()

import json
import os
import sys

def json_to_txt(input_dir,output_dir):
    for file_name in os.listdir():

        base_name = os.path.basename(file_name).split(".")[0]
        output_file = r"{}.txt".format(base_name)
        file_of_interest = os.path.join(os.path.curdir,file_name)
        try:
            with open(file_of_interest, "r") as f:
                data = json.load(f)
            with open(os.path.join(output_dir, output_file), "a") as output:
                for shape in data["shapes"]:
                    label = shape["label"]
                    points = shape["points"]
                    index = 0
                    width = data["imageWidth"]
                    height = data["imageHeight"]

                    normalized = []

                    for point in points:
                        x = point[0]
                        y = point[1]
                        x_normalized = x / width
                        y_normalized = y / height

                        normalized.append(x_normalized)
                        normalized.append(y_normalized)

                    if label == "BoxSteel":
                        index = 1

                    normalized.insert(0, index)
                    output.writelines("\n{}".format(str(normalized)))
        except Exception as  e:
            print("Exception in {} :: {}".format(file_of_interest, e))



if len(sys.argv)==3:
    json_to_txt(sys.argv[1],sys.argv[2])
else:
    print("some arguments are missing")