#-*- coding:utf-8 -*-
import random
import torch
from torch.autograd import Variable


class ImagePool():
    
    '''
    from https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
    Copyright (c) 2016, Phillip Isola and Jun-Yan Zhu All rights reserved.
    '''
    
    def __init__(self, pool_size):
        self.pool_size = pool_size
        if self.pool_size > 0:
            self.num_imgs = 0
            self.images = []


    def query(self, images):
        if self.pool_size == 0:
            return Variable(images)
        return_images = []


        for image in images:
            image = torch.unsqueeze(image, 0)  
            if self.num_imgs < self.pool_size:
                self.num_imgs = self.num_imgs + 1
                self.images.append(image)
                return_images.append(image)
            else:
                p = random.uniform(0, 1)
                if p > 0.5:
                    random_id = random.randint(0, self.pool_size - 1)
                    tmp = self.images[random_id].clone()
                    self.images[random_id] = image
                    return_images.append(tmp)
                else:
                    return_images.append(image)
        return_images = Variable(torch.cat(return_images, 0))  
        return return_images
