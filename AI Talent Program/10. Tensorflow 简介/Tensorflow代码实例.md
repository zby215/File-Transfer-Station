该课程主要为大家讲授如下的内容：
- Tensorflow代码实例


1. 范例模型
	范例模型是一个word embeddings+LSTM+Dense处理情感分析任务的模型。数据导入自tf.keras.datasets中的IMDB影评数据集，经过对齐处理后输入模型进行训练，得到的是一个连续的标量。最后自定义编码函数录入实时定义的字符串，得到预测结果。
	[[Tensorflow代码实例.png]]
	[[Tensorflow代码实例(2).png]]