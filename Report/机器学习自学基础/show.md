## Logistic

解决问题

1. 两分类
2. 线性可回归问题

复习一下回归的定义 : 加入现在又一些数据点，我们用一条直线对这些点做拟合，期望得到最佳拟合直线，拟合的过程叫做回归

在拟合问题中，主要的思想在于我们拟合良好的数据预测回归公式

Logistic就是经典的一个拟合的实例，这是一个标准的二值型输出分类器 : 

我们对于每一个数据集的特征都创建一个对应的回归系数，每一个特征对最后的分类的结果都存在贡献，我们目的就是对于拟合一组这样的系数使得我们对于分类的结果在训练集上很优秀，并在之后的数据集上泛化的很好

$$z=w_0x_0+w_1x_1+w_2x_2+...+w_nx_n$$

在这里我们的$$X$$是分类器的输入数据，$$W$$是迭代找的最佳系数

### Gradient descent

高数中我们都学习如何快速的求一个函数的最优值，我们通常使用的一个重要的工具叫做梯度

我们可以理解梯度就是我们朝最优值变化的一个趋势，沿这个趋势可以最快的到达目的地(当然这是微分上的概念，实际上我们还需要考虑**步长(震荡)**和局部最优的情况)

$$x_{k+1} = x_k + \rho_k\bigtriangledown^{k}$$

这里的公式就渗透了我们的利用梯度求解最优值的迭代过程

问题

1. 但是这里会引出来一个之后会显现的很重要的问题 : 步长(步长太短算法收敛的很慢，步长太大，算法容易发散并且会出现频繁的在最有值附近震荡的情况)，解决办法主要办法就是动态步长选取,这是后话了，之后会讲到
2. 迭代次数(迭代多少次可以处于良好的误差范围中)

如何利用梯度下降求解Logistic算法

1. 首先引入感知器神经元

   ![感知器神经元](/home/lantian/File/Study/Report/机器学习自学基础/感知器神经元.png)

感知器神经元是一种现行分类器，包含一个算法框架和一个激活函数，在这里我们的算法框架就是我们的公式

$$z=w_0x_0+w_1x_1+w_2x_2+...+w_nx_n$$

激活函数需要讲一下 ： 

对于这个现行分类的问题，我们需要的目的是接收出入然后预测输出，因为是二值型的数值分类器我们要求是输出0,1代表两种不同的分类方式

一般来说我们对于这种输出0,1的函数(激活函数)最有印象的就是

![hardlim函数](/home/lantian/File/Study/Report/机器学习自学基础/hardlim函数.png)

这是一个0,1阶跃函数，我们又称是hardlim函数，针对我们的算法框架的输出，该函数可以生成对应的份额里标准，这好像就是我们的需要的答案了

---

**算法的目标：**

训练我们的参数，是的经过参数的迭代求出的$$z$$在经过我们的激活函数之后可以**误差很小**的将数据集正确的区分开来，之后我们会更形象的看出来

这样的化，我们聚会很清楚的发现，这个问题就会变成基础的最优化问题，只不过这里的优化目标比较复杂而已，对于最优化问题，我们就可以考虑使用梯度的方法来解决

---

但是在这里，我们的梯度是什么?好像很难找到适用于该题目的梯度的概念

我们可以将梯度形象的理解成是我们当前的分类拟合出来的参数$$W$$针对我们的数据集的拟合出来的误差，我们的目标无非就是要让误差下降

**算法的思路有了:**

1. 收集数据(特征 ， label标签(目标))

2. 确定迭代次数，和迭代的步长

3. 确定初始化的$$W$$参数向量

4. 迭代公式

   $$f(x)=w^{T}x$$

   $$error=label-hardlim(f(x))$$

   $$w_{k+1}=w_k+\alpha x^{T} error$$

   训练参数向量

### Sigmod or Hardlim

Hardlim函数：可以看出来在0的附近是非常的剧烈的变化的，是阶跃的

Sigmod函数 :

sigmod函数相对于hardlim更稳定的原因在于引入了概率，这样可以为算法提供一个平稳的分类的便捷，保证在迭代次数增大的同时我们的算法也会收敛的很好，更稳定

但是这样类似的曲线有很多，为什么一定要用sigmod函数呢

1. 我们之前应该还记的，我们对应这个最优化问题，使用功能的梯度的表达是是$$w^Tx$$

   这个表达式的含义在于我们的对$$w$$向量和$$x$$向量求内积，这个表示我们的算法的计算结果，这个计算结果之后要带入我们的激活函数中去进行分类

![远看sigmod函数](/home/lantian/File/Study/Report/机器学习自学基础/远看sigmod函数.png)

![近看sigmod函数](/home/lantian/File/Study/Report/机器学习自学基础/近看sigmod函数.png)

在logistic 和 Sigmod都讲完之后演示两张图表示出回归的效果的差距(同迭代次数下)

硬限符函数不是一个连续的函数，在一个很小的区间内，函数变化会非常的剧烈，目标函数会发生很剧烈的震荡，决策的便捷汇编的非常的狭窄，严重的而影响我们额分类精度和评估的结果





为了方便直观的说明问题，这里的数据有两个特征，100的数据量，我们的目的就是拟合出来一个参数向量可以将我们的两中类别尽可能的分类开

![测试用例](/home/lantian/File/Study/Report/机器学习自学基础/测试用例.png)



hardlim 500

错误分类 : 2

![hardlim500](/home/lantian/File/Study/Report/机器学习自学基础/hardlim500.png)

hardlim 501

错误分类 : 5

![hardlim501](/home/lantian/File/Study/Report/机器学习自学基础/hardlim501.png)

sigmod 500

错误分类 : 2

![sigmod500](/home/lantian/File/Study/Report/机器学习自学基础/sigmod500.png)

sigmod 501

错误分类 : 2

![sigmod501](/home/lantian/File/Study/Report/机器学习自学基础/sigmod501.png)

可以看出来分类的结果是非常的稳定的

### ML

在我们继续讲解之前，需要引入最大似然估计的概念

有一组数据量是m的数据集，每一个数据都是有一个**未知**但是**真实**的概率分布独立的生成的，我们想要找到一个概率分布是的尽可能和我们的这个未知的真实分布是一致的就是最大似然法需要解决的问题

**最大似然的核心**

因此我们可以将最大似然法看做是尝试的模型的分布尽可能的和经验分布一致匹配的一种尝试，理想的情况下，我们希望匹配真实数据的真实分布，但是我们知道真实分布是不可能的，因为我们对这个真实的分布一无所知



让我们来重新的看待这个问题，假设生成这个数据集的分布是一个我们未知的分布，我们现在想要模拟的向量$$W$$实际上就是在数据集$$X$$上去找他的联合分布模型情况(一个特征就是一个概率分布，多个特征就是查找联合分布)



**最大似然的优点**

- 已经被证明，当使用的样本数目越多，我们的估计越准确，当样本数目足够多的时候，参数会收敛到参数的真实值



我们一开始假设的样本之间是相互独立的，所以联合分布就是独立分布的乘积

1. 第一个公式很好理解，带包的意思就是当对应的样本的label是1的时候选取前者计算我们的概率

   否则使用后者计算概率

2. 因为概率的乘积运算容易导数值下溢，并且乘法不好计算，所以我们通常使用对数似然转化成加法，并且显然，对数似然并不改变任何性质

3. 这里就凸显出logsitic函数好处,下面的计算公式在最大似然公式推到中会使用
   $$
   P\{Y=1|x\}=p(x)=\frac{1}{1+e^{-w^Tx}} \\
   P\{Y=0|x\}=p(x)=\frac{1}{1+e^{w^Tx}} \\
   ln(\frac{P\{Y=1|x\}}{P\{Y=0|x\}})=ln\frac{p(x)}{1-p(x)}=w^Tx
   $$
   ​

$$
l(w)=\Pi^{n}_{i=1}(P\{Y=1|x_i\})^{y_i}(1-P\{Y=1|x_i\})^{1-y_i}  \\
L(w)=ln(l(w))=\Sigma_{i=1}^{n}y_iw^Tx_i-\Sigma_{i=1}^{n}ln(1+e^{w^Tx})  \\
最小化目标函数(w的函数)等价于最大似然估计，求导计算最大似然估计 \\
求导计算梯度我们，要让后面的一部分就是sigmod函数，而不是其他的类似sigmod性质的其他函数，这样可以保证我们的最大似然法是最精确的  \\
\frac{\partial L(w)}{\partial w} = \Sigma_{i=1}^ny_ix_i-\Sigma^u_{i=1}\frac{e^{w^Tx_i}}{1+e^{w^Tx_i}}x_i =\Sigma^n_{i=1}(y_i-\frac{1}{1+e^{-w^Tx_i}})x_i   \\
$$

代码

```python
def sigmod(inx):
    return 1.0 / (1 + exp(-inx))

def hardlim(inx):
    h = []
    for i in inx:
        if i < 0 : h.append(0)
        else : h.append(1)
    return mat(h).transpose()

def logistic(datamat , label):
    datamatrix = mat(datamat)
    labelmat = mat(label).transpose()
    m , n = shape(datamatrix)
    alpha = 0.001
    step = 501
    weights = ones((n,1))
    # 利用最大似然法的批量梯度下降
    for i in range(step):
        h = sigmod(datamatrix * weights)    # 计算后一项
        error = (labelmat - h)    # 计算误差，上面的yi-...
        weights += alpha * datamatrix.transpose() * error    # 最后一个乘法代表的计算梯度，只不过是矩阵的形式而已
    return weights
```

显然hardlim或者其他的和logistic的性质类似的函数都没有办法做到和logistic函数一样的效果

#### BGD

批量梯度下降算法，是最原始的一种梯度下降算法，对于整个数据集进行遍历操作，可以尽可能的保证我们的回归系数的精度，但是带来的缺点显而易见

一旦我们的数据集的个数和我们的特征的数目变得异常的巨大，我们的计算量是非常的庞大的，甚至是不可接收的

#### SGD

```python
def soclogistic(datamat , label):
    import random
    datamatrix = array(datamat)
    m , n = shape(datamat)
    weights = ones(n)
    for j in range(500):
        dataindex = list(range(m))
        for i in range(m):
            alpha = 4 / (i + j + 1.0) + 0.01
            randomindex = random.randint(0,len(dataindex) - 1)
            h = sigmod(sum(datamatrix[randomindex] * weights))
            error = label[randomindex] - h
            weights = weights + alpha * error * datamatrix[randomindex]
            del(dataindex[randomindex])
        return weights
```

为了弥补BGD的缺陷，SGD的核心在于在数据量庞大的时候，我们随机抽取的数据集其实可以当做整体数据集影响的近似估计，我们从训练集中抽取出一小批量的样本作为本次迭代的数据集(该样本集的大小基本不随数据量的变大而变化)

**假设现在有100个样本，100个特征,100次迭代，乘法次数 : **

* BGD : (100 * 100 + 100 * 100) * 100 = 2 * E6

* SGD : (100 + 100) * 100 * 50 = E5

  (该样本集的大小基本不随数据量的变大而变化),所以就算数据集是庞大的，我们的只要抽取的样本小就可以，而起而只要样本狗随机，可以达到和批量梯度下降差不多的拟合结果)

![sgd150vsbgd500](/home/lantian/File/Study/Report/机器学习自学基础/sgd150vsbgd500.png)

## K-Means



### Hyperparameter and validation set

### KFoldXV

## Difficulty

### Curse of dimensionality

### PCA

### Maniford

## Create some ML Algorithm 

