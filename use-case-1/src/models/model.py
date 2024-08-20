from src.models.blocks import *


class UNet(nn.Module):
    def __init__(self, n_channels_in, n_classes):
        super(UNet, self).__init__()
        self.n_channels_in = n_channels_in
        self.n_classes = n_classes

        self.stem = (ConvBlock(n_channels_in, 64))
        self.down1 = (Downscaling(64, 128))
        self.down2 = (Downscaling(128, 256))
        self.down3 = (Downscaling(256, 512))
        #self.down4 = (Downscaling(512, 1024))
        #self.up1 = (Upscaling(1024, 512))
        self.up2 = (Upscaling(512, 256))
        self.up3 = (Upscaling(256, 128))
        self.up4 = (Upscaling(128, 64))
        self.head = (OutConv(64, n_classes))

    def forward(self, x):
        x1 = self.stem(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        #x5 = self.down4(x4)
        #x = self.up1(x5, x4)
        #x = self.up2(x, x3)
        x = self.up2(x4,x3) #wenn nur auf 512 Channels erweitert werden sollen 
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        logits = self.head(x)
        return logits

    def use_checkpointing(self):
        self.stem = torch.utils.checkpoint(self.inc)
        self.down1 = torch.utils.checkpoint(self.down1)
        self.down2 = torch.utils.checkpoint(self.down2)
        self.down3 = torch.utils.checkpoint(self.down3)
        #self.down4 = torch.utils.checkpoint(self.down4)
        #self.up1 = torch.utils.checkpoint(self.up1)
        self.up2 = torch.utils.checkpoint(self.up2)
        self.up3 = torch.utils.checkpoint(self.up3)
        self.up4 = torch.utils.checkpoint(self.up4)
        self.head = torch.utils.checkpoint(self.head)
