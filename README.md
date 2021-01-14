# Feed

## 介绍

本repo是一个RSS的内容更新repo，使用github action实现新消息的更新。

每小时拉取[RSS列表](./list.txt)中的RSS源，并将内容更新在每页上。

历史存档在[这里](./ARCHIVED.md)

### TODO

- [ ] 将RSSHUB迁移到repo上，直接在更新时构建RSSHUB镜像然后本地读取对应端口信息
- [ ] 实现最README页直接展示今天新更新的信息
- [ ] 重新设计sqlite3数据库中字段信息，包括但不限于文章更新时间、拉取时间，文章标题，文章正文内容等
- [ ] 优化更新和对比效率
- [ ] 做好所有rss源适配

## 今日更新

# 2021-1-15

### error read: http://www.jintiankansha.me/rss/GEYDCOBUPRRWGMDBGFSDIZTGMM2GCZRVMQZGGNRQHBRTQZLEME4TQYLFGJRDKZBTGI2TSZJUGM======

### [社保卡何时全国统一？人社部回应来了](https://m.21jingji.com/article/20210114/herald/f7adc120208595ee589f45f7633407fc.html)

### [nacos 出现严重安全漏洞，特殊 UA 可以绕过所有鉴权，有用了的小伙伴注意了……](https://www.v2ex.com/t/744865)

### [首次发现非光合细菌中的生物钟](http://jandan.net/p/108331)

### [知道什么是抗营养素吗](http://jandan.net/p/108346)

### [一美男子血液中长出“致幻蘑菇”](http://jandan.net/p/108349)

### [火车千足虫每8年就会席卷日本山区](http://jandan.net/p/108342)

### [Virtual Machine Startup Shells Closes the Digital Divide One Cloud Computer at a Time](https://www.linuxjournal.com/content/virtual-machine-startup-shells-closes-digital-divide-one-cloud-computer-time)

### [【OpenSocial Specification】网页链接 开放社会规范。 [图片]](https://weibo.com/1715118170/JDcEYxBOG)

### [【Lulu – Mac open-source firewall that aims to block unknown outgoing connections】网页链接 Lulu – Mac开源防火墙，旨在阻止未知的传出连接。网路冷眼技...](https://weibo.com/1715118170/JDcsIBGDu)

### [#绿洲摄影#中国.云南.大理.洱海.小普陀 绿洲 [图片]](https://weibo.com/1715118170/JDcmqeVFH)

### [【Superintelligence cannot be contained: Lessons from Computability Theory】网页链接 论 文《不能包含超级智能：可计算性理论的教训》。 [图片]](https://weibo.com/1715118170/JDcgVf5qk)

### [【A cool Drag-and-Drop implementation for Svelte】网页链接 Svelte的一个很酷的拖放实现。 网路冷眼技术分享 #科技暖心季# [图片]](https://weibo.com/1715118170/JDc4myjSV)

### [Recognizing Pose Similarity in Images and Videos](http://feedproxy.google.com/~r/blogspot/gJZg/~3/3l_KQibU2Bw/recognizing-pose-similarity-in-images.html)

 <span class="byline-author">Posted by Jennifer J. Sun, Student Researcher and Ting Liu, Senior Software Engineer, Google Research</span> <p>Everyday actions, such as jogging, reading a book, pouring water, or playing sports, can be viewed as a sequence of <a href="https://en.wikipedia.org/wiki/Pose_(computer_vision)">poses</a>, consisting of the position and orientation of a person’s body. An understanding of poses from images and videos is a crucial step for enabling a range of applications, including <a href="https://ai.googleblog.com/2019/03/real-time-ar-self-expression-with.html">augmented reality</a> display, <a href="https://blog.google/technology/ai/move-mirror-you-move-and-80000-images-move-you/">full-body gesture control</a>, and <a href="https://ai.googleblog.com/2020/06/repnet-counting-repetitions-in-videos.html">physical exercise quantification</a>. However, a 3-dimensional pose captured in two dimensions in images and videos appears different depending on  the viewpoint of the camera. The ability to recognize similarity in 3D pose using only 2D information will help vision systems better understand the world. </p><p>In “<a href="https://arxiv.org/abs/1912.01001">View-Invariant Probabilistic Embedding for Human Pose</a>” (Pr-VIPE), a spotlight paper at <a href="https://eccv2020.eu/">ECCV 2020</a>, we present a new algorithm for human pose perception that recognizes similarity in human body poses across different camera views by mapping <a href="https://cocodataset.org/#keypoints-2020">2D body pose keypoints</a> to a view-invariant embedding space. This ability enables tasks, such as pose retrieval, action recognition, action video synchronization, and more. Compared to <a href="https://openaccess.thecvf.com/content_ICCV_2017/papers/Martinez_A_Simple_yet_ICCV_2017_paper.pdf">existing models</a> that directly map 2D pose keypoints to 3D pose keypoints, the Pr-VIPE embedding space is (1) view-invariant, (2) <a href="https://en.wikipedia.org/wiki/Normal_distribution">probabilistic</a> in order to capture 2D input ambiguity, and (3) does not require <a href="https://en.wikipedia.org/wiki/Camera_resectioning#Projection">camera parameters</a> during training or inference. Trained with in-lab setting data, the model works on in-the-wild images out of the box, given a reasonably good 2D pose estimator (e.g., <a href="https://arxiv.org/pdf/1803.08225.pdf">PersonLab</a>, <a href="https://ai.googleblog.com/2020/08/on-device-real-time-body-pose-tracking.html">BlazePose</a>, among others). The model is simple, results in compact embeddings, and can be trained (in ~1 day) using 15 CPUs. We have released the code on <a href="https://github.com/google-research/google-research/tree/master/poem">our GitHub repo</a>.  </p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-RNUg7WWiVhI/X_91h1QzsBI/AAAAAAAAG_4/B2wCJOoi-ssxWb9rfydHk3YGUsxWA895ACLcBGAsYHQ/s640/image16.gif" style="margin-left: auto; margin-right: auto;"><img border="0" height="570" src="https://1.bp.blogspot.com/-RNUg7WWiVhI/X_91h1QzsBI/AAAAAAAAG_4/B2wCJOoi-ssxWb9rfydHk3YGUsxWA895ACLcBGAsYHQ/w640-h570/image16.gif" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Pr-VIPE can be directly applied to align videos from different views.</td></tr></tbody></table><p><b>Pr-VIPE </b><br />The input to Pr-VIPE is a set of 2D keypoints, from any 2D pose estimator that produces a minimum of <a href="https://cocodataset.org/#keypoints-2020">13 body keypoints</a>, and the output is the <a href="https://en.wikipedia.org/wiki/Normal_distribution">mean and variance</a> of the pose embedding. The distances between embeddings of 2D poses correlate to their similarities in absolute 3D pose space. Our approach is based on two observations: </p><ul><li>The same 3D pose may appear very different in 2D as the viewpoint changes. </li><li>The same 2D pose can be <a href="https://en.wikipedia.org/wiki/3D_projection#Perspective_projection">projected</a> from different 3D poses. </li></ul><p>The first observation motivates the need for view-invariance. To accomplish this, we define the <em>matching probability</em>, i.e., the likelihood that different 2D poses were projected from the same, or similar 3D poses. The matching probability predicted by Pr-VIPE for matching pose pairs should be higher than for non-matching pairs. </p><p>To address the second observation, Pr-VIPE utilizes a probabilistic embedding formulation. Because many 3D poses can project to the same or similar 2D poses, the model input exhibits an inherent ambiguity that is difficult to capture through <a href="https://en.wikipedia.org/wiki/Deterministic_algorithm">deterministic</a> mapping point-to-point in embedding space. Therefore, we map a 2D pose through a probabilistic mapping to an embedding distribution, of which we use the variance to represent the uncertainty of the input 2D pose. As an example, in the figure below the third 2D view of the 3D pose on the left is similar to the first 2D view of a different 3D pose on the right, so we map them into a similar location in the embedding space with large variances. </p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-UxnxKO-tuG4/X_92DyZPcHI/AAAAAAAAHAA/f5p28lqJbochbIg-FU0Vj9CzvXVXzz-TwCLcBGAsYHQ/s954/image6.jpg" style="margin-left: auto; margin-right: auto;"><img border="0" height="406" src="https://1.bp.blogspot.com/-UxnxKO-tuG4/X_92DyZPcHI/AAAAAAAAHAA/f5p28lqJbochbIg-FU0Vj9CzvXVXzz-TwCLcBGAsYHQ/w640-h406/image6.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Pr-VIPE enables vision systems to recognize 2D poses across views. We embed 2D poses using Pr-VIPE such that the embeddings are (1) view-invariant (2D projections of similar 3D poses are embedded close together) and (2) probabilistic. By embedding detected 2D poses, Pr-VIPE enables direct retrieval of pose images from different views, and can also be applied to action recognition and video alignment.</td></tr></tbody></table><em>View-Invariance</em><br />During training, we use 2D poses from two sources: <a href="http://vision.imar.ro/human3.6m/description.php">multi-view images</a> and <a href="https://en.wikipedia.org/wiki/3D_projection#Perspective_projection">projections</a> of groundtruth 3D poses. <a href="https://en.wikipedia.org/wiki/Triplet_loss">Triplets</a> of 2D poses (anchor, positive, and negative) are selected from a batch, where the anchor and positive are two different projections of the same 3D pose, and the negative is a projection of a non-matching 3D pose. Pr-VIPE then estimates the matching probability of 2D pose pairs from their embeddings. <br />During training, we push the matching probability of positive pairs to be close to 1 with a positive pairwise loss in which we minimize the embedding distance between positive pairs, and the matching probability of negative pairs to be small by maximizing the ratio of the matching probabilities between positive and negative pairs with a triplet ratio loss.  <br /><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-jghZ4_x8VeM/X_92Pzy896I/AAAAAAAAHAE/UsuxcBVMGacJQX6UOuyfiXBD1g-aA_A8wCLcBGAsYHQ/s1254/image13.jpg" style="margin-left: auto; margin-right: auto;"><img border="0" height="230" src="https://1.bp.blogspot.com/-jghZ4_x8VeM/X_92Pzy896I/AAAAAAAAHAE/UsuxcBVMGacJQX6UOuyfiXBD1g-aA_A8wCLcBGAsYHQ/w640-h230/image13.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Overview of the Pr-VIPE model. During training, we apply three losses (triplet ratio loss, positive pairwise loss, and a prior loss that applies a unit Gaussian prior to our embeddings). During inference, the model maps an input 2D pose to a probabilistic, view-invariant embedding.</td></tr></tbody></table><em>Probabilistic Embedding</em><br />Pr-VIPE maps a 2D pose to a probabilistic embedding as a <a href="https://en.wikipedia.org/wiki/Multivariate_normal_distribution">multivariate Gaussian distribution using</a> a <a href="https://arxiv.org/abs/1810.00319">sampling-based approach</a> for similarity score computation between two distributions. During training, we use a Gaussian prior loss to regularize the predicted distribution. <p><b>Evaluation</b><br />We propose a new <em>cross-view pose retrieval</em> benchmark to evaluate the view-invariance property of the embedding. Given a monocular pose image, cross-view retrieval aims to retrieve the same pose from different views without using camera parameters. The results demonstrate that Pr-VIPE retrieves poses more accurately across views compared to baseline methods in both evaluated datasets (<a href="http://vision.imar.ro/human3.6m/description.php">Human3.6M</a>, <a href="http://gvv.mpi-inf.mpg.de/3dhp-dataset/">MPI-INF-3DHP</a>). </p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-dqjpSmDUuVk/X_92X439bRI/AAAAAAAAHAM/ODgkBCGa23wYpVgwEMhQ6k_9pmkZSyv2gCLcBGAsYHQ/s1611/image9.png" style="margin-left: auto; margin-right: auto;"><img border="0" height="290" src="https://1.bp.blogspot.com/-dqjpSmDUuVk/X_92X439bRI/AAAAAAAAHAM/ODgkBCGa23wYpVgwEMhQ6k_9pmkZSyv2gCLcBGAsYHQ/w640-h290/image9.png" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Pr-VIPE retrieves poses across different views more accurately relative to the baseline method (<a href="https://openaccess.thecvf.com/content_ICCV_2017/papers/Martinez_A_Simple_yet_ICCV_2017_paper.pdf">3D pose estimation</a>).</td></tr></tbody></table><p>Common 3D pose estimation methods (such as the <a href="https://openaccess.thecvf.com/content_ICCV_2017/papers/Martinez_A_Simple_yet_ICCV_2017_paper.pdf">simple baseline</a> used for comparison above, <a href="https://arxiv.org/abs/1904.03345">SemGCN</a>, and <a href="https://arxiv.org/abs/1903.02330">EpipolarPose</a>, amongst many others), predict 3D poses in camera coordinates, which are not directly view-invariant. Thus, <a href="https://en.wikipedia.org/wiki/Procrustes_analysis">rigid alignment</a> between every query-index pair is required for retrieval using estimated 3D poses, which is computationally expensive due to the need for <a href="https://en.wikipedia.org/wiki/Singular_value_decomposition">singular value decomposition</a> (SVD). In contrast, Pr-VIPE embeddings can be directly used for distance computation in Euclidean space, without any post-processing. </p><p><b>Applications</b><br />View-invariant pose embedding can be applied to many image and video related tasks. Below, we show Pr-VIPE applied to cross-view retrieval on in-the-wild images without using camera parameters.</p><p><i></i></p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-Y6wz_YqHthc/X_92-Pa-qOI/AAAAAAAAHAk/ez9D_xToW_sZE2Rwio4VQot0tFeezJw9ACLcBGAsYHQ/s1181/Pr-VIPE-InTheWild.png" style="margin-left: auto; margin-right: auto;"><img border="0" height="538" src="https://1.bp.blogspot.com/-Y6wz_YqHthc/X_92-Pa-qOI/AAAAAAAAHAk/ez9D_xToW_sZE2Rwio4VQot0tFeezJw9ACLcBGAsYHQ/w640-h538/Pr-VIPE-InTheWild.png" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;"></td></tr></tbody></table><i><br />We can retrieve in-the-wild images from different views without using camera parameters by embedding the detected 2D pose using Pr-VIPE. Using the query image (top row), we search for a matching pose from a different camera view and we show the nearest neighbor retrieval (bottom row). This enables us to search for matching poses across camera views more easily. </i><p></p><p>The same Pr-VIPE model can also be used for video alignment. To do so, we stack Pr-VIPE embeddings within a small time window, and use the <a href="https://en.wikipedia.org/wiki/Dynamic_time_warping">dynamic time warping</a> (DTW) algorithm to align video pairs.  </p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-4GrUP63WOvY/X_93G9b398I/AAAAAAAAHAo/zwnsATDSkGUW22to6BbZwPpToITe1QKMQCLcBGAsYHQ/s640/image1.gif" style="margin-left: auto; margin-right: auto;"><img border="0" height="570" src="https://1.bp.blogspot.com/-4GrUP63WOvY/X_93G9b398I/AAAAAAAAHAo/zwnsATDSkGUW22to6BbZwPpToITe1QKMQCLcBGAsYHQ/w640-h570/image1.gif" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Manual video alignment is difficult and time-consuming. Here, Pr-VIPE is applied to automatically align videos of the same action repeated from different views.</td></tr></tbody></table><p>The video alignment distance calculated via DTW can then be used for action recognition by classifying videos using <a href="https://en.wikipedia.org/wiki/Nearest_neighbor_search">nearest neighbor search</a>. We evaluate the Pr-VIPE embedding using the <a href="http://dreamdragon.github.io/PennAction/">Penn Action</a> dataset and demonstrate that using the Pr-VIPE embedding without fine-tuning on the target dataset, yields highly competitive recognition accuracy. In addition, we show that Pr-VIPE even achieves relatively accurate results using only videos from a single view in the index set. </p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-ah2jdq78hmE/X_93O1awojI/AAAAAAAAHAw/BwS5Kggqo80wlD82alhQdsQiOrhiaRUDwCLcBGAsYHQ/s1127/image15.png" style="margin-left: auto; margin-right: auto;"><img border="0" height="190" src="https://1.bp.blogspot.com/-ah2jdq78hmE/X_93O1awojI/AAAAAAAAHAw/BwS5Kggqo80wlD82alhQdsQiOrhiaRUDwCLcBGAsYHQ/w640-h190/image15.png" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Pr-VIPE recognizes action across views using pose inputs only, and is comparable to or better than methods using pose only or with additional context information (such as <a href="https://arxiv.org/abs/1603.04037">Iqbal et al.</a>, <a href="https://openaccess.thecvf.com/content_cvpr_2018/papers/Liu_Recognizing_Human_Actions_CVPR_2018_paper.pdf">Liu and Yuan</a>, <a href="https://arxiv.org/abs/1912.08077">Luvizon et al.</a>, and <a href="https://openaccess.thecvf.com/content_ICCV_2017/papers/Du_RPAN_An_End-To-End_ICCV_2017_paper.pdf">Du et al.</a>). When action labels are only available for videos from a single view, Pr-VIPE (1-view only) can still achieve relatively accurate results.</td></tr></tbody></table><p><b>Conclusion</b><br />We introduce the Pr-VIPE model for mapping 2D human poses to a view-invariant probabilistic embedding space, and show that the learned  embeddings can be directly used for pose retrieval, action recognition, and video alignment. Our cross-view retrieval benchmark can be used to test the view-invariant property of other embeddings. We look forward to hearing about what you can do with pose embeddings! </p><p><b>Acknowledgments</b><br /><em>Special thanks to Jiaping Zhao, Liang-Chieh Chen, Long Zhao (Rutgers University), Liangzhe Yuan, Yuxiao Wang, Florian Schroff, Hartwig Adam, and the Mobile Vision team for the wonderful collaboration and support.</em></p><div class="feedflare">
<a href="http://feeds.feedburner.com/~ff/blogspot/gJZg?a=3l_KQibU2Bw:DI8hFWQcDuk:yIl2AUoC8zA"><img border="0" src="http://feeds.feedburner.com/~ff/blogspot/gJZg?d=yIl2AUoC8zA" /></a>
</div><img alt="" height="1" src="http://feeds.feedburner.com/~r/blogspot/gJZg/~4/3l_KQibU2Bw" width="1" />

### [成为自己，姚安娜出道纪录片「破格公主」](https://app.vmovier.com/apiv3/post/view?postid=60975)

### [知乎十周年品牌短片「有问题就会有答案」](https://app.vmovier.com/apiv3/post/view?postid=60973)

### [超震撼气象延时「天象Sky-Lapse 2020」](https://app.vmovier.com/apiv3/post/view?postid=60971)

### [Insta360 年度回顾「Best of 2020」](https://app.vmovier.com/apiv3/post/view?postid=60960)

### [表情包也能出专辑「时髦的popo猫」](https://app.vmovier.com/apiv3/post/view?postid=60964)

### [泰国广告发话了「看电影请关机」](https://app.vmovier.com/apiv3/post/view?postid=60958)

### [旅拍博主的声音日记「我眼中的2020」](https://app.vmovier.com/apiv3/post/view?postid=60968)

### [创意视觉欺诈术「男巫2020合集」](https://app.vmovier.com/apiv3/post/view?postid=60934)

### [大众一镜到底创意广告「历史的车轮」](https://app.vmovier.com/apiv3/post/view?postid=60969)

### [中国自动驾驶发展报告2020（上）： 感知篇——浪潮已至](http://www.jintiankansha.me/t/2a24CornNi)

### error read: http://www.waerfa.com/feed

### error read: http://www.bigdatainterview.com/feed/

### [Word Ladders and Equivalence Classes](https://datagenetics.com/blog/january52021/index.html)

### [【A Brief History of Consumer Culture】网页链接 消费文化简史。在20世纪的整个过程中，资本主义通过将普通人塑造成对更多东西有不可抑制的渴望的消费者来保持...](https://weibo.com/1715118170/JDeeve5Ho)

### error read: http://www.jintiankansha.me/rss/GEYDCOBUPRRWGMDBGFSDIZTGMM2GCZRVMQZGGNRQHBRTQZLEME4TQYLFGJRDKZBTGI2TSZJUGM======

### [[CL]《Robustness Gym: Unifying the NLP Evaluation Landscape》K Goel, N Rajani, J Vig, S Tan, J Wu, S Zheng, C Xiong, M Bansal, C Ré [Stanford Univers...](https://weibo.com/1402400261/JDeum3Fum)

### [《今日学术视野(2021.1.15)》网页链接](https://weibo.com/1402400261/JDehlDxhy)

### [早！[太阳] #早安# [图片]](https://weibo.com/1402400261/JDegju5vw)

### [【I received first-ever donation on my open-source side project and it felt great】网页链接 我在开源方面的项目中获得了首次捐款，感觉很棒。开源地址托管...](https://weibo.com/1715118170/JDequr4dL)