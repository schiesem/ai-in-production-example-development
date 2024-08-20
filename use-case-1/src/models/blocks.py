import torch
import torch.nn as nn
import torch.nn.functional as F


class ConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels, mid_channels=None):
        super().__init__()
        if not mid_channels:
            mid_channels = out_channels
        self.conv_block = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(mid_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.conv_block(x)


class Downscaling(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(kernel_size=2, stride=2),
            ConvBlock(in_channels, out_channels)
        )

    def forward(self, x):
        return self.maxpool_conv(x)


class Upscaling(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.up = nn.ConvTranspose2d(in_channels, in_channels // 2, kernel_size=2, stride=2)
        self.conv = ConvBlock(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.up(x1)

        # Berechnung der Dimensionsunterschiede zwischen x1 (Feature-Map nach Upsampling) und x2 (Feature-Map, die von einem parallelen Pfad oder einer höheren Ebene im Netzwerk stammt)
        # Dimension ist CHW
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]

        # Padding von x1, um sicherzustellen, dass x1 und x2 die gleichen Dimensionen haben
        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])

        # Concatenation von x1 und x2:
        # Die beiden Feature-Maps x1 und x2 werden entlang der Kanaldimension (dim=1) zusammengeführt
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)

# finale Ausgangsschicht oft die Aufgabe hat, die tiefen Features des Netzwerks in eine Karte von Ausgabeklassen zu transformieren.
class OutConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(OutConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1) #1x1 Conv-Kernel zur Transformation der Merkmalskarten in Klassenwahrscheinlichkeiten oder -markierungen, ohne die räumliche Dimension zu verändern.

    def forward(self, x):
        return self.conv(x)