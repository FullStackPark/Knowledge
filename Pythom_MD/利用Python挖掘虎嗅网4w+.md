![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522820595971aa1932277f)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/15228206024404bda89c4e4)

**1 分析背景**

****1.1** **分析原理---为什么选择分析虎嗅网****

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228206651559518937293)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522820672721cbad9f3ed3)

综合上述两类情形，可以得出这样的结论，透过社会化媒体，我们可以观察现实世界：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228206790022a183d0a5f)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522735902233cc00b649be)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522820761306afda8fc187)

因此，对该平台上的发布内容进行分析，对于研究互联网的发展进程和现状有一定的实际价值。

**1.2 本文的分析目的**

笔者在本项目中的分析目的主要有4个：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522820784279c21771064a)

**1.3** **分析方法---分析工具和分析类型**

本文中，笔者使用的数据分析工具如下：

* Python3.5.2（编程语言）

* Gensim（词向量、主题模型）

* Scikit-Learn（聚类和分类）

* Keras（深度学习框架）

* Tensorflow（深度学习框架）

* Jieba(分词和关键词提取)

* Excel（可视化）

* Seaborn（可视化）

* 新浪微舆情（情绪语义分析）

* Bokeh（可视化）

* Gephi（网络可视化）

* Plotly（可视化）

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282081271778ae420017)

**2** **数据采集和文本预处理**

**2.1** **数据采集**

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282083547204437e6fc9)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522820845319f5d6a0d86d)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522820860276f6a4abaabf)

【全模式】: 新浪/ 微舆情/ 新浪微舆情/ 专注/于/ 社会化/ 大数据/ 社会化大数据/ 的/ 场景化/ 应用

【精确模式】: 新浪微舆情/ 专注/于/ 社会化大数据/ 的/ 场景化/ 应用

【搜索引擎模式】：新浪，微舆情，新浪微舆情，专注，于，社会化，大数据，社会化大数据，的，场景化，应用

为了避免歧义和切出符合预期效果的词汇，笔者采取的是精确（分词）模式。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228208787748d86e95982)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522820896036a81a6e4691)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/1522820914734890ec69fdf)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228209328433acd421495)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522820942066b852779ab8)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282095991563e1581bdb)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522820970804bbacd36ab3)

**3.2** **发文时间规律分析**

笔者从时间维度里提取出“周”和“时段”的信息，也就是开题提到的“人工特征”的提取，现在做文章分布数量的在“周”和“时”上的交叉分析，得到下图：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228209777691c25d3766f)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282100092460fca68b8c)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522821016921de49a0d29e)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821023497a6163428f5)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821036595fe60b3140e)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282104346963ff288079)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282106047459231930a6)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282107369286f088de85)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228210790370b19bb8e7f)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228210939638eed71995a)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228211124956b80079b36)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/152282112150700ae38945d)

将上述结果绘制成如下动态的流向图：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282112905942d18de4df)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821151053827aebe83d)

上面的数据分析是基于数值型数据的描述性分析，接下来，笔者将进行更为深入的文本挖掘。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522821199046218ee2c0e1)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/1522821220003f85456a756)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/152282123895933153e9159)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228212484795965dc38a2)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821259119abcda1e63a)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522821263719b30cd7516d)

**4.2 LDA**  **主题模型分析**

刚才针对关键词的分类较为粗略，且人为划分，难免有失偏颇，达不到全面的效果。因此，笔者采用LDA主题模型来发现该语料中的潜在主题。关于LDA主题模型的相关原理，

一般情况下，笔者将主题的数量设定为10个，经过数小时的运行，得到如下结果：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282127308334b0d581df)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/152282128669769b42f3881)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228212956235e37c103cf)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821299265a01dbf7cca)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228214393119c46ddc4fd)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228215205584399faf8a5)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/1522821532548d8cb5bace3)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228215428302a32a2dbe7)

从老罗的写作主题及其概率分布来看，他比较倾向于写创业、融资、智能手机和新媒体营销方面的文章，这个比较符合大众认知，因为善打情怀牌的老罗喜欢谈创业、谈自己对于手机的理解，而且由于自己鲜明的个性和犀利的语言，他常常在为自己的锤子品牌代言。

根据文档ID，笔者找到了他发布的这几篇文章：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228215551859455622fa3)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228215618271dc02faabe)

接下来是虎嗅自己的媒体，主页上发文量破万，所涉及的写作主题集中在“行业新闻”、“智能手机”和“新媒体&营销”：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282157639957360ae986)

与其写作主题类似的作者除了一些个人自媒体人，还包括一些媒体，如环球网、财富中文网、彭博商业周刊等。从前面的分析中可以推测出，他们在上述3个话题上的发文量也比较大。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/152282157632785faeb397c)

在这10,189篇文章里，笔者按文档ID随机抽取出其中的若干篇文章的标题，粗略验证下。然后，把这些标题绘制成独角兽形状的词云。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228215763286d12e74fc1)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228215763558ad935143e)

由上面的标题及其关键词云，预测的主题还是比较合理的。

再看看另外两个笔者比较感兴趣的自媒体---混沌大学和21世纪经济报道。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/1522821582017bf70baad79)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228215820095034209e41)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522821588412898792784e)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282160204976323982fd)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228216169932fafd03787)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282162403351b030fead)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/1522821642754032fe2a389)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821662400ecac16e449)

接下来，通过Word2vec，笔者查找出自己感兴趣的若干词汇的关联词，从而在虎嗅网的这个独特语境下去解读它们。

由此，笔者依次对“百度”、“人工智能”、“褚时健”和“罗振宇”这几个关键词进行关联词分析。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/152282167210898648b5d72)

出来的都是与百度相关的词汇，不是百度的产品、公司，就是百度的CEO和管理者，“搜索”二字变相的出现了很多次，它是百度起家的一大法宝。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522821679906f7e658cdc7)

与“AI”相关的词汇也是很好的解释了人工智能的细分领域和目前比较火的几个应用场景。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/152282167990692012f028c)

与褚时健一样，相关词中前几位名人（牛根生、胡雪岩、鲁冠球、王永庆和宗庆后）也是名噪一时的商业精英，“老爷子”、“褚老”、“橙王”是外界对其的尊称。有意思的是，褚老也有一些政治人物（毛主席和蒋委员长）那样的英雄气概，其人其事大有“**东隅已逝，桑榆非晚**”、“**待从头，收拾旧山河**”的豁达精神和乐观主义！

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228216799231e6007e1fe)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/15228216871025b68ef778d)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228217068696ac02ad9b2)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821712987bb52d52953)

对于上述百强互联网公司的旗下品牌名录，笔者利用上面训练出来的词向量模型，用来进行下面的词聚类和词分类。

**4.7.1** **词聚类**

运用基于Word2Vec（词向量）的K-Means聚类，充分考虑了词汇之间的语义关系，将余弦夹角值较小的词汇聚集在一起，形成簇群。下图是高维词向量压缩到2维空间的可视化呈现：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/152282172099680f0beb3b6)

笔者将词向量模型中所包含的所有词汇划定为300个类别，看看这种设定下的品牌聚类效果如何。分析结果和规整如下所示：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228217271838064897d56)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821727253dabb295e7b)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228217506620cd14c1169)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282176691657fbcb8993)

**4.7.2** **词分类**

在这里，笔者还是利用之前训练得出的词向量，通过基于CNN（ ConvolutionalNeural Networks，卷积神经网络）做文本分类，用来预测。CNN的具体原理太过复杂，笔者在这里不做赘述，感兴趣的小伙伴可以查阅后面的参考资料。

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228217745340a9948f821)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821789592a5f41a5e0f)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522821794806f99ce4c44d)

接着，笔者用之前未出现在训练语料中的词来检验效果，出来的结果是类别标签及其对应的概率，概率值大的类别是品牌最有可能从属的细分领域。结果如下图所示：

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/1522821801275e0d12c3a3c)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p9.pstatp.com/large/pgc-image/1522821801275e3dc906e19)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/152282180129073f4543675)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228218012837344209385)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821809724fe4512c139)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/1522821823983cf3ec0e272)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/1522821841111abbb36b224)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228218476118335941d99)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p1.pstatp.com/large/pgc-image/15228218681277d9ad4d3ba)

再看由颜色区分出的6个簇群：

> * **淡蓝系**：腾讯、微信、百度、QQ、网易、搜狐…
>
> * **洋红系**：阿里巴巴、淘宝、京东、新浪微博、天猫…
>
> * **深绿系**：小米、多看、MIUI、天翼阅读…
>
> * **浅绿系**：乐居、房天下
>
> * **明黄系**：人人贷、拍拍贷
>
> * **黄橙系**：汽车之家、易车网、易湃
>

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/15228218865864179433514)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282189488351683432b8)

![从零到项目实战！利用Python挖掘虎嗅网4w+文章！找工作随便找！](http://p3.pstatp.com/large/pgc-image/152282191408068fa3c5269)

如有编程请联系小编删除！好东西大家分享！
