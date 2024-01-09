from nudenet import NudeDetector
import os
nude_detector = NudeDetector()
# all_labels = {
#     "FEMALE_GENITALIA_COVERED":0,
#     "FACE_FEMALE":0,
#     "BUTTOCKS_EXPOSED":0,
#     "FEMALE_BREAST_EXPOSED":0,
#     "FEMALE_GENITALIA_EXPOSED":0,
#     "MALE_BREAST_EXPOSED":0,
#     "ANUS_EXPOSED":0,
#     "FEET_EXPOSED":0,
#     "BELLY_COVERED":0,
#     "FEET_COVERED":0,
#     "ARMPITS_COVERED":0,
#     "ARMPITS_EXPOSED":0,
#     "FACE_MALE":0,
#     "BELLY_EXPOSED":0,
#     "MALE_GENITALIA_EXPOSED":0,
#     "ANUS_COVERED":0,
#     "FEMALE_BREAST_COVERED":0,
#     "BUTTOCKS_COVERED":0,
# }
# path = "output_frames"
# filtered_classes={}
# filtered_classes_avg={}
# file_list = os.listdir(path)
# for image in file_list:
#     data = nude_detector.detect(path + "/" + image)
#     for each in data:
#         dataclass=each['class']
#         datascore=each['score']
#         if dataclass=="BUTTOCKS_EXPOSED" or dataclass == "FEMALE_BREAST_EXPOSED" or dataclass == "FEMALE_GENITALIA_EXPOSED" or dataclass == "MALE_BREAST_EXPOSED" or dataclass=="ANUS_EXPOSED" or dataclass == "BELLY_EXPOSED" or dataclass == "MALE_GENITALIA_EXPOSED":
#            if dataclass in filtered_classes:
#                filtered_classes[dataclass]+=datascore
#                filtered_classes[dataclass+"_COUNT"]+=1
#                filtered_classes_avg[dataclass]=filtered_classes[dataclass]/filtered_classes[dataclass+"_COUNT"]
#            else:
#                filtered_classes[dataclass]=datascore
#                filtered_classes[dataclass+"_COUNT"]=1
#                filtered_classes_avg[dataclass]=filtered_classes[dataclass]/filtered_classes[dataclass+"_COUNT"]

# print("-------------------------------Result--------------------------------")
# print(filtered_classes_avg)

data = nude_detector.detect("../image.jpg")
for each in data:
    print(each['class']+": "+str(each['score']))

