# Modified Implementation of AlexNet

The AlexNet implementation in this repository is based on 
the implementation by [kratzert](https://github.com/kratzert/finetune_alexnet_with_tensorflow).

The AlexNet architecture in this implementation deviates from the
original implementation, so as to use the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)
dataset, which are smaller in dimensions compared to the ImageNet images.

Beside the comments in the code itself, I also wrote an article which you can find [here](https://mohitjain.me/2018/06/06/alexnet/) with further explanations on AlexNet.

## Content

- `alexnet.py`: Class with the graph definition of the AlexNet.
- `AlexNet Train.ipynb`: Notebook to train and test the implementation of AlexNet.

If you are having trouble viewing the notebook file, click [here](http://nbviewer.jupyter.org/github/Natsu6767/Modified-AlexNet-Tensorflow/blob/master/AlexNet%20Train.ipynb).
