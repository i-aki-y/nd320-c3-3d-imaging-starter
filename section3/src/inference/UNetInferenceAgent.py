"""
Contains class that runs inferencing
"""
import torch
import numpy as np
import torch.nn.functional as F

from networks.RecursiveUNet import UNet

from utils.utils import med_reshape

class UNetInferenceAgent:
    """
    Stores model and parameters and some methods to handle inferencing
    """
    def __init__(self, parameter_file_path='', model=None, device="cpu", patch_size=64):

        self.model = model
        self.patch_size = patch_size
        self.device = device

        if model is None:
            self.model = UNet(num_classes=3)

        if parameter_file_path:
            self.model.load_state_dict(torch.load(parameter_file_path, map_location=self.device))

        self.model.to(device)

    def single_volume_inference_unpadded(self, volume):
        """
        Runs inference on a single volume of arbitrary patch size,
        padding it to the conformant size first

        Arguments:
            volume {Numpy array} -- 3D array representing the volume

        Returns:
            3D NumPy array with prediction mask
        """        
        vol_padded = med_reshape(volume, new_shape=(volume.shape[0], self.patch_size, self.patch_size))

        return self.single_volume_inference(vol_padded)

    def single_volume_inference(self, volume):
        """
        Runs inference on a single volume of conformant patch size

        Arguments:
            volume {Numpy array} -- 3D array representing the volume

        Returns:
            3D NumPy array with prediction mask
        """
        self.model.eval()

        # Assuming volume is a numpy array of shape [X,Y,Z] and we need to slice X axis
        slices = []

        # TASK: Write code that will create mask for each slice across the X (0th) dimension. After 
        # that, put all slices into a 3D Numpy array. You can verify if your method is 
        # correct by running it on one of the volumes in your training set and comparing 
        # with the label in 3D Slicer.
        # <YOUR CODE HERE>

        for i in range(volume.shape[0]):
            image = volume[i]
            data = torch.reshape(torch.from_numpy(image), (-1, 1, self.patch_size, self.patch_size)).type(torch.float).to(self.device)
            prediction = self.model(data)
            prediction_softmax = F.softmax(prediction, dim=1)
            mask = torch.argmax(prediction_softmax.squeeze(), dim=0).cpu().detach()

            # add class 1 and 2
            slices.append(mask)

        masks = np.stack(slices)
        print("masks shape: ", masks.shape)
        return masks

