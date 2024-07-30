#This is the code repository for Leveraging Deep Learning-based Road Extraction from Satellite Imagery for Socioeconomic Analysis in Impoverished Counties. 


1. pre-processing: identify the noisy or cloud covered satellite imagery.

2. CoANet3: generate the road masks based on the CoANet model pretrained on the DeepGlobe dataset. Please refer to the original github repository for detailed description (CoANet: Connectivity Attention Network for Road Extraction From Satellite Imagery).

3. post-processing: concat the road masks and perform morthological operations.

4. topology_construction: transform the road skeleton image into the road network shapefile. Please refer to the original github repository for detailed description (Learning to Generate Maps from Trajectories).

5. process_RN2.py: transform the road network shapefile into graph and calculate the structural features.

6. sample_roadnetwork: an example of the extracted road network in one impoverished county. The whole dataset is too large to upload here. We are trying to upload them elsewhere.

##Citation<br />
If you find this project useful in your research, please consider citing:<br />

@article{xi2024pixels,<br />
  title={From Pixels to Progress: Generating Road Network from Satellite Imagery for Socioeconomic Insights in Impoverished Areas},<br />
  author={Xi, Yanxin and Liu, Yu and Liu, Zhicheng and Tarkoma, Sasu and Hui, Pan and Li, Yong},<br />
  journal={arXiv preprint arXiv:2406.11282},<br />
  year={2024}<br />
}<br />
