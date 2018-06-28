# Modified Implementation of AlexNet

This AlexNet implementation in this repository is based on 
the implementation by [kratzert](https://github.com/kratzert/finetune_alexnet_with_tensorflow).

The AlexNet architecture in this implementation deviates from the
original implementation, so as to use the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)
dataset, which are smaller in dimensions compared to the ImageNet images.

## Content

- `alexnet.py`: Class with the graph definition of the AlexNet.
- `AlexNet Train.ipynb`: Notebook to train and test the implementation of AlexNet.
