import pandas as pd
import numpy as np
from shapely.geometry import Point
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = None
from skimage import morphology,draw
import cv2
import matplotlib.pyplot as plt
import os


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
#后四行为最后一部分，17年还在处理

for city in district_list: #['神木市']: # 
    #if os.path.exists('skeleton_file_final/pred_skeleton_'+city+'_'+str(2017)+'_2.png'): ##等于前文的d500
    if os.path.exists('skeleton_file_final_d500/pred_skeleton_'+city+'_'+str(2021)+'_2.png'):
        continue
    print(city)

    if not os.path.exists('combine_lable_final/'+city+'_pred_'+str(2021)+'_divide_inhabited2.png'):
        continue
    print('reading '+'combine_lable_final/'+city+'_pred_'+str(2021)+'_divide_inhabited2.png')
    road2017 = Image.open('combine_lable_final/'+city+'_pred_'+str(2021)+'_divide_inhabited2.png')
    #road2017 = road2017.resize((int(np.array(road2017).shape[1]),int(np.array(road2017).shape[0])))
    road2017_arr = np.array(road2017)
    # print(road2017_arr.shape)
    road2017 = None

    road_tmp = road2017_arr
    
    road_seg = np.array(road_tmp) #[512:-512*5,1024:-512*4]
    road_idx = np.where(road_seg > 0)

    print(2017,len(road_idx[0]))

    bin_image = np.zeros((road_seg.shape[0],road_seg.shape[1]))
    bin_image[road_idx[0],road_idx[1]] = 1

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11,11))
    bin_image = cv2.morphologyEx(bin_image, cv2.MORPH_CLOSE, kernel)

    bin_image = np.uint8(bin_image)

#print(np.sum(np.array(test_img)))

#     image = test_img

#     print(image.shape)
# #实施骨架算法
    skeleton =morphology.skeletonize(bin_image)
# if 1:
#     city = '西乡县'
#     skeleton = Image.open('skeleton_file_final/pred_skeleton_'+city+'_'+str(2017)+'_2_tmp.png')

    road_seg = np.uint8(np.array(skeleton)) #[512:-512*5,1024:-512*4]
    road_idx = np.where(road_seg > 0)
    print(2017,len(road_idx[0]),'  skeleton')

    # skeleton = Image.fromarray(skeleton)
    # skeleton.convert('L').save('skeleton_file_final/pred_skeleton_'+city+'_'+str(2017)+'_2_tmp.png')  #xiaoxian

    road_seg[road_idx] = 1

    # bin_image = np.uint8(road_seg)

    _, labels, stats, centroids = cv2.connectedComponentsWithStats(road_seg)
# print(centroids)
# print("stats",stats)
#print('len(stats): ',len(stats))
    i=0
    for istat in stats:
        #if istat[4]<10:  #skeleton_file_final
        if istat[4]<500 and istat[4]>0:  #skeleton_file_final_d500
        # print(i, istat[4])
        # print(istat[0:2])
        # if istat[3]>istat[4]:
        #     r=istat[3]
        # else:r=istat[4]
            if istat[0]<=100 and istat[1]<=100 and istat[0]+istat[2]>=road_seg.shape[0]-20 and istat[1]+istat[3]>=road_seg.shape[1]-20: #road2017_arr
                print(tuple(istat[0:2]),tuple(istat[0:2]+istat[2:4]))
                continue
            cv2.rectangle(road_seg,tuple(istat[0:2]),tuple(istat[0:2]+istat[2:4]) , 0,thickness=-1)  # 26  #test_img
            i=i+1

#print(i,len(stats),'dif')

#print(np.sum(np.array(test_img)))

# plt.imshow(test_img)
# plt.show()

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(13,13)) 
# bin_image = cv2.dilate(test_img,kernel,5)

    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
    # bin_image = cv2.morphologyEx(test_img, cv2.MORPH_CLOSE, kernel)
    # image = bin_image

#     image = test_img

#     print(image.shape)
# #实施骨架算法
#     skeleton =morphology.skeletonize(image)
#     print(np.sum(np.array(skeleton)))
    # skeleton = Image.fromarray(skeleton)

    road_idx = np.where(road_seg > 0)
    road_seg[road_idx] = 255
    print(2017,len(road_idx[0]),'  skeleton')

    skeleton = Image.fromarray(road_seg) #test_img
    skeleton.convert('L').save('skeleton_file_final_d500/pred_skeleton_'+city+'_'+str(2021)+'_2.png')  #xiaoxian

