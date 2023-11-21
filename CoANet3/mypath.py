class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'spacenet':
            return '/home/mj/data/work_road/data/SpaceNet/spacenet/result_3m/'
        elif dataset == 'DeepGlobe':
            # return '/home/mj/data/work_road/data/DeepGlobe/'
            # return './process/train/'
            return '../zl16_images_20_plus_20/2021/'

        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
