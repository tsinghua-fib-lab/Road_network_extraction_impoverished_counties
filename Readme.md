This is the code repository for Leveraging Deep Learning-based Road Extraction from Satellite Imagery for Socioeconomic Analysis in Impoverished Counties. 

TODO: code and dataset

pre-processing: identify the hazy or cloud covered satellite imagery.

CoANet3: generate the road masks based on the CoANet model pretrained on the DeepGlobe dataset. Please refer to the original github repository for detailed description (CoANet: Connectivity Attention Network for Road Extraction From Satellite Imagery).

post-processing: concat the road masks and perform morthological operations.

topology_construction: transform the road skeleton image into the road network shapefile. Please refer to the original github repository for detailed description (Learning to Generate Maps from Trajectories).

process_RN2.py: transform the road network shapefile into graph and calculate the structural features.

sample_roadnetwork: an example of the extracted road network in one impoverished county. The whole dataset is too large to upload here. We are trying to upload them elsewhere.
