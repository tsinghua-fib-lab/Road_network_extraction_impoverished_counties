import sys
sys.path.append('../')
sys.path.append('../tptk/')
import argparse
import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()
# export CV_IO_MAX_IMAGE_PIXELS=1099511627776
import cv2
from tptk.common.mbr import MBR
from tptk.common.grid import Grid
from tptk.common.road_network import load_rn_shp
from topology_construction.graph_extraction import GraphExtractor
from topology_construction.link_generation import LinkGenerator
from topology_construction.custom_map_matching import CustomMapMatching
from topology_construction.map_refinement import MapRefiner
import json
import os
import pandas as pd
import numpy as np
from multiprocessing import Pool
from functools import partial
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = None
from skimage import morphology,draw
import argparse


def get_test_mbr(conf):
    dataset_conf = conf['dataset']
    feature_extraction_conf = conf['feature_extraction']
    min_lat, min_lng, max_lat, max_lng = dataset_conf['min_lat'], dataset_conf['min_lng'], \
                                         dataset_conf['max_lat'], dataset_conf['max_lng']
    whole_region_mbr = MBR(min_lat, min_lng, max_lat, max_lng)
    whole_region_grid = Grid(whole_region_mbr, dataset_conf['nb_rows'], dataset_conf['nb_cols'])
    test_row_min, test_col_min, test_row_max, test_col_max = feature_extraction_conf['test_tile_row_min'], \
                                                             feature_extraction_conf['test_tile_col_min'], \
                                                             feature_extraction_conf['test_tile_row_max'], \
                                                             feature_extraction_conf['test_tile_col_max']
    tile_pixel_size = feature_extraction_conf['tile_pixel_size']
    test_row_min_idx = test_row_min * tile_pixel_size
    test_row_max_idx = test_row_max * tile_pixel_size
    test_col_min_idx = test_col_min * tile_pixel_size
    test_col_max_idx = test_col_max * tile_pixel_size

    test_region_lower_left_mbr = whole_region_grid.get_mbr_by_matrix_idx(test_row_max_idx, test_col_min_idx)
    test_region_min_lat, test_region_min_lng = test_region_lower_left_mbr.max_lat, test_region_lower_left_mbr.min_lng
    test_region_upper_right_mbr = whole_region_grid.get_mbr_by_matrix_idx(test_row_min_idx, test_col_max_idx)
    test_region_max_lat, test_region_max_lng = test_region_upper_right_mbr.max_lat, test_region_upper_right_mbr.min_lng
    test_region_mbr = MBR(test_region_min_lat, test_region_min_lng, test_region_max_lat, test_region_max_lng)
    return test_region_mbr


def transform_graph_main(year, district,county_idx):
    
    if county_idx<10:
        df = pd.read_csv('../data/district_boundary_long_lat3_10.csv')
    else:
        df = pd.read_csv('../data/district_boundary_long_lat3_20.csv')

    conf_path = '../data/json/test_rn_OSM_full_'+district+'.json'

    if not os.path.exists('../data/tdrive_sample/results_pred_'+district+'_'+str(year)+'/'):
        os.makedirs('../data/tdrive_sample/results_pred_'+district+'_'+str(year)+'/')

    results_path = '../data/tdrive_sample/results_pred_'+district+'_'+str(year)+'/'
    # results_path = '../data/tdrive_sample/results_pred_'+district+'_'+str(year)+'/'

    with open(conf_path, 'r') as f:
        conf = json.load(f)
    # results_path = opt.results_path
    # traj_path = '../data/{}/traj/'.format(conf['dataset']['dataset_name'])
    extracted_rn_path = results_path + 'extracted_rn/'
    linked_rn_path = results_path + 'linked_rn/'
    mm_on_linked_rn_path = results_path + 'mm_on_linked_rn/'
    final_rn_path = results_path + 'final_rn/'
    os.makedirs(mm_on_linked_rn_path, exist_ok=True)
    os.makedirs(extracted_rn_path, exist_ok=True)
    os.makedirs(linked_rn_path, exist_ok=True)
    os.makedirs(final_rn_path, exist_ok=True)

    topo_params = conf['topology_construction']
    phase = 1

    # Graph Extraction
    if phase == 1:
        mbr = get_test_mbr(conf)
        # skeleton = cv2.imread(results_path + 'pred_thinned.png', cv2.IMREAD_GRAYSCALE)
        # skeleton = cv2.imread(str(conf['dataset']['dataset_name'])+'.png', cv2.IMREAD_GRAYSCALE)
        # skeleton = Image.open(str(conf['dataset']['dataset_name'])+'.png')

        latin_name = str(conf['dataset']['dataset_name']).split('_')[-1]
        name_cn = list(df[df['latin']==latin_name]['district'])[0]
        # cname = list(df[df['latin']==latin_name]['district'])[0]
        # print(cname+'  is being processed.')
        # skeleton = Image.open('../../../../../20_20_districts/skeleton_file_overlap4/pred_skeleton_'+cname+'_'+str(year)+'.png')
        skeleton = Image.open('../temp_output/topology_construction/'+str(year)+'/pred_skeleton_'+name_cn+'_'+str(year)+'_2.png')
        skeleton = np.array(skeleton)
        map_extractor = GraphExtractor(epsilon=10, min_road_dist=1)
        map_extractor.extract(skeleton, mbr, extracted_rn_path)
    # Link Generation
    # elif opt.phase == 2:
    #     link_generator = LinkGenerator(radius=topo_params['link_radius'])
    #     # the extracted rn is undirected, while the linked rn is directed (bi-directional)
    #     extracted_rn = load_rn_shp(extracted_rn_path, is_directed=False)
    #     link_generator.generate(extracted_rn, linked_rn_path)
    # # Custom Map Matching
    # elif opt.phase == 3:
    #     custom_map_matching = CustomMapMatching(linked_rn_path, topo_params['alpha'])
    #     filenames = os.listdir(traj_path)
    #     with Pool() as pool:
    #         pool.map(partial(custom_map_matching.execute,
    #                          traj_path=traj_path, mm_result_path=mm_on_linked_rn_path), filenames)
    # # Map Refinement
    # elif opt.phase == 4:
    #     linked_rn = load_rn_shp(linked_rn_path, is_directed=True)
    #     map_refiner = MapRefiner(topo_params['min_supp'])
    #     map_refiner.refine(linked_rn, mm_on_linked_rn_path, final_rn_path)
    # else:
    #     raise Exception('invalid phase')
