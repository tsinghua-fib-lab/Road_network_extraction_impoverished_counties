import os
from PIL import Image
import pandas as pd
import math
import numpy as np
# import geopandas as gpd
import PIL.Image
import cv2
PIL.Image.MAX_IMAGE_PIXELS = None
import matplotlib.pyplot as plt
import glob
import shutil
from PIL import Image
import time

# district_list = ['茶陵县', '涟源市', '剑川县', '扎囊县', '汾西县', '柞水县', '康乐县', '黄平县', '仪陇县', '皋兰县', '忻城县', '灵台县', '秭归县', '汝阳县', '印江土家族苗族自治县',  \
#                  '兰考县', '广宗县', '大新县', '保亭黎族苗族自治县', '蕲春县', '麻江县', '新晃侗族自治县', '白河县', '乃东区', '宣化区', '新县', '岚皋县', '岢岚县', '陇川县', '仁布县', \
#                 '武冈市', '余干县', '沈丘县', '新蔡县', '朝天区', '岳西县', '普格县', '上犹县', '南部县', '循化撒拉族自治县', '昭化区', '南皮县', '天等县', '威县', '龙州县', \
#                 '丹寨县', '泾源县', '永平县', '望江县', '秦安县', '汉阴县', '靖州苗族侗族自治县', '马关县', '会昌县', '吉安县', '吴堡县', '正宁县', '偏关县', '湟源县', '阜南县', \
#                 '镇宁布依族苗族自治县', '商南县', '广安区', '大宁县', '盐津县', '施甸县', '关岭布依族苗族自治县', '镇康县', '新邵县', '舒城县', '凤凰县', '牟定县', '吉县', '册亨县', \
#                 '芒市', '灵寿县', '洛宁县', '城关区', '城步苗族自治县', '会同县', '砀山县', '千阳县', '西盟佤族自治县', '魏县', '东川区', '云州区']

# district_list = ['罗田县', '凤山县', '寻乌县', '桑日县', \
#                 '商水县', '台江县', '麻栗坡县', '纳雍县', '达孜区', '弥渡县', '浑源县', '颍上县', '田东县', '阳高县', '六枝特区', '贵定县', '柘城县', '东兰县', '乐安县', '平昌县', '隆安县', \
#                 '光山县', '琼结县', '合阳县', '五寨县', '南康区', '左权县', '饶阳县', '留坝县', '镇远县', '海兴县', '紫阳县', '巴州区', '白沙黎族自治县', '岑巩县', '古丈县', '普定县', '宜君县', \
#                 '城固县', '民和回族土族自治县', '耀州区', '英山县', '平陆县', '勉县', '鹤庆县', '阜城县', '瑞金市', '曲松县', '剑河县', '颍东区', '施秉县', '威信县', '万全区', '范县', '宁陵县', \
#                 '成县', '广昌县', '碧江区', '漾濞彝族自治县', '武山县', '和顺县', '隆德县', '石泉县', '栾川县', '右玉县', '怀安县', '崆峒区', '普安县', '商城县', '姚安县', '南涧彝族自治县', '安仁县', \
#                 '五峰土家族自治县', '孝昌县', '陇县', '新河县', '贞丰县', '湄潭县', '苍溪县', '井冈山市', '代县', '佛坪县', '富川瑶族自治县', '旬邑县', '唐县', '永和县', '临高县', '白水县', '红安县', \
#                 '尖扎县', '潜山市', '赤水市', '新宁县', '娄烦县', '顺平县', '瓮安县', '静乐县', '江口县', '确山县', '花垣县', '望都县', '神池县', '保靖县', '通道侗族自治县', '万安县', '封丘县', \
#                 '万山区', '长武县', '壶关县', '永靖县', '甘洛县', '佳县', '惠水县', '裕安区', '阆中市', '大名县', '梁河县', '玉屏侗族自治县', '昭阳区', '萧县', '子洲县', '孟连傣族拉祜族佤族自治县', \
#                 '泾川县', '中方县', '平顺县', '泗县', '赞皇县', '凌云县', '米脂县', '涞水县', '凤冈县', '灵璧县', '台前县', '保德县']

district_list = ['晴隆县', '郸城县', '贡嘎县', '曲水县', '宾川县', '炎陵县', \
                '平塘县', '雷山县', '泸西县', '龙里县', '龙胜各族自治县', '蒲城县', '方山县', '淮滨县', '东乡族自治县', '中阳县', '元阳县', '洱源县', '临城县', '扶风县', '兴仁市', '德江县', '印台区', \
                    '武强县', '锦屏县', '五指山市', '巴马瑶族自治县', '鲁甸县', '永寿县', '张家川回族自治县', '安龙县', '清水县', '莲花县', '金秀瑶族自治县', '和政县', '富平县', '石阡县', '祥云县', '宜章县', \
                        '曲阳县', '沐川县', '屏边苗族自治县', '武乡县', '文山市', '睢县', '甘谷县', '桐柏县', '辰溪县', '利辛县', '漳县', '积石山保安族东乡族撒拉族自治县', '太康县', '沿河土家族自治县', \
                            '安远县', '合作市', '石城县', '屏山县', '绥德县', '澄城县', '西和县', \
                                '阳原县', '淳化县', '延川县', '宁武县', '北川羌族自治县', '双柏县', '康县', '南江县', '云阳县', '宁县', '永顺县', '石屏县', '溆浦县', '太白县', '茂县', '恩施市', '汉滨区', '山阳县', 
'延长县', '繁峙县', '大姚县', '竹溪县', '兰西县', '彝良县','叙永县', '武定县', '崇礼区', '彭水苗族土家族自治县', '镇巴县', '永善县', '榕江县', '云县', '望谟县', '察哈尔右翼前旗', \
'郧西县', '松桃苗族自治县', '五台县', '麦积区', '南郑区', '丹江口市', '昌宁县', '桑珠孜区', '西林县', '平江县','长阳土家族自治县', '南召县', '石门县', '淅川县', '互助土族自治县', \
'永德县', '兴县', '新化县', '宁陕县', '神农架林区', '宁明县', '宁洱哈尼族彝族自治县', '遂川县', '耿马傣族佤族自治县', '陇西县', '习水县', '镇原县', '克东县', '临洮县', '凤庆县']
# 后四行为最后一部分

for district in district_list:
    print(district)
    if os.path.exists('combine_lable_final/' + district+'_pred_2021_divide_inhabited2.png'):
        continue

    dir_name = '../CoANet3/test_run/'+district+'_out_imgs_1300'
    if not os.path.exists(dir_name):
        continue

#     file_stat = os.stat(dir_name)
#     # 获取最后修改时间
#     last_modified_time = time.ctime(file_stat.st_mtime)
# #    print(district, last_modified_time)

#     if 1: #int(last_modified_time[9:10])<3 or int(last_modified_time[11:13])<22:
# #        print(district,'  working')
#         #pred_img_list_tmp = glob.glob(dir_name+'/*.png')
#         #pred_img_list = []


    #tilefile_list_y = list(pd.read_csv('../../tilefile_zl16_20_plus_20/'+district+'.csv')['y_tile'])

    # tilefile_list_y = (pd.read_csv('../../tilefile_zl16_20_plus_20/'+district+'.csv'))
    if os.path.exists('../tilefile_zl16_20_plus_20/'+district+'.csv'):
        tilefile_list_y = (pd.read_csv('../tilefile_zl16_20_plus_20/'+district+'.csv'))
    elif os.path.exists('../tilefile_zl16_20_plus_20_2/'+district+'.csv'):
        tilefile_list_y = (pd.read_csv('../tilefile_zl16_20_plus_20_2/'+district+'.csv'))
    elif os.path.exists('../tilefile_zl16_20_plus_20_3/'+district+'.csv'):
        tilefile_list_y = (pd.read_csv('../tilefile_zl16_20_plus_20_3/'+district+'.csv'))
    elif os.path.exists('../tilefile_zl16_20_plus_20_4/'+district+'.csv'):
        tilefile_list_y = (pd.read_csv('../tilefile_zl16_20_plus_20_4/'+district+'.csv'))
    elif os.path.exists('../tilefile_zl16_20_plus_20_5/'+district+'.csv'):
        tilefile_list_y = (pd.read_csv('../tilefile_zl16_20_plus_20_5/'+district+'.csv'))
    elif os.path.exists('../tilefile_zl16_20_plus_20_6/'+district+'.csv'):
        tilefile_list_y = (pd.read_csv('../tilefile_zl16_20_plus_20_6/'+district+'.csv'))
    
    pred_img_list_tmp = tilefile_list_y.apply(lambda x: str(x['y_tile'])+'_'+str(x['x_tile']), axis=1)
    y_tile_list = [int(x.split('_')[0]) for x in pred_img_list_tmp]
    #print(y_tile_list[:5])
    x_tile_list = [int(x.split('_')[1]) for x in pred_img_list_tmp]

    min_x = min(x_tile_list)
    max_x = max(x_tile_list)
    min_y = min(y_tile_list)
    max_y = max(y_tile_list)
#            print(district,min_x, max_x, min_y, max_y)

    mask_width_now = max_x-min_x+1
    mask_height_now = max_y-min_y+1

    # mask_now = max(mask_width_now, mask_height_now)
    mask_width = mask_width_now
    mask_height = mask_height_now
    print(district,min_x, max_x, min_y, max_y,mask_height_now, mask_width_now)

    # mask_whole=np.zeros([mask_height*512,mask_width*512],dtype=int)
    mask_whole=np.zeros([mask_height*128,mask_width*128],dtype=int)

    for k in range(len(y_tile_list)):
        img_name = str(y_tile_list[k])+'_'+str(x_tile_list[k])
        # if img_name == '26414_52325':
        #         print('26414_52325')

        # if len(list(uninhabited_df[uninhabited_df['img']==img_name]['uninhabited']))==0 or list(uninhabited_df[uninhabited_df['img']==img_name]['uninhabited'])[0]==0:
        #  or
        # if len(list(uninhabited_df_haze[uninhabited_df_haze['img_name']==img_name]['haze']))>0:
        #     if list(uninhabited_df[uninhabited_df['img_name']==img_name]['haze'])[0]==1 and os.path.exists(dir_name+'/' + img_name  +'_pred.png'):

        if os.path.exists(dir_name+'/' + img_name  +'_pred.png'):
            img_temp=Image.open(dir_name+'/' + img_name  +'_pred.png')
            # if img_name == '26414_52325':
            #     print(1)

            img_temp = img_temp.resize((128,128))
            mask_whole[(y_tile_list[k]-min_y)*128:(y_tile_list[k]-min_y+1)*128, (x_tile_list[k]-min_x)*128:(x_tile_list[k]-min_x+1)*128]=np.array(img_temp)[:,:,0]

    resized_img_tmp = Image.fromarray(mask_whole.astype(np.uint8))

    resized_img = resized_img_tmp#.resize((int(mask_width_now)*128,int(mask_height_now)*128))
    resized_img.save('combine_lable_final/' + district+'_pred_2021_divide_inhabited2.png')

