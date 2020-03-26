import oldtensorflow as tf
import numpy as np


def upsample(x):
    """
    Apply a two times upsample on x and return the result.
    :x: 4-Rank Tensor
    :return: TF Operation
    """
    # TODO: Use `tf.layers.conv2d_transpose`
    return tf.layers.conv2d_transpose(x,3,(2,2),(2,2))

#The second argument 3 is the number of kernels/output channels.
#The third argument is the kernel size, (2, 2).
#Note that the kernel size could also be (1, 1) and the output shape
#would be the same. However, if it were changed to (3, 3) note the shape
#would be (9, 9), at least with 'VALID' padding.
#
#The fourth argument, the number of strides, is how we get from a
#height and width from (4, 4) to (8, 8). If this were a regular convolution
#the output height and width would be (2, 2).


x = tf.constant(np.random.randn(1, 4, 4, 3), dtype=tf.float32)
conv = upsample(x)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run(conv)

    print('Input Shape: {}'.format(x.get_shape()))
    print('Output Shape: {}'.format(result.shape))
