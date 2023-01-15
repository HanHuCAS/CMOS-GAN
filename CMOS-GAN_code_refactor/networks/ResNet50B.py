import torch.nn as nn
import torch.nn.functional as F



def get_ResNet50( input_dim,num_classes):

    return ResNet50( ResNet50Backbone(input_dim=input_dim), num_classes=num_classes  )


class ResNet50(nn.Module):

    def __init__(self,backbone,num_classes):
        super(ResNet50, self).__init__()
        self.backbone=    backbone
        self.classifier_1 = nn.Linear( in_features = 2048, out_features = num_classes, bias = True)

    def forward(self, x,content=False):

        feature=self.backbone(x,content=content)
        if content:
            return feature

        out=self.classifier_1(feature[0])

        return feature,out

class ResNet50Backbone(nn.Module):

    def __init__(self,input_dim):
        super(ResNet50Backbone, self).__init__()


        self.conv1_7x7_s2 = nn.Conv2d(  in_channels=input_dim, out_channels=64, kernel_size=(7, 7), stride=(2, 2), groups=1, bias=False)
        self.conv1_7x7_s2_bn = nn.BatchNorm2d(  num_features=64, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_1_1x1_reduce = nn.Conv2d(  in_channels=64, out_channels=64, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv2_1_1x1_proj = nn.Conv2d(  in_channels=64, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv2_1_1x1_reduce_bn = nn.BatchNorm2d(  num_features=64, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_1_1x1_proj_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_1_3x3 = nn.Conv2d(  in_channels=64, out_channels=64, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv2_1_3x3_bn = nn.BatchNorm2d(  num_features=64, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_1_1x1_increase = nn.Conv2d(  in_channels=64, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv2_1_1x1_increase_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_2_1x1_reduce = nn.Conv2d(  in_channels=256, out_channels=64, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv2_2_1x1_reduce_bn = nn.BatchNorm2d(  num_features=64, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_2_3x3 = nn.Conv2d(  in_channels=64, out_channels=64, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv2_2_3x3_bn = nn.BatchNorm2d(  num_features=64, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_2_1x1_increase = nn.Conv2d(  in_channels=64, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv2_2_1x1_increase_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_3_1x1_reduce = nn.Conv2d(  in_channels=256, out_channels=64, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv2_3_1x1_reduce_bn = nn.BatchNorm2d(  num_features=64, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_3_3x3 = nn.Conv2d(  in_channels=64, out_channels=64, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv2_3_3x3_bn = nn.BatchNorm2d(  num_features=64, eps=9.999999747378752e-06, momentum=0.1)
        self.conv2_3_1x1_increase = nn.Conv2d(  in_channels=64, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv2_3_1x1_increase_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_1_1x1_reduce = nn.Conv2d(  in_channels=256, out_channels=128, kernel_size=(1, 1), stride=(2, 2), groups=1, bias=False)
        self.conv3_1_1x1_proj = nn.Conv2d(  in_channels=256, out_channels=512, kernel_size=(1, 1), stride=(2, 2), groups=1, bias=False)
        self.conv3_1_1x1_reduce_bn = nn.BatchNorm2d(  num_features=128, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_1_1x1_proj_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_1_3x3 = nn.Conv2d(  in_channels=128, out_channels=128, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv3_1_3x3_bn = nn.BatchNorm2d(  num_features=128, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_1_1x1_increase = nn.Conv2d(  in_channels=128, out_channels=512, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv3_1_1x1_increase_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_2_1x1_reduce = nn.Conv2d(  in_channels=512, out_channels=128, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv3_2_1x1_reduce_bn = nn.BatchNorm2d(  num_features=128, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_2_3x3 = nn.Conv2d(  in_channels=128, out_channels=128, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv3_2_3x3_bn = nn.BatchNorm2d(  num_features=128, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_2_1x1_increase = nn.Conv2d(  in_channels=128, out_channels=512, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv3_2_1x1_increase_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_3_1x1_reduce = nn.Conv2d(  in_channels=512, out_channels=128, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv3_3_1x1_reduce_bn = nn.BatchNorm2d(  num_features=128, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_3_3x3 = nn.Conv2d(  in_channels=128, out_channels=128, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv3_3_3x3_bn = nn.BatchNorm2d(  num_features=128, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_3_1x1_increase = nn.Conv2d(  in_channels=128, out_channels=512, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv3_3_1x1_increase_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_4_1x1_reduce = nn.Conv2d(  in_channels=512, out_channels=128, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv3_4_1x1_reduce_bn = nn.BatchNorm2d(  num_features=128, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_4_3x3 = nn.Conv2d(  in_channels=128, out_channels=128, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv3_4_3x3_bn = nn.BatchNorm2d(  num_features=128, eps=9.999999747378752e-06, momentum=0.1)
        self.conv3_4_1x1_increase = nn.Conv2d(  in_channels=128, out_channels=512, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv3_4_1x1_increase_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_1_1x1_reduce = nn.Conv2d(  in_channels=512, out_channels=256, kernel_size=(1, 1), stride=(2, 2), groups=1, bias=False)
        self.conv4_1_1x1_proj = nn.Conv2d(  in_channels=512, out_channels=1024, kernel_size=(1, 1), stride=(2, 2), groups=1, bias=False)
        self.conv4_1_1x1_reduce_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_1_1x1_proj_bn = nn.BatchNorm2d(  num_features=1024, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_1_3x3 = nn.Conv2d(  in_channels=256, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv4_1_3x3_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_1_1x1_increase = nn.Conv2d(  in_channels=256, out_channels=1024, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_1_1x1_increase_bn = nn.BatchNorm2d(  num_features=1024, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_2_1x1_reduce = nn.Conv2d(  in_channels=1024, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_2_1x1_reduce_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_2_3x3 = nn.Conv2d(  in_channels=256, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv4_2_3x3_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_2_1x1_increase = nn.Conv2d(  in_channels=256, out_channels=1024, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_2_1x1_increase_bn = nn.BatchNorm2d(  num_features=1024, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_3_1x1_reduce = nn.Conv2d(  in_channels=1024, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_3_1x1_reduce_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_3_3x3 = nn.Conv2d(  in_channels=256, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv4_3_3x3_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_3_1x1_increase = nn.Conv2d(  in_channels=256, out_channels=1024, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_3_1x1_increase_bn = nn.BatchNorm2d(  num_features=1024, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_4_1x1_reduce = nn.Conv2d(  in_channels=1024, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_4_1x1_reduce_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_4_3x3 = nn.Conv2d(  in_channels=256, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv4_4_3x3_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_4_1x1_increase = nn.Conv2d(  in_channels=256, out_channels=1024, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_4_1x1_increase_bn = nn.BatchNorm2d(  num_features=1024, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_5_1x1_reduce = nn.Conv2d(  in_channels=1024, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_5_1x1_reduce_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_5_3x3 = nn.Conv2d(  in_channels=256, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv4_5_3x3_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_5_1x1_increase = nn.Conv2d(  in_channels=256, out_channels=1024, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_5_1x1_increase_bn = nn.BatchNorm2d(  num_features=1024, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_6_1x1_reduce = nn.Conv2d(  in_channels=1024, out_channels=256, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_6_1x1_reduce_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_6_3x3 = nn.Conv2d(  in_channels=256, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv4_6_3x3_bn = nn.BatchNorm2d(  num_features=256, eps=9.999999747378752e-06, momentum=0.1)
        self.conv4_6_1x1_increase = nn.Conv2d(  in_channels=256, out_channels=1024, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv4_6_1x1_increase_bn = nn.BatchNorm2d(  num_features=1024, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_1_1x1_reduce = nn.Conv2d(  in_channels=1024, out_channels=512, kernel_size=(1, 1), stride=(2, 2), groups=1, bias=False)
        self.conv5_1_1x1_proj = nn.Conv2d(  in_channels=1024, out_channels=2048, kernel_size=(1, 1), stride=(2, 2), groups=1, bias=False)
        self.conv5_1_1x1_reduce_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_1_1x1_proj_bn = nn.BatchNorm2d(  num_features=2048, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_1_3x3 = nn.Conv2d(  in_channels=512, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv5_1_3x3_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_1_1x1_increase = nn.Conv2d(  in_channels=512, out_channels=2048, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv5_1_1x1_increase_bn = nn.BatchNorm2d(  num_features=2048, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_2_1x1_reduce = nn.Conv2d(  in_channels=2048, out_channels=512, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv5_2_1x1_reduce_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_2_3x3 = nn.Conv2d(  in_channels=512, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv5_2_3x3_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_2_1x1_increase = nn.Conv2d(  in_channels=512, out_channels=2048, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv5_2_1x1_increase_bn = nn.BatchNorm2d(  num_features=2048, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_3_1x1_reduce = nn.Conv2d(  in_channels=2048, out_channels=512, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv5_3_1x1_reduce_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_3_3x3 = nn.Conv2d(  in_channels=512, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv5_3_3x3_bn = nn.BatchNorm2d(  num_features=512, eps=9.999999747378752e-06, momentum=0.1)
        self.conv5_3_1x1_increase = nn.Conv2d(  in_channels=512, out_channels=2048, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=False)
        self.conv5_3_1x1_increase_bn = nn.BatchNorm2d(  num_features=2048, eps=9.999999747378752e-06, momentum=0.1)

    def forward(self, x, content=False, single_output=False):
        
        conv1_7x7_s2_pad = F.pad(x, (3, 3, 3, 3))
        conv1_7x7_s2    = self.conv1_7x7_s2(conv1_7x7_s2_pad)
        conv1_7x7_s2_bn = self.conv1_7x7_s2_bn(conv1_7x7_s2)
        conv1_relu_7x7_s2 = F.relu(conv1_7x7_s2_bn)
        pool1_3x3_s2_pad = F.pad(conv1_relu_7x7_s2, (0, 1, 0, 1), value=float('-inf'))
        pool1_3x3_s2    = F.max_pool2d(pool1_3x3_s2_pad, kernel_size=(3, 3), stride=(2, 2), padding=0, ceil_mode=False)

        conv2_1_1x1_reduce = self.conv2_1_1x1_reduce(pool1_3x3_s2) #64 -> 64
        conv2_1_1x1_proj = self.conv2_1_1x1_proj(pool1_3x3_s2) # 64 256
        conv2_1_1x1_reduce_bn = self.conv2_1_1x1_reduce_bn(conv2_1_1x1_reduce)
        conv2_1_1x1_proj_bn = self.conv2_1_1x1_proj_bn(conv2_1_1x1_proj)
        conv2_1_1x1_reduce_relu = F.relu(conv2_1_1x1_reduce_bn) # 64
        conv2_1_3x3_pad = F.pad(conv2_1_1x1_reduce_relu, (1, 1, 1, 1)) # 256
        conv2_1_3x3     = self.conv2_1_3x3(conv2_1_3x3_pad) #  64 -> 64
        conv2_1_3x3_bn  = self.conv2_1_3x3_bn(conv2_1_3x3)   
        conv2_1_3x3_relu = F.relu(conv2_1_3x3_bn)
        conv2_1_1x1_increase = self.conv2_1_1x1_increase(conv2_1_3x3_relu)
        conv2_1_1x1_increase_bn = self.conv2_1_1x1_increase_bn(conv2_1_1x1_increase)  # 64 -> 256
        conv2_1         = conv2_1_1x1_proj_bn + conv2_1_1x1_increase_bn  # 256
        conv2_1_relu    = F.relu(conv2_1)


        conv2_2_1x1_reduce = self.conv2_2_1x1_reduce(conv2_1_relu)
        conv2_2_1x1_reduce_bn = self.conv2_2_1x1_reduce_bn(conv2_2_1x1_reduce)
        conv2_2_1x1_reduce_relu = F.relu(conv2_2_1x1_reduce_bn)
        conv2_2_3x3_pad = F.pad(conv2_2_1x1_reduce_relu, (1, 1, 1, 1))
        conv2_2_3x3     = self.conv2_2_3x3(conv2_2_3x3_pad)
        conv2_2_3x3_bn  = self.conv2_2_3x3_bn(conv2_2_3x3)
        conv2_2_3x3_relu = F.relu(conv2_2_3x3_bn)
        conv2_2_1x1_increase = self.conv2_2_1x1_increase(conv2_2_3x3_relu)
        conv2_2_1x1_increase_bn = self.conv2_2_1x1_increase_bn(conv2_2_1x1_increase)
        conv2_2         = conv2_1_relu + conv2_2_1x1_increase_bn
        conv2_2_relu    = F.relu(conv2_2)
        conv2_3_1x1_reduce = self.conv2_3_1x1_reduce(conv2_2_relu)
        conv2_3_1x1_reduce_bn = self.conv2_3_1x1_reduce_bn(conv2_3_1x1_reduce)
        conv2_3_1x1_reduce_relu = F.relu(conv2_3_1x1_reduce_bn)
        conv2_3_3x3_pad = F.pad(conv2_3_1x1_reduce_relu, (1, 1, 1, 1))
        conv2_3_3x3     = self.conv2_3_3x3(conv2_3_3x3_pad)
        conv2_3_3x3_bn  = self.conv2_3_3x3_bn(conv2_3_3x3)
        conv2_3_3x3_relu = F.relu(conv2_3_3x3_bn)
        conv2_3_1x1_increase = self.conv2_3_1x1_increase(conv2_3_3x3_relu)
        conv2_3_1x1_increase_bn = self.conv2_3_1x1_increase_bn(conv2_3_1x1_increase)
        conv2_3         = conv2_2_relu + conv2_3_1x1_increase_bn
        conv2_3_relu    = F.relu(conv2_3)
        conv3_1_1x1_reduce = self.conv3_1_1x1_reduce(conv2_3_relu)
        conv3_1_1x1_proj = self.conv3_1_1x1_proj(conv2_3_relu)
        conv3_1_1x1_reduce_bn = self.conv3_1_1x1_reduce_bn(conv3_1_1x1_reduce)
        conv3_1_1x1_proj_bn = self.conv3_1_1x1_proj_bn(conv3_1_1x1_proj)
        conv3_1_1x1_reduce_relu = F.relu(conv3_1_1x1_reduce_bn)
        conv3_1_3x3_pad = F.pad(conv3_1_1x1_reduce_relu, (1, 1, 1, 1))
        conv3_1_3x3     = self.conv3_1_3x3(conv3_1_3x3_pad)
        conv3_1_3x3_bn  = self.conv3_1_3x3_bn(conv3_1_3x3)
        conv3_1_3x3_relu = F.relu(conv3_1_3x3_bn)
        conv3_1_1x1_increase = self.conv3_1_1x1_increase(conv3_1_3x3_relu)
        conv3_1_1x1_increase_bn = self.conv3_1_1x1_increase_bn(conv3_1_1x1_increase)
        conv3_1         = conv3_1_1x1_proj_bn + conv3_1_1x1_increase_bn
        conv3_1_relu    = F.relu(conv3_1)
        conv3_2_1x1_reduce = self.conv3_2_1x1_reduce(conv3_1_relu)
        conv3_2_1x1_reduce_bn = self.conv3_2_1x1_reduce_bn(conv3_2_1x1_reduce)
        conv3_2_1x1_reduce_relu = F.relu(conv3_2_1x1_reduce_bn)
        conv3_2_3x3_pad = F.pad(conv3_2_1x1_reduce_relu, (1, 1, 1, 1))
        conv3_2_3x3     = self.conv3_2_3x3(conv3_2_3x3_pad)
        conv3_2_3x3_bn  = self.conv3_2_3x3_bn(conv3_2_3x3)
        conv3_2_3x3_relu = F.relu(conv3_2_3x3_bn)
        conv3_2_1x1_increase = self.conv3_2_1x1_increase(conv3_2_3x3_relu)
        conv3_2_1x1_increase_bn = self.conv3_2_1x1_increase_bn(conv3_2_1x1_increase)
        conv3_2         = conv3_1_relu + conv3_2_1x1_increase_bn
        conv3_2_relu    = F.relu(conv3_2)
        conv3_3_1x1_reduce = self.conv3_3_1x1_reduce(conv3_2_relu)
        conv3_3_1x1_reduce_bn = self.conv3_3_1x1_reduce_bn(conv3_3_1x1_reduce)
        conv3_3_1x1_reduce_relu = F.relu(conv3_3_1x1_reduce_bn)
        conv3_3_3x3_pad = F.pad(conv3_3_1x1_reduce_relu, (1, 1, 1, 1))
        conv3_3_3x3     = self.conv3_3_3x3(conv3_3_3x3_pad)
        conv3_3_3x3_bn  = self.conv3_3_3x3_bn(conv3_3_3x3)
        conv3_3_3x3_relu = F.relu(conv3_3_3x3_bn)
        conv3_3_1x1_increase = self.conv3_3_1x1_increase(conv3_3_3x3_relu)
        conv3_3_1x1_increase_bn = self.conv3_3_1x1_increase_bn(conv3_3_1x1_increase)
        conv3_3         = conv3_2_relu + conv3_3_1x1_increase_bn
        conv3_3_relu    = F.relu(conv3_3)
        conv3_4_1x1_reduce = self.conv3_4_1x1_reduce(conv3_3_relu)
        conv3_4_1x1_reduce_bn = self.conv3_4_1x1_reduce_bn(conv3_4_1x1_reduce)
        conv3_4_1x1_reduce_relu = F.relu(conv3_4_1x1_reduce_bn)
        conv3_4_3x3_pad = F.pad(conv3_4_1x1_reduce_relu, (1, 1, 1, 1))
        conv3_4_3x3     = self.conv3_4_3x3(conv3_4_3x3_pad)
        conv3_4_3x3_bn  = self.conv3_4_3x3_bn(conv3_4_3x3)
        conv3_4_3x3_relu = F.relu(conv3_4_3x3_bn)
        conv3_4_1x1_increase = self.conv3_4_1x1_increase(conv3_4_3x3_relu)
        conv3_4_1x1_increase_bn = self.conv3_4_1x1_increase_bn(conv3_4_1x1_increase)
        conv3_4         = conv3_3_relu + conv3_4_1x1_increase_bn
        conv3_4_relu    = F.relu(conv3_4)
        conv4_1_1x1_reduce = self.conv4_1_1x1_reduce(conv3_4_relu)
        conv4_1_1x1_proj = self.conv4_1_1x1_proj(conv3_4_relu)
        conv4_1_1x1_reduce_bn = self.conv4_1_1x1_reduce_bn(conv4_1_1x1_reduce)
        conv4_1_1x1_proj_bn = self.conv4_1_1x1_proj_bn(conv4_1_1x1_proj)
        conv4_1_1x1_reduce_relu = F.relu(conv4_1_1x1_reduce_bn)
        conv4_1_3x3_pad = F.pad(conv4_1_1x1_reduce_relu, (1, 1, 1, 1))
        conv4_1_3x3     = self.conv4_1_3x3(conv4_1_3x3_pad)
        conv4_1_3x3_bn  = self.conv4_1_3x3_bn(conv4_1_3x3)
        conv4_1_3x3_relu = F.relu(conv4_1_3x3_bn)
        conv4_1_1x1_increase = self.conv4_1_1x1_increase(conv4_1_3x3_relu)
        conv4_1_1x1_increase_bn = self.conv4_1_1x1_increase_bn(conv4_1_1x1_increase)
        conv4_1         = conv4_1_1x1_proj_bn + conv4_1_1x1_increase_bn

        if content:
            return  conv4_1

        conv4_1_relu    = F.relu(conv4_1)
        conv4_2_1x1_reduce = self.conv4_2_1x1_reduce(conv4_1_relu)
        conv4_2_1x1_reduce_bn = self.conv4_2_1x1_reduce_bn(conv4_2_1x1_reduce)
        conv4_2_1x1_reduce_relu = F.relu(conv4_2_1x1_reduce_bn)
        conv4_2_3x3_pad = F.pad(conv4_2_1x1_reduce_relu, (1, 1, 1, 1))
        conv4_2_3x3     = self.conv4_2_3x3(conv4_2_3x3_pad)
        conv4_2_3x3_bn  = self.conv4_2_3x3_bn(conv4_2_3x3)
        conv4_2_3x3_relu = F.relu(conv4_2_3x3_bn)
        conv4_2_1x1_increase = self.conv4_2_1x1_increase(conv4_2_3x3_relu)
        conv4_2_1x1_increase_bn = self.conv4_2_1x1_increase_bn(conv4_2_1x1_increase)
        conv4_2         = conv4_1_relu + conv4_2_1x1_increase_bn
        conv4_2_relu    = F.relu(conv4_2)
        conv4_3_1x1_reduce = self.conv4_3_1x1_reduce(conv4_2_relu)
        conv4_3_1x1_reduce_bn = self.conv4_3_1x1_reduce_bn(conv4_3_1x1_reduce)
        conv4_3_1x1_reduce_relu = F.relu(conv4_3_1x1_reduce_bn)
        conv4_3_3x3_pad = F.pad(conv4_3_1x1_reduce_relu, (1, 1, 1, 1))
        conv4_3_3x3     = self.conv4_3_3x3(conv4_3_3x3_pad)
        conv4_3_3x3_bn  = self.conv4_3_3x3_bn(conv4_3_3x3)
        conv4_3_3x3_relu = F.relu(conv4_3_3x3_bn)
        conv4_3_1x1_increase = self.conv4_3_1x1_increase(conv4_3_3x3_relu)
        conv4_3_1x1_increase_bn = self.conv4_3_1x1_increase_bn(conv4_3_1x1_increase)
        conv4_3         = conv4_2_relu + conv4_3_1x1_increase_bn
        conv4_3_relu    = F.relu(conv4_3)
        conv4_4_1x1_reduce = self.conv4_4_1x1_reduce(conv4_3_relu)
        conv4_4_1x1_reduce_bn = self.conv4_4_1x1_reduce_bn(conv4_4_1x1_reduce)
        conv4_4_1x1_reduce_relu = F.relu(conv4_4_1x1_reduce_bn)
        conv4_4_3x3_pad = F.pad(conv4_4_1x1_reduce_relu, (1, 1, 1, 1))
        conv4_4_3x3     = self.conv4_4_3x3(conv4_4_3x3_pad)
        conv4_4_3x3_bn  = self.conv4_4_3x3_bn(conv4_4_3x3)
        conv4_4_3x3_relu = F.relu(conv4_4_3x3_bn)
        conv4_4_1x1_increase = self.conv4_4_1x1_increase(conv4_4_3x3_relu)
        conv4_4_1x1_increase_bn = self.conv4_4_1x1_increase_bn(conv4_4_1x1_increase)
        conv4_4         = conv4_3_relu + conv4_4_1x1_increase_bn
        conv4_4_relu    = F.relu(conv4_4)
        conv4_5_1x1_reduce = self.conv4_5_1x1_reduce(conv4_4_relu)
        conv4_5_1x1_reduce_bn = self.conv4_5_1x1_reduce_bn(conv4_5_1x1_reduce)
        conv4_5_1x1_reduce_relu = F.relu(conv4_5_1x1_reduce_bn)
        conv4_5_3x3_pad = F.pad(conv4_5_1x1_reduce_relu, (1, 1, 1, 1))
        conv4_5_3x3     = self.conv4_5_3x3(conv4_5_3x3_pad)
        conv4_5_3x3_bn  = self.conv4_5_3x3_bn(conv4_5_3x3)
        conv4_5_3x3_relu = F.relu(conv4_5_3x3_bn)
        conv4_5_1x1_increase = self.conv4_5_1x1_increase(conv4_5_3x3_relu)
        conv4_5_1x1_increase_bn = self.conv4_5_1x1_increase_bn(conv4_5_1x1_increase)
        conv4_5         = conv4_4_relu + conv4_5_1x1_increase_bn
        conv4_5_relu    = F.relu(conv4_5)
        conv4_6_1x1_reduce = self.conv4_6_1x1_reduce(conv4_5_relu)
        conv4_6_1x1_reduce_bn = self.conv4_6_1x1_reduce_bn(conv4_6_1x1_reduce)
        conv4_6_1x1_reduce_relu = F.relu(conv4_6_1x1_reduce_bn)
        conv4_6_3x3_pad = F.pad(conv4_6_1x1_reduce_relu, (1, 1, 1, 1))
        conv4_6_3x3     = self.conv4_6_3x3(conv4_6_3x3_pad)
        conv4_6_3x3_bn  = self.conv4_6_3x3_bn(conv4_6_3x3)
        conv4_6_3x3_relu = F.relu(conv4_6_3x3_bn)
        conv4_6_1x1_increase = self.conv4_6_1x1_increase(conv4_6_3x3_relu)
        conv4_6_1x1_increase_bn = self.conv4_6_1x1_increase_bn(conv4_6_1x1_increase)
        conv4_6         = conv4_5_relu + conv4_6_1x1_increase_bn
        conv4_6_relu    = F.relu(conv4_6)
        conv5_1_1x1_reduce = self.conv5_1_1x1_reduce(conv4_6_relu)
        conv5_1_1x1_proj = self.conv5_1_1x1_proj(conv4_6_relu)
        conv5_1_1x1_reduce_bn = self.conv5_1_1x1_reduce_bn(conv5_1_1x1_reduce)
        conv5_1_1x1_proj_bn = self.conv5_1_1x1_proj_bn(conv5_1_1x1_proj)
        conv5_1_1x1_reduce_relu = F.relu(conv5_1_1x1_reduce_bn)
        conv5_1_3x3_pad = F.pad(conv5_1_1x1_reduce_relu, (1, 1, 1, 1))
        conv5_1_3x3     = self.conv5_1_3x3(conv5_1_3x3_pad)
        conv5_1_3x3_bn  = self.conv5_1_3x3_bn(conv5_1_3x3)
        conv5_1_3x3_relu = F.relu(conv5_1_3x3_bn)
        conv5_1_1x1_increase = self.conv5_1_1x1_increase(conv5_1_3x3_relu)
        conv5_1_1x1_increase_bn = self.conv5_1_1x1_increase_bn(conv5_1_1x1_increase)
        conv5_1         = conv5_1_1x1_proj_bn + conv5_1_1x1_increase_bn
        conv5_1_relu    = F.relu(conv5_1)
        conv5_2_1x1_reduce = self.conv5_2_1x1_reduce(conv5_1_relu)
        conv5_2_1x1_reduce_bn = self.conv5_2_1x1_reduce_bn(conv5_2_1x1_reduce)
        conv5_2_1x1_reduce_relu = F.relu(conv5_2_1x1_reduce_bn)
        conv5_2_3x3_pad = F.pad(conv5_2_1x1_reduce_relu, (1, 1, 1, 1))
        conv5_2_3x3     = self.conv5_2_3x3(conv5_2_3x3_pad)
        conv5_2_3x3_bn  = self.conv5_2_3x3_bn(conv5_2_3x3)
        conv5_2_3x3_relu = F.relu(conv5_2_3x3_bn)
        conv5_2_1x1_increase = self.conv5_2_1x1_increase(conv5_2_3x3_relu)
        conv5_2_1x1_increase_bn = self.conv5_2_1x1_increase_bn(conv5_2_1x1_increase)
        conv5_2         = conv5_1_relu + conv5_2_1x1_increase_bn
        conv5_2_relu    = F.relu(conv5_2)
        conv5_3_1x1_reduce = self.conv5_3_1x1_reduce(conv5_2_relu)
        conv5_3_1x1_reduce_bn = self.conv5_3_1x1_reduce_bn(conv5_3_1x1_reduce)
        conv5_3_1x1_reduce_relu = F.relu(conv5_3_1x1_reduce_bn)
        conv5_3_3x3_pad = F.pad(conv5_3_1x1_reduce_relu, (1, 1, 1, 1))
        conv5_3_3x3     = self.conv5_3_3x3(conv5_3_3x3_pad)
        conv5_3_3x3_bn  = self.conv5_3_3x3_bn(conv5_3_3x3)
        conv5_3_3x3_relu = F.relu(conv5_3_3x3_bn)
        conv5_3_1x1_increase = self.conv5_3_1x1_increase(conv5_3_3x3_relu)
        conv5_3_1x1_increase_bn = self.conv5_3_1x1_increase_bn(conv5_3_1x1_increase)
        conv5_3         = conv5_2_relu + conv5_3_1x1_increase_bn
        conv5_3_relu    = F.relu(conv5_3)
        pool5_7x7_s1    = F.avg_pool2d(conv5_3_relu, kernel_size=(7, 7), stride=(1, 1), padding=(0,), ceil_mode=False, count_include_pad=False)
        classifier_0    = pool5_7x7_s1.view(pool5_7x7_s1.size(0), -1)
        
        if single_output:
            return classifier_0

        return classifier_0, [conv2_1, conv3_1, conv4_1, conv5_1]      