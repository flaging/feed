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

# 2021-1-14

### [Python 中的面向接口编程](http://crossoverjie.top/2021/01/14/basic/python-oop/)

 <p><img alt="" src="https://tva1.sinaimg.cn/large/008eGmZEly1gmmkyd7lu6j31c00u0gx9.jpg" /></p>
<h1 id="前言"><a class="headerlink" href="https://crossoverjie.top/atom.xml#前言" title="前言"></a>前言</h1><p><code>”面向接口编程“</code>写 <code>Java</code> 的朋友耳朵已经可以听出干茧了吧，当然这个思想在 <code>Java</code> 中非常重要，甚至几乎所有的编程语言都需要，毕竟程序具有良好的扩展性、维护性谁都不能拒绝。</p>
<a id="more"></a>
<p>最近无意间看到了我刚开始写 <code>Python</code> 时的部分代码，当时实现的需求有个很明显的特点：</p>
<ul>
<li>不同对象具有公共的行为能力，但具体每个对象的实现方式又各不相同。</li>
</ul>
<p>说人话就是商户需要接入平台，接入的步骤相同，但具体实现不同。</p>
<p>作为一个”资深“ <code>Javaer</code>，需求还没看完我就洋洋洒洒的把各个实现类写好了：</p>
<p><img alt="" src="https://tva1.sinaimg.cn/large/008eGmZEly1gmmkyu72kgj30ho0bodgn.jpg" /></p>
<p>当然最终也顺利实现需求，甚至把组里一个没写过 <code>Java</code> 的大哥唬的一愣一愣的，直呼牛逼。</p>
<p><img alt="" src="https://tva1.sinaimg.cn/large/008eGmZEly1gmmkz0fp9mj301c01c742.jpg" /></p>
<p>不过事后也给我吐槽：</p>
<ul>
<li>你这设计是不错，但是感觉好复杂，跟代码时要找到真正的业务逻辑（实现类）得绕几圈。</li>
</ul>
<p>截止目前 <code>Python</code> 写多了，我总算是能总结他的感受：就是不够 <code>Pythonic</code>。</p>
<p>虽说 <code>Python</code> 没有类似 <code>Java</code> 这样的 <code>Interface</code> 特性，但作为面向对象的高级语言也是支持继承的；</p>
<p>在这里我们也可以利用继承的特性来实现面向接口编程：</p>
<figure class="highlight python"><table><tr><td class="gutter"><pre><div class="line">1</div><div class="line">2</div><div class="line">3</div><div class="line">4</div><div class="line">5</div><div class="line">6</div><div class="line">7</div><div class="line">8</div><div class="line">9</div><div class="line">10</div><div class="line">11</div><div class="line">12</div><div class="line">13</div><div class="line">14</div><div class="line">15</div><div class="line">16</div><div class="line">17</div><div class="line">18</div><div class="line">19</div><div class="line">20</div><div class="line">21</div><div class="line">22</div></pre></td><td class="code"><pre><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">Car</span>:</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(self)</span>:</span></div><div class="line">        <span class="keyword">pass</span></div><div class="line"></div><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">Benz</span><span class="params">(Car)</span>:</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(self)</span>:</span></div><div class="line">        print(<span class="string">"benz run"</span>)</div><div class="line"></div><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">BMW</span><span class="params">(Car)</span>:</span></div><div class="line"></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(self)</span>:</span></div><div class="line">        print(<span class="string">"bwm run"</span>)</div><div class="line"></div><div class="line"><span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(car)</span>:</span></div><div class="line">    car.run()</div><div class="line"></div><div class="line"><span class="keyword">if</span> __name__ == <span class="string">"__main__"</span>:</div><div class="line">    benz = Benz()</div><div class="line">    bmw = BMW()</div><div class="line"></div><div class="line">    run(benz)</div><div class="line">    run(bmw)</div></pre></td></tr></table></figure>
<p>代码非常简单，在 <code>Python</code> 中也没有类似于 <code>Java</code> 中的 <code>extends</code> 关键字，只需要在类声明末尾用括号包含基类即可。</p>
<p>这样在每个子类中就能单独实现业务逻辑，方便扩展和维护。</p>
<h1 id="类型检查"><a class="headerlink" href="https://crossoverjie.top/atom.xml#类型检查" title="类型检查"></a>类型检查</h1><p>由于 <code>Python</code> 作为一个动态类型语言，无法做到 <code>Java</code> 那样在编译期间校验一个类是否完全实现了某个接口的所有方法。</p>
<p>为此 <code>Python</code> 提供了解决办法，那就是 <code>abc(Abstract Base Classes)</code> ，当我们将基类用 <code>abc</code> 声明时就能近似做到：</p>
<figure class="highlight python"><table><tr><td class="gutter"><pre><div class="line">1</div><div class="line">2</div><div class="line">3</div><div class="line">4</div><div class="line">5</div><div class="line">6</div><div class="line">7</div><div class="line">8</div><div class="line">9</div><div class="line">10</div><div class="line">11</div><div class="line">12</div><div class="line">13</div><div class="line">14</div><div class="line">15</div><div class="line">16</div><div class="line">17</div><div class="line">18</div><div class="line">19</div><div class="line">20</div><div class="line">21</div><div class="line">22</div></pre></td><td class="code"><pre><div class="line"><span class="keyword">import</span> abc</div><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">Car</span><span class="params">(abc.ABC)</span>:</span></div><div class="line"><span class="meta">    @abc.abstractmethod</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(self)</span>:</span></div><div class="line">        <span class="keyword">pass</span></div><div class="line"></div><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">Benz</span><span class="params">(Car)</span>:</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(self)</span>:</span></div><div class="line">        print(<span class="string">"benz run"</span>)</div><div class="line"></div><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">BMW</span><span class="params">(Car)</span>:</span></div><div class="line">    <span class="keyword">pass</span></div><div class="line"></div><div class="line"><span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(car)</span>:</span></div><div class="line">    car.run()</div><div class="line"></div><div class="line"><span class="keyword">if</span> __name__ == <span class="string">"__main__"</span>:</div><div class="line">    benz = Benz()</div><div class="line">    bmw = BMW()</div><div class="line"></div><div class="line">    run(benz)</div><div class="line">    run(bmw)</div></pre></td></tr></table></figure>
<p>一旦有类没有实现方法时，运行期间便会抛出异常：</p>
<figure class="highlight python"><table><tr><td class="gutter"><pre><div class="line">1</div><div class="line">2</div></pre></td><td class="code"><pre><div class="line">bmw = BMW()</div><div class="line">TypeError: Can<span class="string">'t instantiate abstract class BMW with abstract methods run</span></div></pre></td></tr></table></figure>
<p>虽然无法做到在运行之前（毕竟不需要编译）进行校验，但有总比没有好。</p>
<h1 id="鸭子类型"><a class="headerlink" href="https://crossoverjie.top/atom.xml#鸭子类型" title="鸭子类型"></a>鸭子类型</h1><p>以上两种方式看似已经毕竟优雅的实现面向接口编程了，但实际上也不够 <code>Pythonic</code>。</p>
<p>在继续之前我们先聊聊<code>接口</code>的本质到底是什么？</p>
<p>在 <code>Java</code> 这类静态语言中面向接口编程是比较麻烦的，也就是我们常说的子类向父类转型，因此需要编写额外的代码。</p>
<p>带来的好处也是显而易见，只需要父类便可运行。</p>
<p>但我们也不必过于执着于接口，它本身只是一个协议、规范，并不特指 <code>Java</code> 中的 <code>Interface</code>，甚至有些语言压根没有这个关键字。</p>
<p>动态语言的特性也不需要强制校验是否实现了方法。</p>
<p>在 <code>Python</code> 中我们可以利用鸭子类型来优雅的实现面向接口编程。</p>
<p>在这之前先了解下鸭子类型，借用维基百科的说法：</p>
<ul>
<li>“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”</li>
</ul>
<p>我用大白话翻译下就是：</p>
<p>即便两个完全不想干的类，如果他们都实现了相同的方法，那就可以把他们当做同一类型的类来使用。</p>
<p>举个简单例子：</p>
<figure class="highlight python"><table><tr><td class="gutter"><pre><div class="line">1</div><div class="line">2</div><div class="line">3</div><div class="line">4</div><div class="line">5</div><div class="line">6</div><div class="line">7</div><div class="line">8</div><div class="line">9</div><div class="line">10</div><div class="line">11</div><div class="line">12</div><div class="line">13</div><div class="line">14</div><div class="line">15</div><div class="line">16</div></pre></td><td class="code"><pre><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">Order</span>:</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">create</span><span class="params">(self)</span>:</span></div><div class="line">        <span class="keyword">pass</span></div><div class="line"></div><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">User</span>:</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">create</span><span class="params">(self)</span>:</span></div><div class="line">        <span class="keyword">pass</span></div><div class="line"></div><div class="line"><span class="function"><span class="keyword">def</span> <span class="title">create</span><span class="params">(obj)</span>:</span></div><div class="line">    obj.create()</div><div class="line"></div><div class="line"><span class="keyword">if</span> __name__ == <span class="string">"__main__"</span>:</div><div class="line">    order = Order()</div><div class="line">    user = User()</div><div class="line">    create(order)</div><div class="line">    create(user)</div></pre></td></tr></table></figure>
<p>这里的 <code>order</code> 和 <code>user</code> 本身完全没有关系，只是他们都有相同方法，又得益于动态语言没法校验类型的特点，所以完全可以在运行的时候认为他们是同一种类型。</p>
<p>因此基于鸭子类型，之前的代码我们可以稍作简化：</p>
<figure class="highlight python"><table><tr><td class="gutter"><pre><div class="line">1</div><div class="line">2</div><div class="line">3</div><div class="line">4</div><div class="line">5</div><div class="line">6</div><div class="line">7</div><div class="line">8</div><div class="line">9</div><div class="line">10</div><div class="line">11</div><div class="line">12</div><div class="line">13</div><div class="line">14</div><div class="line">15</div><div class="line">16</div><div class="line">17</div><div class="line">18</div><div class="line">19</div><div class="line">20</div><div class="line">21</div></pre></td><td class="code"><pre><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">Car</span>:</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(self)</span>:</span></div><div class="line">        <span class="keyword">pass</span></div><div class="line"></div><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">Benz</span>:</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(self)</span>:</span></div><div class="line">        print(<span class="string">"benz run"</span>)</div><div class="line"></div><div class="line"><span class="class"><span class="keyword">class</span> <span class="title">BMW</span>:</span></div><div class="line">    <span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(self)</span>:</span></div><div class="line">        print(<span class="string">"bwm run"</span>)</div><div class="line"></div><div class="line"><span class="function"><span class="keyword">def</span> <span class="title">run</span><span class="params">(car)</span>:</span></div><div class="line">    car.run()</div><div class="line"></div><div class="line"><span class="keyword">if</span> __name__ == <span class="string">"__main__"</span>:</div><div class="line">    benz = Benz()</div><div class="line">    bmw = BMW()</div><div class="line"></div><div class="line">    run(benz)</div><div class="line">    run(bmw)</div></pre></td></tr></table></figure>
<p>因为在鸭子类型中我们在意的是它的行为，而不是他们的类型；所以完全可以不用继承便可以实现面向接口编程。</p>
<h1 id="总结"><a class="headerlink" href="https://crossoverjie.top/atom.xml#总结" title="总结"></a>总结</h1><p>我觉得平时没有接触过动态类型语言的朋友，在了解完这些之后会发现新大陆，就像是 <code>Python</code> 老手第一次使用 <code>Java</code> 时；虽然觉得语法啰嗦，但也会羡慕它的类型检查、参数验证这类特点。</p>
<p>动静语言之争这里不做讨论了，各有各的好，鞋好不好穿只有自己知道。</p>
<p>随便提一下其实不止动态语言具备鸭子类型，有些静态语言也能玩这个骚操作，感兴趣下次再介绍。</p>

### [2020年高校毕业生求职研究报告](http://mi.talkingdata.com/report-detail.html?id=990)

### error read: http://www.bigdatainterview.com/feed/

### [Cluedo](https://datagenetics.com/blog/january42021/index.html)

### [如果要给这轮牛市起个名字，我觉得是“改革牛”](http://www.jintiankansha.me/t/5nxgOccdbJ)

### [四螺旋DNA结构你听说过没有](http://jandan.net/p/108339)

### [关于结婚的话题：彩礼，婚房，和爱情](http://jandan.net/p/108345)

### [CIA关于UFO的完整档案已被解密](http://jandan.net/p/108344)

### [海中霸凌事件：会殴打鱼类的章鱼](http://jandan.net/p/108343)

### [输给了一阵狂风的欧洲最强战舰](http://jandan.net/p/108340)

### [通过编写一个简单的游戏学习 C 语言](https://linux.cn/article-13013-1.html?utm_source=rss&utm_medium=rss)

### [从 Linux 命令行进行打印](https://linux.cn/article-13012-1.html?utm_source=rss&utm_medium=rss)

### [【Rust日报】2021-01-13 -- Open Source Security, Inc.宣布为Rust的GCC前端提供资金](https://rustcc.cn/article?id=58a22139-4cdb-4141-a069-650b4fdc816a)

### [【Discovering and exploring mmap using Go】网页链接 使用Go发现和探索mmap。 网路冷眼技术分享 #科技暖心季# [图片]](https://weibo.com/1715118170/JD3eLqt4M)

### [【Department of Defense and Department of Commerce Explore 5G Challenge to Develop Open 5G Systems 】网页链接 美国🇺🇸国防部和商务部探索5G挑战以开...](https://weibo.com/1715118170/JD32e2tVw)

### [#绿洲摄影#中国.成都.武侯祠.红墙夹道 醉美红墙绿竹 绿洲 [图片]](https://weibo.com/1715118170/JD2ZHF5kF)

### [#绿洲摄影#腊梅花开 在南京明孝陵古墙的深红色背景下，金色的腊梅花盛开，呈现出一幅标志性的冬季画卷。 绿洲 [图片][图片][图片][图片]](https://weibo.com/1715118170/JD2SQvF35)

### [【What Silicon Valley gets about engineers that traditional companies do not】网页链接 硅谷对工程师的了解是传统公司所不具备的。网路冷眼技术分享 #科技...](https://weibo.com/1715118170/JD2QfaoOf)

### [【Understanding Image Contrast Algorithms】网页链接 了解图像对比度算法。 网路冷眼技术分享 #科技暖心季# [图片][图片][图片][图片][图片][图片][图片][图片...](https://weibo.com/1715118170/JD2DS2sdj)

### error read: http://www.waerfa.com/feed

### error read: http://www.bigdatainterview.com/feed/

### error read: http://www.bigdatainterview.com/feed/

### [【WhatsApp displays 404 not found when I send a link to Signal】网页链接 2021-01-10 at 22.50.34.png?dl=0 当我发送到Signal的链接时，WhatsApp显示404找不...](https://weibo.com/1715118170/JD4O833tb)

### error read: http://www.bigdatainterview.com/feed/

### error read: http://www.jintiankansha.me/rss/GEYDCOBUPRRWGMDBGFSDIZTGMM2GCZRVMQZGGNRQHBRTQZLEME4TQYLFGJRDKZBTGI2TSZJUGM======

### [[LG]《A Bayesian neural network predicts the dissolution of compact planetary systems》M Cranmer, D Tamayo, H Rein, P Battaglia, S Hadden, P J. Armita...](https://weibo.com/1402400261/JD50hgCcK)

### [《今日学术视野(2021.1.14)》网页链接](https://weibo.com/1402400261/JD4RcExeC)

### [早！[太阳] #早安# [图片]](https://weibo.com/1402400261/JD4Qz3Wpg)

### [【Theseus: A modern experimental OS written from scratch in Rust】网页链接 用Rust从头开始编写的现代实验操作系统Theseus。网路冷眼技术分享 #科技暖心季# ...](https://weibo.com/1715118170/JD4ZZxP6q)

### error read: http://www.jintiankansha.me/rss/GEYDCNRWPQ2TIZJWGJQTINLEMUYGGNRXMVRDSNZSG4ZDMNJQMU4WEMBZGAYTMMZQMEZGCMZZGE======

### [古文中的「無」「无」「亡」均表示「没有」之意，它们有何区别？](https://daily.zhihu.com/story/9732002)

### [西北有哪些不可错过的旅游美景？](https://daily.zhihu.com/story/9732000)

### [红黄代表暖，蓝绿代表冷，或许是一种错觉](https://daily.zhihu.com/story/9731990)

### [一岁半宝宝到底能不能看电视?](https://daily.zhihu.com/story/9731983)

### [同西方相比，亚洲有哪些健康有益的饮食习惯？](https://daily.zhihu.com/story/9731976)

### [瞎扯 · 如何正确地吐槽](https://daily.zhihu.com/story/9732005)

### [性能优化那些事](https://www.infoq.cn/article/miCvX1aTFrTx1NYFywPs)

### [网易严选流量体系建设实践](https://www.infoq.cn/article/VrJIq8xRjDPTQSHucgpK)

### [【Univariate Function Optimization in Python】网页链接 Python中的单变量函数优化。](https://weibo.com/1715118170/JD5ATvl4Z)

### [【Theranos destroyed crucial subpoenaed SQL blood test database, can't unlock backups, prosecutors say】网页链接 检察官说，Theranos破坏了传票的重要SQL...](https://weibo.com/1715118170/JD5oluBAc)

### [【Ecosia – A search engine that plants trees】网页链接 Ecosia – 一个种树的搜索引擎。网路冷眼技术分享 #科技暖心季# [图片]](https://weibo.com/1715118170/JD5cb57p7)

### error read: http://www.waerfa.com/feed

### error read: https://rsshub.app/gov/ndrc/xwdt

### [青年图摘0114！孤傲的大侠](https://qingniantuzhai.com/qing-nian-tu-zhai-0114-3/)

 <!--kg-card-begin: markdown--><img alt="青年图摘0114！孤傲的大侠" src="https://qingniantuzhai.com/content/images/2021/01/00893JKXly1gmlusmcmo2j30hs0ir76e_---.jpg" /><p>【1】这门神有点胖呀<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx3.sinaimg.cn/mw600/00893JKXly1gmm4i1u0irj30ly0ogti1.jpg" /></p>
<p>【2】说的好有道理<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmm3bpfe27j30go0hsabr.jpg" /></p>
<p>【3】没瑕疵<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmm2m5jmg6j30j60j60sz.jpg" /></p>
<p>【4】低配黄金甲<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmm2isv4jbj30f00k0taa.jpg" /></p>
<p>【5】这恐怕起来了也没力气<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx2.sinaimg.cn/mw600/007YR64mgy1gmm1lq16kaj31b20u0kjl.jpg" /></p>
<p>【6】生物书早就写过，嘴进鳃出<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx2.sinaimg.cn/mw600/00893JKXly1gmlzx6t1l1j30u00yktfv.jpg" /></p>
<p>【7】应该是到了很需要的时候了<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmlw35qc9vj30hs0igaax.jpg" /></p>
<p>【8】即使是无边的黑暗也埋没不了闪闪发亮的屁股<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmlvxzednmj30u00xq4ah.jpg" /></p>
<p>【9】没办法，兔子太不配合<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmlvlm3r4qj30fa0b1aad.jpg" /><br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx1.sinaimg.cn/mw600/00893JKXly1gmlvkrs3tnj30fa0nhq50.jpg" /></p>
<p>【10】嘴皮子利索的挣钱多<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmlvil9ikpj30c8079q38.jpg" /></p>
<p>【11】腹腔妊娠不是梦<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmlvjbmfjkj30u01fk7hr.jpg" /></p>
<p>【12】孤傲的大侠<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/00893JKXly1gmlusmcmo2j30hs0ir76e.jpg" /></p>
<p>【13】失败的电动尾门<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx2.sinaimg.cn/mw1024/00893JKXly1gmls9jl7b8g30dd0abhe0.gif" /></p>
<p>【14】侮辱性极强<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx2.sinaimg.cn/mw1024/00893JKXly1gmluonxkidg30k00ia7wp.gif" /></p>
<p>【15】擦了擦切肉的刀<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx2.sinaimg.cn/mw600/00893JKXly1gmlu9uzf9bj30c80fiwf8.jpg" /><br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx1.sinaimg.cn/mw600/00893JKXly1gmlu9llhhjj30c80cbdgf.jpg" /></p>
<p>【16】真.门面房<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://ww1.sinaimg.cn/mw600/00745YaMgy1gmlswsznr8j30go0m6jti.jpg" /></p>
<p>【17】出污泥而不染濯清涟而不妖<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://ww1.sinaimg.cn/mw600/00745YaMgy1gmlswsyh2zj30kk0plwfv.jpg" /></p>
<p>【18】给您劈个叉吧<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx2.sinaimg.cn/mw1024/00893JKXly1gmm5u82mz6g30hs0c01ky.gif" /></p>
<p>【19】一开始以为眼花了，后来发现真的眼花<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx4.sinaimg.cn/mw600/0081ffzKly1gmlrsfv6n9j338o4jcqv8.jpg" /></p>
<p>【20】冰雪奇圆<br />
<img alt="青年图摘0114！孤傲的大侠" src="https://wx3.sinaimg.cn/mw600/005Fip1Jly1gmlnnqauu7j30u010aaco.jpg" /></p>
<!--kg-card-end: markdown-->

### [GitHub 上一个开源编程语言自制教程，作者 @karminski-牙医 将基于 Go 语言，教你用 450 行代码自制编程语言。GitHub：网页链接 [图片][图片][图片]](https://weibo.com/5722964389/JD5YRyc7D)

### [Daily Hacker News for 2021-01-13](https://www.daemonology.net/hn-daily/2021-01-13.html)

### [2021年值得CTO期待的十大Web开发趋势](https://www.infoq.cn/article/bmHglmGu5Hw0Z6MH5ETd)

### [运维数智化时代——京东数科AIOps落地实践（一）](https://www.infoq.cn/article/bFMX2Y4NpAKIZf7i2DVz)

### error read: http://segmentfault.com/feeds/blogs

### [【Does refactoring Legacy Code pay off in your career?】网页链接 重构遗留代码对你的职业生涯中有回报吗？ [图片]](https://weibo.com/1715118170/JD5ZkxTzE)

### [【Google Sued by YouTube Rival Rumble over Search Rankings】网页链接 谷歌因搜索排名问题被YouTube的竞争对手Rumble起诉。视频共享网站Rumble引用《华尔街日...](https://weibo.com/1715118170/JD5MHtB2C)

### [转发微博 - 转发 @网路冷眼:&ensp;#冷眼赠书福利# 转发赠书# 网路冷眼联合@华章图书 @华章计算机科学 送出 5 本《ECharts数据可视化》，截至 1 月 20 日，转发此...](https://weibo.com/1715118170/JD5GCbkyX)

### [派早报：英伟达推出 RTX 3060 显卡、Anker 发布声阔 Liberty Air 2 Pro 耳机等](https://sspai.com/post/64558)

### error read: http://120.53.237.72:1200/zhihu/zhuanlan/paperweekly

### [[HIRING, still....\ HPC/Cluster Management Support, but definitely not reading from a script!](https://www.reddit.com/r/HPC/comments/kwu4h0/hiring_still_hpccluster_management_support_but/)

 <!-- SC_OFF --><div class="md"><p><a href="http://www.brightcomputing.com/">Bright Computing</a> (the industry leader in commercial cluster management solutions (ie, supercomputers)) is hiring two System Engineer positions, <a href="https://www.brightcomputing.com/jobs/system-engineer">one in Amsterdam</a>, and <a href="https://www.brightcomputing.com/jobs/system-engineer-0">one (anywhere) in the US</a>.</p> <p>The position has three primary components:</p> <ol> <li>Responding to requests for support. We are not offering phone-based support at this time, everything is done through email/JIRA. Screen sharing sessions are most often handled by senior staff and are scheduled well in advance.</li> <li>Performing deployments of our software. We are a software company, so we prefer that <a href="https://www.brightcomputing.com/partners">our partners</a> perform the majority of our deployments. However, there are some installations where it makes sense to have a deployment performed by an in-house resource.</li> <li>R&amp;D tasks/documentation. &quot;Is it possible to incorporate XYZ into our product?&quot; or &quot;Can we pull information/statistics from ABC FPGA board?&quot;</li> </ol> <p>The team currently has three people in Amsterdam, five in the US, and one each in Australia and New Zealand. This spread allows us to provide support from Monday morning 9am Australian Central time (11:30pm Sunday UTC) until Friday evening 5pm Pacific time (1am Saturday UTC). Your normal shift will be +/- &quot;normal&quot; M-F working hours for where you live--no shift work and no on-call rotation.</p> <p>The &quot;support&quot; moniker sometimes turns people off, as they envision a call center type arrangement---a person sitting in a cube reading from a script telling people to reboot.........that is not what this position is about. The issues we receive are often unique and/or specific to a customer, and the systems are most often large high-end and/or large HPC clusters. An average week is anywhere between 90 to 130 new issues filed, mostly evenly divided within the team.</p> <p>At the same time, we're not &quot;system admins&quot; either, we don't do managed services--the customer is the onsite system admin responsible for day-to-day operations. Our focus is on helping high-level customers with our software. Our team is not responsible for sales or marketing. We don't do on-call rotations, there's no shift-work, and has a team lead (me) who's pretty hands-off (but pretty much always available.)</p> <p>The <a href="https://www.brightcomputing.com/support">scope of support coverage</a> is pretty clearly laid out, although we often do go above and beyond to be as helpful as possible.</p> <p>The job in the US is 100% remote, and the position in the Amsterdam office is obviously remote for the foreseeable future.</p> <p>You can apply via the links provided in <a href="https://www.brightcomputing.com/jobs/support-engineer-0">the US Job Posting</a> or <a href="https://www.brightcomputing.com/jobs/support-engineer">the Dutch Job Posting</a>. Both of those links have more details about the position, but I'm available to answer questions.</p> <p>Salaries vary <strong>greatly</strong> on experience and skillsets, but a reasonable/average starting point for a discussion would be in the $90K range in the US and €5k/mo for the job here in NL.</p> </div><!-- SC_ON --> &#32; submitted by &#32; <a href="https://www.reddit.com/user/kenwoodsbright"> /u/kenwoodsbright </a> <br /> <span><a href="https://www.reddit.com/r/HPC/comments/kwu4h0/hiring_still_hpccluster_management_support_but/">[link]</a></span> &#32; <span><a href="https://www.reddit.com/r/HPC/comments/kwu4h0/hiring_still_hpccluster_management_support_but/">[comments]</a></span>

### [迫于炒股，现在怎么办理香港银行卡?](https://www.v2ex.com/t/744435)

### [【未通过】海南金盘智能科技股份有限公司](http://kcb.sse.com.cn//renewal/xmxq/index.shtml?auditId=433)

### [【未通过】青岛海泰新光科技股份有限公司](http://kcb.sse.com.cn//renewal/xmxq/index.shtml?auditId=413)

### [【未通过】成都纵横自动化技术股份有限公司](http://kcb.sse.com.cn//renewal/xmxq/index.shtml?auditId=403)

### [【未通过】株洲华锐精密工具股份有限公司](http://kcb.sse.com.cn//renewal/xmxq/index.shtml?auditId=586)

### [Gartner 报告最新解读：数仓 or 数据湖？](https://www.infoq.cn/article/qOeKIhCmeVN3QYwcS0b5)

### [如何利用TensorFlow Hub 让BERT开发更简单？](https://www.infoq.cn/article/wBgwjg65QEp7GcwJHoIG)

### [聊聊微服务的通信模式](https://www.infoq.cn/article/SVZcTxqSI9KDtNz1gCd3)

### [16 岁高中生成功将 Linux 移植到 iPhone，并贴出详细指南](https://www.infoq.cn/article/DMMXsxG1O1Bf76u40l7v)

### [Python太慢了吗？](https://www.infoq.cn/article/XC09ISxtCQJR3Asbc9OO)

### [【How to Identify Malicious Bots on your Network】网页链接 如何识别网络上的恶意机器人？](https://weibo.com/1715118170/JD6LLi6Gl)

### [【Free Fullstack Development Foundation Program】网页链接# 免费的全栈开发基础计划。该计划提供了对全栈编程和Web应用程序开发中的中级概念的清晰理解。#科...](https://weibo.com/1715118170/JD6Ly0rP8)

### [【How to keep your Git history clean with interactive rebase】网页链接 如何通过交互式 rebase来保持Git历史记录的清洁？](https://weibo.com/1715118170/JD6nsjKXr)

### [Energy Bar –  在屏幕顶部以能量条的方式显示手机电量[Android]](https://www.appinn.com/energy-bar-for-android/)

 <p><strong>Energy Bar</strong> 是一款可以在 Android 屏幕顶部，以能量条的方式显示手机电量的应用，可自定义颜色、位置、宽度等参数。@<a class="rank-math-link" href="https://www.appinn.com/energy-bar-for-android/">Appinn</a></p>



<div class="wp-block-image"><figure class="aligncenter size-large"><img alt="Energy Bar -  在屏幕顶部以能量条的方式显示手机电量[Android]" src="https://img3.appinn.net/images/202101/energy-bar.jpg!o" title="Energy Bar -  在屏幕顶部以能量条的方式显示手机电量[Android] 1" /></figure></div>



<p>Energy Bar 与<a class="rank-math-link" href="https://www.appinn.com/access-dots-for-android/">Access Dots – 实时提醒，有应用正在用你的摄像头和麦克风[Android]</a> 是同一个开发者。</p>



<h2>Energy Bar</h2>



<p>这可能是一款为用户增加续航焦虑的应用，至于实际用途，就看每个人的情况吧，反正也不一定有实际用途，主要为了好看？</p>



<p>先来看视频：</p>



<div class="aspect-ratio">
 
</div>



<p>Energy Bar 可以设置电量条的位置、宽度、背景透明、左右，以及颜色、样式：</p>



<div class="wp-block-columns">
<div class="wp-block-column">
<figure class="wp-block-image size-large"><img alt="Energy Bar -  在屏幕顶部以能量条的方式显示手机电量[Android] 1" src="https://img3.appinn.net/images/202101/photo_2021-01-14_10-58-26.jpg!o" title="Energy Bar -  在屏幕顶部以能量条的方式显示手机电量[Android] 2" /></figure>
</div>



<div class="wp-block-column">
<figure class="wp-block-image size-large is-resized"><img alt="Energy Bar -  在屏幕顶部以能量条的方式显示手机电量[Android] 2" height="533" src="https://img3.appinn.net/images/202101/photo_2021-01-14_10-58-24.jpg!o" title="Energy Bar -  在屏幕顶部以能量条的方式显示手机电量[Android] 3" width="274" /></figure>
</div>
</div>



<p>青小蛙觉得这个细条条用处不大啊，就应该搞一个超大超粗超彩，看着才霸气。</p>



<p>可以在 <a class="rank-math-link" href="https://play.google.com/store/apps/details?id=you.in.spark.energy" rel="noopener" target="_blank">Google Play</a> 免费安装，无法安装的同学点击下面的按钮前往搬运网盘下载：</p>



<div align="center"><a href="https://d.appinn.com/energy-bar-for-android/" rel="noopener" target="view_window"><img alt="Energy Bar -  在屏幕顶部以能量条的方式显示手机电量[Android] 3" src="https://img3.appinn.net/images/201507/down.png" title="Energy Bar -  在屏幕顶部以能量条的方式显示手机电量[Android] 4" /></a></div>



<p>注意有几种配色需要付费解锁使用。</p>
<hr /><h2>相关阅读</h2><ul><li><a href="https://www.appinn.com/hidden-bar-for-macos/" rel="bookmark" title="Permanent Link: Hidden Bar &#8211; 隐藏 macOS 菜单栏不常用的应用图标，替代 Bartender 3">Hidden Bar &#8211; 隐藏 macOS 菜单栏不常用的应用图标，替代 Bartender 3</a></li><li><a href="https://www.appinn.com/qt-address-bar/" rel="bookmark" title="Permanent Link: QT Address Bar &#8211; 窗口地址栏增强工具">QT Address Bar &#8211; 窗口地址栏增强工具</a></li><li><a href="https://www.appinn.com/vu-bar/" rel="bookmark" title="Permanent Link: Vu-Bar &#8211; 有利于阅读的文字挡板工具">Vu-Bar &#8211; 有利于阅读的文字挡板工具</a></li><li><a href="https://www.appinn.com/notch-battery-bar-for-android/" rel="bookmark" title="Permanent Link: 显示电池剩余电量，刘海屏还能这样用？[Android]">显示电池剩余电量，刘海屏还能这样用？[Android]</a></li><li><a href="https://www.appinn.com/bar-chart-race-generator/" rel="bookmark" title="Permanent Link: Bar chart race generator &#8211; 0 门槛，在线生成条形竞赛图动画">Bar chart race generator &#8211; 0 门槛，在线生成条形竞赛图动画</a></li></ul><hr />
<a href="http://www.appinn.com/copyright/?utm_source=feeds&amp;utm_medium=copyright&amp;utm_campaign=feeds" title="版权声明">&#169;</a>2019 青小蛙 for <a href="http://www.appinn.com/?utm_source=feeds&amp;utm_medium=appinn&amp;utm_campaign=feeds" title="本文来自小众软件">小众软件</a> | <a href="http://www.appinn.com/join-us/?utm_source=feeds&amp;utm_medium=joinus&amp;utm_campaign=feeds" title="加入小众软件">加入我们</a> | <a href="https://meta.appinn.com/c/faxian/?utm_source=feeds&amp;utm_medium=contribute&amp;utm_campaign=feeds" rel="noopener" target="_blank" title="给小众软件投稿">投稿</a> | <a href="http://www.appinn.com/feeds-subscribe/?utm_source=feeds&amp;utm_medium=feedsubscribe&amp;utm_campaign=feeds" target="_blank" title="可以分类订阅小众，Windows/MAC/游戏"><font color="red">订阅指南</font></a><br /> 3659b075e72a5b7b1b87ea74aa7932ff <br />
<a href="https://www.appinn.com/energy-bar-for-android/#comments" title="to the comments">点击这里留言、和原作者一起评论</a>

### error read: http://120.53.237.72:1200/zhihu/zhuanlan/paperweekly

### error read: http://www.bigdatainterview.com/feed/

### [拜登政府有机会扭转美国不平等加剧趋势](http://www.ftchinese.com/story/001090950)

### [擅自研发可随意展示红码绿码 APP，一男子被杭州警方抓获](https://www.v2ex.com/t/744751)

### [吐槽： Apple 手机壳是消耗品吗？](https://www.v2ex.com/t/744608)

### [1月14日新闻茶泡Fan](https://www.cfan.com.cn/2021/0114/134755.shtml)

### [黑客以 60 万美元出售 Windows 10 源代码](https://linux.cn/article-13014-1.html?utm_source=rss&utm_medium=rss)

### [Rust 入门学习路线](https://rustcc.cn/article?id=a6118e2e-4bd1-4e77-ae73-33bfed1842e1)

### [配置语言的黄金时代](https://www.infoq.cn/article/AXQrTwNtDSwS0NMxwB5M)

### [从大型活动备战准备到资源调度，从服务器、存储、网络到数据库、监控和运维，从研发效能度量到 AI 技术加持，京东智联云作为京东的技术基石发挥了哪些作用？点击...](https://weibo.com/1746173800/JD79WAsPF)

### [《猫、爱因斯坦和密码学：我也能看懂的量子通信》明日开奖，欢迎参与～ - 转发 @爱可可-爱生活:&ensp;#抽奖##赠书#活动汇总，参与请转发原微博：《猫、爱因斯坦...](https://weibo.com/1402400261/JD6QvmhJF)

### [如何用 QNAP NAS 搭建属于自己的云端书库？](https://sspai.com/post/64484)

### [ACM Fellow 名单重磅发布！12 位华人学者入选](https://segmentfault.com/a/1190000038978868)

### [苹果团十周年！原封 iPhone 12 澳门版（带小票，直营店保）、港行，下单减 100，激活 24 小时无理由退换，绿屏可换。国行 M1 MacBook Pro / Mac Mini 16G 内存定...](https://www.v2ex.com/t/744798)

### [有结扎过的老哥吗？](https://www.v2ex.com/t/744763)

### [MacBook Pro M1 真香](https://www.v2ex.com/t/744579)

### error read: https://rsshub.app/telegram/channel/wxfanfou

### [快手AI技术对游戏的全链路赋能](https://www.infoq.cn/article/pIaQYU0KZGTDBIel1uKH)

### [400万Docker镜像中，51%的镜像存在高危漏洞](https://www.infoq.cn/article/DZTt1g4rvzlQ7f5OhiNC)

### [Shopify如何在浏览器之外使用WebAssembly？](https://www.infoq.cn/article/xBWeq2eclVFf0WcytYVs)

### [开源问题系列探讨：许可证的核心诉求是什么？](https://www.infoq.cn/article/48bOExBvoPvix7RCTka1)

### [【Trankit：基于Transformer的轻量多语言自然语言处理工具包】’trankit - Trankit is a Light-Weight Transformer-based Python Toolkit for Multilingual Natu...](https://weibo.com/1402400261/JD7BtqHOM)

### [【iMove：逻辑可复用、面向函数的流程可视化JavaScript工具库】'iMove - Move your mouse, generate code from flow chart' by imgcook GitHub: 网页链接 #开源#...](https://weibo.com/1402400261/JD7DF1pya)

### [【Stanford pulls plug on the return of freshmen and sophomores to campus】网页链接 斯坦福大学阻止大一和大二学生返回校园。](https://weibo.com/1715118170/JD7WHd48Y)

### [【Runtime improvement for Minimum Cut algorithm first time in 25 years】网页链接 25年以来首次实现最小切割算法的运行时改进。PDF格式下载地址：网页链接 [...](https://weibo.com/1715118170/JD7yigMFP)

### error read: http://www.waerfa.com/feed

### error read: http://120.53.237.72:1200/zhihu/zhuanlan/paperweekly

### error read: http://www.bigdatainterview.com/feed/

### [Comic for 2021.01.13](http://www.explosm.net/comics/5767/)

### [熬不住了，想辞职了…](https://www.v2ex.com/t/744757)

### [迫于闲的蛋疼，问一下各位买了智能手表的感觉这东西值不值得买](https://www.v2ex.com/t/744609)

### [女朋友公司开始强制 996，该怎么办？](https://www.v2ex.com/t/744589)

### [弹劾是如何运作的？](http://jandan.net/p/108348)

### [美团配送实时特征平台建设实践](https://www.infoq.cn/article/40uuWNy38rbVSf3Wm3my)

### [英特尔急了：没落的芯片之王迫切需要一位技术型CEO](https://www.infoq.cn/article/7dhLFp8ITG7OGSqcMgZo)

### [【Log Pattern Recognition: LogMine】网页链接 日志模式识别：LogMine。 [图片]](https://weibo.com/1715118170/JD8l16SUw)

### [早十几年前，淘宝靠着本土化的运营更懂中国人，打败了进场的ebay。十几年过去后，淘宝意图在东南亚电商市场上重新把淘宝复制一遍赢得市场，被shoppe用同样的方式...](https://weibo.com/1642628345/JD8jHxjiX)

### [开始自救？英特尔宣布CEO变更，请回前CTO Pat Gelsinger](https://www.jiqizhixin.com/articles/2021-01-14-3)

 

### [规划2021年技术路标，百度研究院做出了这样一份预测](https://www.jiqizhixin.com/articles/2021-01-14-2)

 

### [7位图灵奖得主当选，新晋陈怡然、周昆、颜水成等多位华人，2020 ACM Fellow名单公布](https://www.jiqizhixin.com/articles/2021-01-14)

 

### error read: http://www.waerfa.com/feed

### error read: https://www.codesky.me/feed/

### [rust新手的一个问题：fold和scan。](https://rustcc.cn/article?id=2f4b3a15-7874-4c68-b9d8-5a717e9a3af0)

### [Worktile 王涛的经营之道：7 年牵引式破局 ｜ TGO 科技领袖三十人](https://www.infoq.cn/article/vzl2g0HOT1pQtU5iWWBj)

### [微软和谷歌的 AI 模型在 SuperGLUE 语言基准上超越了人类的表现](https://www.infoq.cn/article/eFpHezZKRZKUbBUe9DxX)

### [2021年，算法还“香”吗？ | InfoQ大咖说](https://www.infoq.cn/article/vkxBDLsdiwI0iSFdbIrq)

### [前端大数据可视化从入门到实战](https://segmentfault.com/a/1190000038980319)

### [【Foam: A personal knowledge management and sharing system for VSCode】网页链接 #科技暖心季# [图片][图片]](https://weibo.com/1715118170/JD8Eb2TtZ)

### [熵增定律确实是最让人沮丧的定律，再牛逼的系统运行久了也会混乱无序，无可奈何。 - 转发 @玩家老C:&ensp;早十几年前，淘宝靠着本土化的运营更懂中国人，打败了...](https://weibo.com/1642628345/JD8qXCE8D)

### [告别繁琐的记账步骤，专为「懒人」打造的记账工具：多少资产](https://sspai.com/post/64506)

### error read: http://www.waerfa.com/feed

### error read: https://www.codesky.me/feed/

### [尽调过200家私募机构后，我是这样挑选基金的...](http://www.jintiankansha.me/t/OpOJ0Kd8Kx)

### [白酒崩！军工崩！汽车崩！但这两个板块却逆市大涨...前期高位股是假摔还是真瓦解？新的抱团方向出现了？](http://www.jintiankansha.me/t/ivw4kShJHd)

### [永远不要低估银行的价值](http://www.jintiankansha.me/t/UAsP424fP3)

### [冰火两重天的2020年，我的成长和反思](http://www.jintiankansha.me/t/hDAdc4jxR1)

### [疫苗多久产生抗体？有慢性病能不能打？你关心的答案来了](https://m.21jingji.com/article/20210114/herald/a133a4c0f36a92f9062c499ee04d3fc4.html)

### [1、《工业互联网创新发展行动计划（2021—2023年）》发布2、2020年社会融资规模增量为34.86万亿元3、特朗普弹劾案过关华盛顿气氛紧张4、美国约翰霍普金斯大学：...](https://t.me/tgchinanews/920)

### [Thu, 14 Jan 2021 07:19:01 GMT](https://t.me/tgchinanews/919)

### [Intel 正在死去，大家怎么看呢？](https://www.v2ex.com/t/744868)

### [要想财富自由，投资自己的最好方法有哪些呢？](https://www.v2ex.com/t/744831)

### error read: https://rsshub.app/telegram/channel/wxfanfou

### error read: http://www.waerfa.com/feed

### error read: https://rsshub.app/xmind/mindmap