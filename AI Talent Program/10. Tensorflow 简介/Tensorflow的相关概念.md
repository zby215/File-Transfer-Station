该课程主要为大家讲授如下的内容：
- Tensorflow的基本概念和设计
- tensorflow的工作原理概览
- tensorflow的优点


1. tensorflow的基本概念
	Tensorflow是一个集成了许多设计模式和功能的AI系统。从编程的观点来看，tensorflow是一个库（library），提供了在机器学习尤其是深度学习工程中可复用的数据结构和功能。
	[[什么是tensorflow.png]]
2. tensorflow的设计概述
	Tensorflow有一套垂直分级的设计，能够提供不同层次的API和相应的功能供开发者使用。
	[[tensorflow的设计.png]]
3. tensorflow的工作原理概览
	1. dataflow graph
		dataflow graph（在pytorch中被称为computational graph或计算图）是一种优化计算的设计。它能够规划计算流程，存储计算状态，并因此而能够引入并行计算功能来加速AI算法。
		[[简单了解tensorflow的工作原理.png]]
	2. tensor
		从纯理论上来讲，Tensor是可以用于表示一切数据的高维数组，可以存储深度学习模型中的参数。Tensorflow中的tensor类型数据集成了并行计算的设计，可以在内存和现存之间互相转移、高效利用计算资源。
		[[简单了解tensorflow的工作原理(2).png]]
		通过打开tensorflow中的调试选项，可以观察到该类型的数据在运算时的一些状态。
		[[tensorflow的例子.png]]

4. tensorflow的优点
	Tensorflow的设计使得它具有一系列优点，包括
	1) 帮助开发者快速构建模型
	2) 计算效率高
	3) 可迁移性好
	4) 功能丰富


---
