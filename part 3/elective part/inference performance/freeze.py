cd /home/ubuntu/inference-walkthrough/src
base_graph.pb 
checkpoint
ckpt.data-00000-of-0000
ckpt.index
ckpt.meta
graph_utils.py
~/tensorflow/bazel-bin/tensorflow/python/tools/freeze_graph \
--input_graph=base_graph.pb \
--input_checkpoint=ckpt \
--input_binary=true \
--output_graph=frozen_graph.pb \
--output_node_names=Softmax


def load_graph(graph_file, use_xla=False):
    jit_level = 0
    config = tf.ConfigProto()
    if use_xla:
        jit_level = tf.OptimizerOptions.ON_1
        config.graph_options.optimizer_options.global_jit_level = jit_level

    with tf.Session(graph=tf.Graph(), config=config) as sess:
        gd = tf.GraphDef()
        with tf.gfile.Open(graph_file, 'rb') as f:
            data = f.read()
            gd.ParseFromString(data)
        tf.import_graph_def(gd, name='')
        ops = sess.graph.get_operations()
        n_ops = len(ops)
        return sess.graph, ops


    
from graph_utils import load_graph

sess, base_ops = load_graph('base_graph.pb')
print(len(base_ops)) # 2165
sess, frozen_ops = load_graph('frozen_graph.pb')
print(len(frozen_ops)) # 245
