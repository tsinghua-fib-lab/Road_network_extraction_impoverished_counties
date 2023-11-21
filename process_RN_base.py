import geopandas as gpd
import networkx as nx
# import torch
# import momepy
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString
import pandas as pd

#district_list = ['阳原县']
district_list = ['茶陵县', '涟源市', '剑川县', '扎囊县', '汾西县', '柞水县', '康乐县', '黄平县', '仪陇县', '皋兰县', '忻城县', '灵台县', '秭归县', '汝阳县', '印江土家族苗族自治县',  \
                 '兰考县', '广宗县', '大新县', '保亭黎族苗族自治县', '蕲春县', '麻江县', '新晃侗族自治县', '白河县', '乃东区', '宣化区', '新县', '岚皋县', '岢岚县', '陇川县', '仁布县', \
                '武冈市', '余干县', '沈丘县', '新蔡县', '朝天区', '岳西县', '普格县', '上犹县', '南部县', '循化撒拉族自治县', '昭化区', '南皮县', '天等县', '威县', '龙州县', \
                '丹寨县', '泾源县', '永平县', '望江县', '秦安县', '汉阴县', '靖州苗族侗族自治县', '马关县', '会昌县', '吉安县', '吴堡县', '正宁县', '偏关县', '湟源县', '阜南县', \
                '镇宁布依族苗族自治县', '商南县', '广安区', '大宁县', '盐津县', '施甸县', '关岭布依族苗族自治县', '镇康县', '新邵县', '舒城县', '凤凰县', '牟定县', '吉县', '册亨县', \
                '芒市', '灵寿县', '洛宁县', '城关区', '城步苗族自治县', '会同县', '砀山县', '千阳县', '西盟佤族自治县', '魏县', '东川区', '云州区', '罗田县', '凤山县', '寻乌县', '桑日县', \
                '商水县', '台江县', '麻栗坡县', '纳雍县', '达孜区', '弥渡县', '浑源县', '颍上县', '田东县', '阳高县', '六枝特区', '贵定县', '柘城县', '东兰县', '乐安县', '平昌县', '隆安县', \
                '光山县', '琼结县', '合阳县', '五寨县', '南康区', '左权县', '饶阳县', '留坝县', '镇远县', '海兴县', '紫阳县', '巴州区', '白沙黎族自治县', '岑巩县', '古丈县', '普定县', '宜君县', \
                '城固县', '民和回族土族自治县', '耀州区', '英山县', '平陆县', '勉县', '鹤庆县', '阜城县', '瑞金市', '曲松县', '剑河县', '颍东区', '施秉县', '威信县', '万全区', '范县', '宁陵县', \
                '成县', '广昌县', '碧江区', '漾濞彝族自治县', '武山县', '和顺县', '隆德县', '石泉县', '栾川县', '右玉县', '怀安县', '崆峒区', '普安县', '商城县', '姚安县', '南涧彝族自治县', '安仁县', \
                '五峰土家族自治县', '孝昌县', '陇县', '新河县', '贞丰县', '湄潭县', '苍溪县', '井冈山市', '代县', '佛坪县', '富川瑶族自治县', '旬邑县', '唐县', '永和县', '临高县', '白水县', '红安县', \
                '尖扎县', '潜山市', '赤水市', '新宁县', '娄烦县', '顺平县', '瓮安县', '静乐县', '江口县', '确山县', '花垣县', '望都县', '神池县', '保靖县', '通道侗族自治县', '万安县', '封丘县', \
                '万山区', '长武县', '壶关县', '永靖县', '甘洛县', '佳县', '惠水县', '裕安区', '阆中市', '大名县', '梁河县', '玉屏侗族自治县', '昭阳区', '萧县', '子洲县', '孟连傣族拉祜族佤族自治县', \
                '泾川县', '中方县', '平顺县', '泗县', '赞皇县', '凌云县', '米脂县', '涞水县', '凤冈县', '灵璧县', '台前县', '保德县', '晴隆县', '郸城县', '贡嘎县', '曲水县', '宾川县', '炎陵县', \
                '平塘县', '雷山县', '泸西县', '龙里县', '龙胜各族自治县', '蒲城县', '方山县', '淮滨县', '东乡族自治县', '中阳县', '元阳县', '洱源县', '临城县', '扶风县', '兴仁市', '德江县', '印台区', \
                    '武强县', '锦屏县', '五指山市', '巴马瑶族自治县', '鲁甸县', '永寿县', '张家川回族自治县', '安龙县', '清水县', '莲花县', '金秀瑶族自治县', '和政县', '富平县', '石阡县', '祥云县', '宜章县', \
                        '曲阳县', '沐川县', '屏边苗族自治县', '武乡县', '文山市', '睢县', '甘谷县', '桐柏县', '辰溪县', '利辛县', '漳县', '积石山保安族东乡族撒拉族自治县', '太康县', '沿河土家族自治县', \
                            '安远县', '合作市', '石城县', '屏山县', '绥德县', '澄城县', '西和县','阳原县', '淳化县', '延川县', '宁武县', '北川羌族自治县', '双柏县', '康县', '南江县', '云阳县', '宁县', '永顺县', '石屏县', '溆浦县', '太白县', '茂县', '恩施市', '汉滨区', '山阳县', 
'延长县', '繁峙县', '大姚县', '竹溪县', '兰西县', '彝良县','叙永县', '武定县', '崇礼区', '彭水苗族土家族自治县', '镇巴县', '永善县', '榕江县', '云县', '望谟县', '察哈尔右翼前旗', \
'郧西县', '松桃苗族自治县', '五台县', '麦积区', '南郑区', '丹江口市', '昌宁县', '桑珠孜区', '西林县', '平江县','长阳土家族自治县', '南召县', '石门县', '淅川县', '互助土族自治县', \
'永德县', '兴县', '新化县', '宁陕县', '神农架林区', '宁明县', '宁洱哈尼族彝族自治县', '遂川县', '耿马傣族佤族自治县', '陇西县', '习水县', '镇原县', '克东县', '临洮县', '凤庆县']

RL_list2017 = []
RL_list2021 = []
alpha_list = []
beta_list = []
gamma_list = []

for district in district_list:
    #for year in [2017]:
    print(district)
    
    year = 2017
    data = gpd.read_file('RoadNetwork/'+'results_pred_'+district+'_'+str(year)+'/extracted_rn/edges.shp')
    data.crs = "EPSG:4326"
    data.to_crs("EPSG:3857",inplace=True)
    # print(data.crs)
    data['distance'] = data.geometry.length
    # print(data.head())
    distance_list = list(data['distance'])
    RL_list2017.append(np.sum(distance_list))

    year = 2021
    data = gpd.read_file('RoadNetwork/'+'results_pred_'+district+'_'+str(year)+'/extracted_rn/edges.shp')
    data.crs = "EPSG:4326"
    data.to_crs("EPSG:3857",inplace=True)
    # print(data.crs)
    data['distance'] = data.geometry.length
    # print(data.head())
    distance_list = list(data['distance'])
    RL_list2021.append(np.sum(distance_list))

pd_dict = pd.DataFrame({'county':district_list,'rn2017':RL_list2017,'rn2021':RL_list2021})
pd_dict.to_csv('rn_panel.csv', index=False)


        # nodes_shp_path = 'RoadNetwork/'+'results_pred_'+district+'_'+str(year)+'/extracted_rn/nodes.shp'  # 替换成你的节点 Shapefile 文件路径
        # edges_shp_path = 'RoadNetwork/'+'results_pred_'+district+'_'+str(year)+'/extracted_rn/edges.shp'  # 替换成你的边 Shapefile 文件路径

        # nodes_gdf = gpd.read_file(nodes_shp_path)  # 替换成你的节点 Shapefile 文件路径
        # edges_gdf = gpd.read_file(edges_shp_path)  # 替换成你的边 Shapefile 文件路径
        # # edges_gdf.reset_index(drop=True)
        # edges_gdf.crs = 'epsg:4326'  # Set the CRS to EPSG 4326
        # nodes_gdf.crs = 'epsg:4326'

        # # Project to EPSG 3857 CRS
        # edges_gdf = edges_gdf.to_crs('epsg:3857')
        # nodes_gdf = nodes_gdf.to_crs('epsg:3857')
        # # print(data.crs)

        # edges_gdf['length_m'] = edges_gdf['geometry'].length
        # # edges_gdf = edges_gdf.to_crs('epsg:4326')

        # print(nodes_gdf.head())
        # print(edges_gdf.head())

        # # 创建空的 NetworkX 图形
        # G = nx.Graph()

        # # Add nodes to the graph
        # for index, row in nodes_gdf.iterrows():
        #     G.add_node(row['FID'])

        # # Build a spatial index for nodes
        # nodes_sindex = nodes_gdf.sindex

        # # Build a spatial index for edges
        # edges_sindex = edges_gdf.sindex

        # # Add edges to the graph
        # for index, row in edges_gdf.iterrows():
        #     edge_id = row['eid']
        #     edge_geometry = row['geometry']
        #     start_node = edge_geometry.coords[0]
        #     end_node = edge_geometry.coords[-1]
        #     # Calculate edge length as weight
        #     edge_length = row['length_m']

        #     # Find potential nodes near the start and end points of the edge
        #     possible_start_matches = list(nodes_sindex.intersection(start_node))
        #     possible_end_matches = list(nodes_sindex.intersection(end_node))

        #     # Check if the edge geometry intersects or is contained by any node geometry
        #     for match_index in possible_start_matches:
        #         node_geometry = nodes_gdf.loc[match_index, 'geometry']
        #         if edge_geometry.intersects(node_geometry) or edge_geometry.touches(node_geometry):
        #             start_id = nodes_gdf.loc[match_index, 'FID']
        #             break

        #     for match_index in possible_end_matches:
        #         node_geometry = nodes_gdf.loc[match_index, 'geometry']
        #         if edge_geometry.intersects(node_geometry) or edge_geometry.touches(node_geometry):
        #             end_id = nodes_gdf.loc[match_index, 'FID']
        #             break

        #     if start_id is not None and end_id is not None:
        #         G.add_edge(start_id, end_id, weight=edge_length)#

        # # Get the number of nodes and edges in the graph
        # nodes_count = G.number_of_nodes()
        # edges_count = G.number_of_edges()

        # print(f"Number of nodes: {nodes_count}")
        # print(f"Number of edges: {edges_count}")

        # # # 获取节点的位置信息（几何数据）
        # # node_positions = {row['FID']: (row['geometry'].x, row['geometry'].y) for idx, row in nodes_gdf.iterrows()}

        # # # 绘制 NetworkX 图形并保留原始空间布局
        # # plt.figure(figsize=(8, 6))  # 设置画布大小
        # # nx.draw(G, pos=node_positions, with_labels=True, node_size=200, node_color='skyblue')

        # # plt.show()  # 显示图形


        # # pos = nx.spring_layout(G)  # 选择布局算法，这里使用了spring_layout作为示例
        # # nx.draw_networkx_nodes(G, pos, node_size=200, node_color='skyblue')  # 绘制节点
        # # plt.axis('off')  # 关闭坐标轴
        # # plt.show() 

        # # pos = nx.spring_layout(G)  # 定义节点位置
        # # nx.draw(G, pos, node_size=10, with_labels=False)
        # # plt.title('Sample Graph')  # 添加图标题
        # # plt.show()

        # # 获取图的所有连通分量
        # connected_components = list(nx.connected_components(G))

        # # 存储每个连通分量的特征路径长度
        # alpha_list = []
        # beta_list = []
        # gamma_list = []
        # # 遍历每个连通分量并计算特征路径长度
        # for comp in connected_components:
        #     # 获取每个连通分量的子图
        #     subgraph = G.subgraph(comp)
        #     nodes_count = subgraph.number_of_nodes()
        #     edges_count = subgraph.number_of_edges()
        #     if nodes_count>3:
        #         alpha = (edges_count - nodes_count +1)/(2*nodes_count-5)
        #         beta = edges_count/nodes_count
        #         gamma = edges_count/(3*(nodes_count-2))
        #         alpha_list.append(alpha)
        #         beta_list.append(beta)
        #         gamma_list.append(gamma)

        # if alpha_list and beta_list and gamma_list:
        #     # 每个连通分量中心性指标的平均值
        #     avg_degree = sum(alpha_list) / len(alpha_list)
        #     avg_betweenness = sum(beta_list) / len(beta_list)
        #     avg_closeness = sum(gamma_list) / len(gamma_list)

        #     print(f"不连通的带权重图的a为: {avg_degree}")
        #     print(f"不连通的带权重图的b为: {avg_betweenness}")
        #     print(f"不连通的带权重图的g为: {avg_closeness}")

        # # 获取图的所有连通分量
        # connected_components = list(nx.connected_components(G))

        # # 存储每个连通分量的特征路径长度
        # alpha_list = []
        # beta_list = []
        # gamma_list = []
        # # 遍历每个连通分量并计算特征路径长度
        # for comp in connected_components:
        #     # 获取每个连通分量的子图
        #     subgraph = G.subgraph(comp)
        #     nodes_count = subgraph.number_of_nodes()
        #     edges_count = subgraph.number_of_edges()
        #     if nodes_count>3:
        #         alpha = (edges_count - nodes_count +1)/(2*nodes_count-5)
        #         beta = edges_count/nodes_count
        #         gamma = edges_count/(3*(nodes_count-2))
        #         alpha_list.append(alpha)
        #         beta_list.append(beta)
        #         gamma_list.append(gamma)

        # if alpha_list and beta_list and gamma_list:
        #     # 每个连通分量中心性指标的平均值
        #     avg_degree = sum(alpha_list) / len(alpha_list)
        #     avg_betweenness = sum(beta_list) / len(beta_list)
        #     avg_closeness = sum(gamma_list) / len(gamma_list)

        #     print(f"不连通的带权重图的a为: {avg_degree}")
        #     print(f"不连通的带权重图的b为: {avg_betweenness}")
        #     print(f"不连通的带权重图的g为: {avg_closeness}")
