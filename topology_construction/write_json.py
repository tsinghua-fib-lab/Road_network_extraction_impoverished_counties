import json
import pandas as pd
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = None
import numpy as np

district = 'test'
year = 2017
pred_path = 'x'
csv_path = 'Y'

# district_csv = pd.read_csv()

min_lat = 35.28150065789119
min_lng = 103.3868408203125
max_lat = 35.634976650677295
max_lng = 103.8592529296875

# pred_img = Image.open(pred_path)
# nb_rows, nb_cols = np.array(pred_img).shape[0], np.array(pred_img).shape[1]
nb_rows = 10112
nb_cols = 11008

dataset_name = 'test_rn_pred_full_'+ district
test_tile_row_max = 79 #nb_rows/128
test_tile_col_max = 86 #nb_cols/128

data = {
    "dataset": {
    "dataset_name": dataset_name,
    "min_lat": min_lat,
    "min_lng": min_lng,
    "max_lat": max_lat,
    "max_lng": max_lng, 
    "nb_rows": nb_rows,
    "nb_cols": nb_cols
  },
  "feature_extraction": {
    "tile_pixel_size": 128,
    "test_tile_row_min": 0,
    "test_tile_row_max": test_tile_row_max,
    "test_tile_col_min": 0,
    "test_tile_col_max": test_tile_col_max 
  },
  "topology_construction": {
    "link_radius": 50,
    "alpha": 1.4,
    "min_supp": 5
  }
}

# 指定要写入的文件名
file_name = 'test_rn_pred_full_'+ district +'.json'

# 写入 JSON 文件
with open(file_name, 'w') as json_file:
    json.dump(data, json_file)


#{
#   "dataset": {
#     "dataset_name": "test_rn_OSM_full_guanghexian",
#     "min_lat": 35.28150065789119,
#     "min_lng": 103.3868408203125,
#     "max_lat": 35.634976650677295,
#     "max_lng": 103.8592529296875, 
#     "nb_rows": 10112,
#     "nb_cols": 11008
#   },
#   "feature_extraction": {
#     "tile_pixel_size": 128,
#     "test_tile_row_min": 0,
#     "test_tile_row_max": 79,
#     "test_tile_col_min": 0,
#     "test_tile_col_max": 86
#   },
#   "topology_construction": {
#     "link_radius": 50,
#     "alpha": 1.4,
#     "min_supp": 5
#   }
# }


# # 构建一个字典
# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }