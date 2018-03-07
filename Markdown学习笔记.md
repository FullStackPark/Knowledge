# MarkDown 语法说明
* [概述](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E6%A6%82%E8%BF%B0)
    * [宗旨](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%AE%97%E6%97%A8)
    * [兼容](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%85%BC%E5%AE%B9html)
    * [特殊字符自动转换](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E7%89%B9%E6%AE%8A%E5%AD%97%E7%AC%A6%E8%87%AA%E5%8A%A8%E8%BD%AC%E6%8D%A2)
* [区块元素](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%8C%BA%E5%9D%97%E5%85%83%E7%B4%A0)
    * [段落和换行](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E6%AE%B5%E8%90%BD%E5%92%8C%E6%8D%A2%E8%A1%8C)
    * [标题](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E6%A0%87%E9%A2%98)
    * [区块引用](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%8C%BA%E5%9D%97%E5%BC%95%E7%94%A8blockquotes)
    * [列表](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%88%97%E8%A1%A8)
    * [代码区块](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E4%BB%A3%E7%A0%81%E5%8C%BA%E5%9D%97)
    * [分割线](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%88%86%E5%89%B2%E7%BA%BF)
* [区段元素](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%8C%BA%E6%AE%B5%E5%85%83%E7%B4%A0)
    * [链接](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E9%93%BE%E6%8E%A5)
    * [强调](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%BC%BA%E8%B0%83)
    * [代码](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E4%BB%A3%E7%A0%81)
    * [图片](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%9B%BE%E7%89%87)
* [其他](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%85%B6%E4%BB%96)
    * [反斜杠](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E8%87%AA%E5%8A%A8%E8%BF%9E%E6%8E%A5)
    * [自动连接](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E5%8F%8D%E6%96%9C%E6%9D%A0)
* [总结](https://github.com/FullStackPark/Knowledge/blob/master/Markdown%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md#%E6%80%BB%E7%BB%93)
****************
本文借鉴与:[Markdown 语法说明](http://wowubuntu.com/markdown/#link)
______________________________________
## 概述
### 宗旨
>**Markdown 的目标是实现「易读易写」.**
>
>**可读性，无论如何，都是最重要的。一份使用 Markdown 格式撰写的文件应该可以直接以纯文本发布，并且看起来不会像是由许多标签或是格式指令所构成。Markdown 语法受到一些既有 text-to-HTML 格式的影响，包括 Setext、atx、Textile、reStructuredText、Grutatext 和 EtText，而最大灵感来源其实是纯文本电子邮件的格式**
>
>总之， Markdown 的语法全由一些符号所组成，这些符号经过精挑细选，其作用一目了然。比如：在文字两旁加上星号，看起来就像*强调*。Markdown 的列表看起来，嗯，就是列表。Markdown 的区块引用看起来就真的像是引用一段文字，就像你曾在电子邮件中见过的那样。

### 兼容HTML

**Markdown 语法的目标是：成为一种适用于网络的书写语言。**

**Markdown 不是想要取代 HTML，甚至也没有要和它相近，它的语法种类很少，只对应 HTML 标记的一小部分。Markdown 的构想不是要使得 HTML 文档更容易书写。在我看来， HTML 已经很容易写了。Markdown 的理念是，能让文档更容易读、写和随意改。HTML 是一种发布的格式，Markdown 是一种书写的格式。就这样，Markdown 的格式语法只涵盖纯文本可以涵盖的范围。**

**不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。不需要额外标注这是 HTML 或是 Markdown；只要直接加标签就可以了。**

**要制约的只有一些 HTML 区块元素――比如 \<div>、\<table>、\<pre>、\<p> 等标签，必须在前后加上空行与其它内容区隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。Markdown 的生成器有足够智能，不会在 HTML 区块标签外加上不必要的 \<p> 标签。**

**例子如下，在 Markdown 文件里加上一段 HTML 表格:**

这是一个普通段落。

\<table>

    <tr>
        <td>Foo\</td>
    </tr>
\</table>

这是另一个普通段落。

**请注意，在 HTML 区块标签间的 Markdown 格式语法将不会被处理。比如，你在 HTML 区块内使用 Markdown 样式的 \*强调\* 会没有效果。**

**HTML 的区段（行内）标签如 \<span>、\<cite>、\<del> 可以在 Markdown 的段落、列表或是标题里随意使用。依照个人习惯，甚至可以不用 Markdown 格式，而直接采用 HTML 标签来格式化。举例说明：如果比较喜欢 HTML 的 \<a> 或 \<img> 标签，可以直接使用这些标签，而不用 Markdown 提供的链接或是图像标签语法**

**和处在 HTML 区块标签间不同，Markdown 语法在 HTML 区段标签间是有效的。**

### 特殊字符自动转换

**在 HTML 文件中，有两个字符需要特殊处理： < 和 & 。 < 符号用于起始标签，& 符号则用于标记 HTML 实体，如果你只是想要显示这些字符的原型，你必须要使用实体的形式，像是 \&lt; 和 \&amp;。**

**& 字符尤其让网络文档编写者受折磨，如果你要打「AT&T」 ，你必须要写成「AT&amp;T」。而网址中的 & 字符也要转换。比如你要链接到：**

http://images.google.com/images?num=30&q=larry+bird

**你必须要把网址转换写为：**

http://images.google.com/images?num=30\&amp;q=larry+bird

**才能放到链接标签的 href 属性里。不用说也知道这很容易忽略，这也可能是 HTML 标准检验所检查到的错误中，数量最多的。**

**Markdown 让你可以自然地书写字符，需要转换的由它来处理好了。如果你使用的 & 字符是 HTML 字符实体的一部分，它会保留原状，否则它会被转换成 \&amp;。**

**所以你如果要在文档插入一个版权号©,你也可以这样写:**\&copy;

**Markdown 保留它不动.而你若写:** AT&T

**Markdown 就会将它转为:** AT\&amp;T

**类似的状况也会发生在 < 符号上，因为 Markdown 允许 兼容 HTML ，如果你是把 < 符号作为 HTML 标签的定界符使用，那 Markdown 也不会对它做任何转换，但是如果你写：** 4 < 5

**Markdown 将会把它转换为：** 4 \&lt; 5

**不过需要注意的是，code 范围内，不论是行内还是区块， < 和 & 两个符号都一定会被转换成 HTML 实体，这项特性让你可以很容易地用 Markdown 写 HTML code （和 HTML 相对而言， HTML 语法中，你要把所有的 < 和 & 都转换为 HTML 实体，才能在 HTML 文件里面写出 HTML code。）**
## 区块元素
### 段落和换行
**一个 Markdown 段落是由一个或多个连续的文本行组成，它的前后要有一个以上的空行（空行的定义是显示上看起来像是空的，便会被视为空行。比方说，若某一行只包含空格和制表符，则该行也会被视为空行）。普通段落不该用空格或制表符来缩进。**

**「由一个或多个连续的文本行组成」这句话其实暗示了 Markdown 允许段落内的强迫换行（插入换行符），这个特性和其他大部分的 text-to-HTML 格式不一样（包括 Movable Type 的「Convert Line Breaks」选项），其它的格式会把每个换行符都转成 \<br /> 标签。**

**如果你确实想要依赖 Markdown 来插入 \<br /> 标签的话，在插入处先按入两个以上的空格然后回车**。
### 标题

**Markdown 支持两种标题的语法，类 Setext 和类 atx 形式。**

**类 Setext 形式是用底线的形式，利用 = （最高阶标题）和 - （第二阶标题），例如：**

This is an H1

\=========

This is an H2

\---------------

**任何数量的 = 和 - 都可以有效果。**

**类 Atx 形式则是在行首插入 1 到 6 个 # ，对应到标题 1 到 6 阶，例如：**

\# 这是 H1
\## 这是 H2

**你可以选择性地「闭合」类 atx 样式的标题，这纯粹只是美观用的，若是觉得这样看起来比较舒适，你就可以在行尾加上 #，而行尾的 # 数量也不用和开头一样（行首的井字符数量决定标题的阶数）：**

\# 这是 H1 \# <br>
\## 这是 H2 \## <br>
\### 这是 H3 \### <br>
### <span id=2.3>区块引用Blockquotes</span>
**Markdown 标记区块引用是使用类似 email 中用 > 的引用方式。如果你还熟悉在 email 信件中的引言部分，你就知道怎么在 Markdown 文件中建立一个区块引用，那会看起来像是你自己先断好行，然后在每行的最前面加上 > ：**<br>
\> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,<br>
\> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.<br>
\> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.<br>
\> <br>
\> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse<br>
\> id sem consectetuer libero luctus adipiscing.<br>

**Markdown 也允许你偷懒只在整个段落的第一行最前面加上 > ：**<br>
\> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

\> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.<br>
**区块引用可以嵌套（例如：引用内的引用），只要根据层次加上不同数量的 > ：**<br>
\> This is the first level of quoting.<br>
\><br>
\> \> This is nested blockquote.<br>
\><br>
\> Back to the first level.<br>

**引用的区块内也可以使用其他的 Markdown 语法，包括标题、列表、代码区块等：**<br>

```
\> ## 这是一个标题。<br>
\> <br>
\> 1.   这是第一行列表项。<br>
\> 2.   这是第二行列表项。<br>
\> <br>
\> 给出一些例子代码：<br>
\> <br>
\>     return shell_exec("echo $input | $markdown_script");<br>
```

**任何像样的文本编辑器都能轻松地建立 email 型的引用。例如在 BBEdit 中，你可以选取文字后然后从选单中选择增加引用阶层。**

### 列表

**Markdown 支持有序列表和无序列表。**

**无序列表使用星号、加号或是减号作为列表标记：**<br>
\*   Red<br>
\*   Green<br>
\*   Blue<br>

**等同于：**<br>
\+   Red<br>
\+   Green<br>
\+   Blue<br>

**也等同于:**<br>
\-   Red<br>
\-   Green<br>
\-   Blue<br>

**有序列表则使用数字接着一个英文句点：**<br>
\1.  Bird<br>
\2.  McHale<br>
\3.  Parish<br>

**很重要的一点是，你在列表标记上使用的数字并不会影响输出的 HTML 结果，上面的列表所产生的 HTML 标记为：**<br>
\<ol><br>
\<li>Bird\</li><br>
\<li>McHale\</li><br>
\<li>Parish\</li><br>
\</ol><br>

**如果你的列表标记写成：**<br>
\1.  Bird<br>
\1.  McHale<br>
\1.  Parish<br>

**或甚至是：**<br>
\3. Bird<br>
\1. McHale<br>
\8. Parish<br>
**你都会得到完全相同的 HTML 输出。重点在于，你可以让 Markdown 文件的列表数字和输出的结果相同，或是你懒一点，你可以完全不用在意数字的正确性。**<br>

**如果你使用懒惰的写法，建议第一个项目最好还是从 1. 开始，因为 Markdown 未来可能会支持有序列表的 start 属性。**

**列表项目标记通常是放在最左边，但是其实也可以缩进，最多 3 个空格，项目标记后面则一定要接着至少一个空格或制表符。**

**要让列表看起来更漂亮，你可以把内容用固定的缩进整理好：**

\*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.<br>
     Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,<br>
     viverra nec, fringilla in, laoreet vitae, risus.<br>
\*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.<br>
    Suspendisse id sem consectetuer libero luctus adipiscing.<br>

**如果列表项目间用空行分开，在输出 HTML 时 Markdown 就会将项目内容用 \<p> 标签包起来，举例来说**：<br>
\*   Bird<br>
\*   Magic<br>

**会被转换为：**<br>
\<ul><br>
\<li>Bird\</li><br>
\<li>Magic\</li><br>
\</ul><br>

**但是这个：**<br>
\*   Bird<br>
\*   Magic<br>

**会被转换为：**<br>
\<ul><br>
\<li>\<p>Bird\</p>\</li><br>
\<li>\<p>Magic\</p>\</li><br>
\</ul><br>

**列表项目可以包含多个段落，每个项目下的段落都必须缩进 4 个空格或是 1 个制表符：**<br>
1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

**如果你每行都有缩进，看起来会看好很多，当然，再次地，如果你很懒惰，Markdown 也允许：**<br>
\*   This is a list item with two paragraphs.

    This is the second paragraph in the list item. You're
only required to indent the first line. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit.

\*   Another item in the same list.<br>

**如果要在列表项目内放进引用，那 > 就需要缩进：**<br>
\*   A list item with a blockquote:<br>

    \> This is a blockquote<br>
    \> inside a list item.<br>
**如果要放代码区块的话，该区块就需要缩进两次，也就是 8 个空格或是 2 个制表符：**
\*   一列表项包含一个列表区块：

        <代码写在这>

**当然，项目列表很可能会不小心产生，像是下面这样的写法：** 
1986. What a great season.<br>

**换句话说，也就是在行首出现数字-句点-空白，要避免这样的状况，你可以在句点前面加上反斜杠。**<br>
1986\\. What a great season.

### 代码区块

**和程序相关的写作或是标签语言原始码通常会有已经排版好的代码区块，通常这些区块我们并不希望它以一般段落文件的方式去排版，而是照原来的样子显示，Markdown 会用 \<pre> 和 \<code> 标签来把代码区块包起来。**<br>

**要在 Markdown 中建立代码区块很简单，只要简单地缩进 4 个空格或是 1 个制表符就可以，例如，下面的输入：**<br>
这是一个普通段落：

    这是一个代码区块。 

**Markdown 会转换成：**<br>
\<p>这是一个普通段落：\</p><br>
<br>
\<pre>\<code>这是一个代码区块。<br>

\</code>\</pre><br>

**这个每行一阶的缩进（4 个空格或是 1 个制表符），都会被移除，例如：**<br>
Here is an example of AppleScript:

    tell application "Foo"
        beep
    end tell
**会被转换为：**<br>
\<p>Here is an example of AppleScript:\</p><br>

\<pre>\<code>tell application "Foo"<br>
    beep<br>
end tell<br>
\</code>\</pre><br>

**一个代码区块会一直持续到没有缩进的那一行（或是文件结尾）**<br>

**在代码区块里面， & 、 < 和 > 会自动转成 HTML<br> 实体，这样的方式让你非常容易使用 Markdown 插入范例用的 HTML<br> 原始码，只需要复制贴上，再加上缩进就可以了，剩下的 Markdown<br> 都会帮你处理，例如：**<br>
    \<div class="footer"><br>
        \&copy; 2004 Foo Corporation<br>
    \</div>
**会被转换为：**<br>
\<pre>\<code>\&lt;div class="footer"\&gt;<br>
    \&amp;copy; 2004 Foo Corporation<br>
\&lt;/div\&gt;<br>
\</code>\</pre><br>

**代码区块中，一般的 Markdown 语法不会被转换，像是星号便只是星号，这表示你可以很容易地以 Markdown 语法撰写 Markdown 语法相关的文件。**
### <span id=2.6>分割线</span>
**你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：**<br>
\* \* \*

\***

\*****

\- - -

\---------------------------------------<br>
## 区段元素
### 链接
Markdown 支持两种形式的链接语法： 行内式和参考式两种形式。

不管是哪一种，链接文字都是用 [方括号] 来标记。

要建立一个行内式的链接，只要在方块括号后面紧接着圆括号并插入网址链接即可，如果你还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可，例如：<br>
This is \[an example](http://example.com/ "Title") inline link.

\[This link](http://example.net/) has no title attribute.<br>

会产生：<br>
\<p>This is \<a href="http://example.com/" title="Title"><br>
an example\</a> inline link.\</p>

\<p>\<a href="http://example.net/">This link\</a> has no<br>
title attribute.\</p><br>

**如果你是要链接到同样主机的资源，你可以使用相对路径：**<br>
See my \[About](/about/) page for details

**参考式的链接是在链接文字的括号后面再接上另一个方括号，而在第二个方括号里面要填入用以辨识链接的标记：**<br>
This is \[an example][id] reference-style link.<br>

**你也可以选择性地在两个方括号中间加上一个空格：**<br>
This is \[an example] [id] reference-style link.

**接着，在文件的任意处，你可以把这个标记的链接内容定义出来**：<br>
[id]: http://example.com/  "Optional Title Here"

链接内容定义的形式为：

   * 方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字
   * 接着一个冒号
   * 接着一个以上的空格或制表符
   * 接着链接的网址
   * 选择性地接着 title 内容，可以用单引号、双引号或是括弧包着<br>
下面这三种链接的定义都是相同：<br>
[foo]: http://example.com/  "Optional Title Here"<br>
[foo]: http://example.com/  'Optional Title Here'<br>
[foo]: http://example.com/  (Optional Title Here)<br>

**请注意**：有一个已知的问题是 Markdown.pl 1.0.1 会忽略单引号包起来的链接 title。

链接网址也可以用尖括号包起来：<br>
\[id]: <http://example.com/>  "Optional Title Here"

**你也可以把 title 属性放到下一行，也可以加一些缩进，若网址太长的话，这样会比较好看：**<br>
[id]: http://example.com/longish/path/to/resource/here<br>
    "Optional Title Here"
    
**网址定义只有在产生链接的时候用到，并不会直接出现在文件之中。**

**链接辨别标签可以有字母、数字、空白和标点符号，但是并不区分大小写，因此下面两个链接是一样的：**<br>
[link text][a]<br>
[link text][A]<br>
**隐式链接标记功能让你可以省略指定链接标记，这种情形下，链接标记会视为等同于链接文字，要用隐式链接标记只要在链接文字后面加上一个空的方括号，如果你要让 "Google" 链接到 google.com，你可以简化成：**<br>
[Google][]<br>
**然后定义链接内容：**<br>
[Google]: http://google.com/

**由于链接文字可能包含空白，所以这种简化型的标记内也许包含多个单词：**<br>
Visit [Daring Fireball][] for more information.<br>

**然后接着定义链接：**<br>
[Daring Fireball]: http://daringfireball.net/<br>

**链接的定义可以放在文件中的任何一个地方，我比较偏好直接放在链接出现段落的后面，你也可以把它放在文件最后面，就像是注解一样。**

**下面是一个参考式链接的范例**：<br>
I get 10 times more traffic from [Google] [1] than from
[Yahoo] [2] or [MSN] [3].

  \[1]: http://google.com/        "Google"<br>
  \[2]: http://search.yahoo.com/  "Yahoo Search"<br>
  \[3]: http://search.msn.com/    "MSN Search"<br>
  
**如果改成用链接名称的方式写**：<br>
I get 10 times more traffic from [Google][] than from
[Yahoo][] or [MSN][].

  \[google]: http://google.com/        "Google"<br>
  \[yahoo]:  http://search.yahoo.com/  "Yahoo Search"<br>
  \[msn]:    http://search.msn.com/    "MSN Search"<br>
  
**上面两种写法都会产生下面的 HTML。**<br>
\<p>I get 10 times more traffic from<br> \<a href="http://google.com/"
title="Google">Google\</a> than from<br>
\<a href="http://search.yahoo.com/" title="Yahoo Search">Yahoo\</a><br>
or \<a href="http://search.msn.com/" title="MSN Search">MSN\</a>.\</p><br>

**下面是用行内式写的同样一段内容的 Markdown 文件，提供作为比较之用：**<br>
I get 10 times more traffic from<br> \[Google](http://google.com/ "Google")<br>
than from \[Yahoo](http://search.yahoo.com/ "Yahoo Search") or
\[MSN](http://search.msn.com/ "MSN Search").<br>

**参考式的链接其实重点不在于它比较好写，而是它比较好读，比较一下上面的范例，使用参考式的文章本身只有 81 个字符，但是用行内形式的却会增加到 176 个字元，如果是用纯 HTML 格式来写，会有 234 个字元，在 HTML 格式中，标签比文本还要多。**

**使用 Markdown 的参考式链接，可以让文件更像是浏览器最后产生的结果，让你可以把一些标记相关的元数据移到段落文字之外，你就可以增加链接而不让文章的阅读感觉被打断。**
### 强调
**Markdown 使用星号（\*）和底线（_）作为标记强调字词的符号，被 * 或 _ 包围的字词会被转成用 \<em> 标签包围，用两个 * 或 _ 包起来的话，则会被转成 <strong>，例如**：<br>
\*single asterisks*

\_single underscores_

\**double asterisks**

\__double underscores__<br>
**会转成:**<br>
\<em>single asterisks\</em>

\<em>single underscores\</em>

\<strong>double asterisks\</strong>

\<strong>double underscores\</strong>

**你可以随便用你喜欢的样式，唯一的限制是，你用什么符号开启标签，就要用什么符号结束**。

**强调也可以直接插在文字中间：**<br>
un\*frigging*believable<br>

**但是如果你的 * 和 _ 两边都有空白的话，它们就只会被当成普通的符号。**

**如果要在文字前后直接插入普通的星号或底线，你可以用反斜线：**<br>
\\* this text is surrounded by literal asterisks\\* 
### 代码
**如果要标记一小段行内代码，你可以用反引号把它包起来（`），例如：**<br>

Use the `printf()` function.

**会产生:**<br>
\<p>Use the \<code>printf()\</code> function.\</p><br>

**如果要在代码区段内插入反引号，你可以用多个反引号来开启和结束代码区段：**<br>
\`\`There is a literal backtick (`) here.``<br>

**这段语法会产生：**<br>
\<p>\<code>There is a literal backtick (`) here.\</code>\</p><br>

**代码区段的起始和结束端都可以放入一个空白，起始端后面一个，结束端前面一个，这样你就可以在区段的一开始就插入反引号：**<br>
A single backtick in a code span: \`\` ` ``

A backtick-delimited string in a code span: \`\` \`foo` ``<br>
**会产生：**<br>
\<p>A single backtick in a code span: \<code>`\</code>\</p>

\<p>A backtick-delimited string in a code span: \<code>`foo`\</code>\</p>

**在代码区段内，& 和尖括号都会被自动地转成 HTML 实体，这使得插入 HTML 原始码变得很容易，Markdown 会把下面这段：**<br>
Please don't use any \`<blink>` tags.<br>

**转为：**

\<p>Please don't use any \<code>\&lt;blink\&gt;\</code> tags.\</p>

你也可以这样写：<br>
\`\&#8212;\` is the decimal-encoded equivalent of \`\&mdash;`.

以产生:<br>
\<p>\<code>\&amp;#8212;\</code> is the decimal-encoded
equivalent of \code>\&amp;mdash;\</code>.\</p>

### 图片

很明显地，要在纯文字应用中设计一个「自然」的语法来插入图片是有一定难度的。

Markdown 使用一种和链接很相似的语法来标记图片，同样也允许两种样式： 行内式和参考式。

行内式的图片语法看起来像是：<br>
\!\[Alt text](/path/to/img.jpg)
![Alt text](/path/to/img.jpg)

\!\[Alt text](/path/to/img.jpg "Optional title")<br>
![Alt text](/path/to/img.jpg "Optional title")

详细叙述如下：<br>

   * 一个惊叹号 !
   * 接着一个方括号，里面放上图片的替代文字
   * 接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上 选择性的 'title' 文字。
   
参考式的图片语法则长得像这样：<br>
!\[Alt text][id]<br>
**「id」是图片参考的名称，图片参考的定义方式则和连结参考一样：**<br>
[id]: url/to/image  "Optional title attribute"<br>
到目前为止， Markdown 还没有办法指定图片的宽高，如果你需要的话，你可以使用普通的 \<img> 标签。
## 其他
### 自动连接
Markdown 支持以比较简短的自动链接形式来处理网址和电子邮件信箱，只要是用尖括号包起来， Markdown 就会自动把它转成链接。一般网址的链接文字就和链接地址一样，例如：<br>
\<http://example.com/><br>
<http://example.com/>

Markdown 会转为：<br>
\<a href="http://example.com/">http://example.com/\</a>

邮址的自动链接也很类似，只是 Markdown 会先做一个编码转换的过程，把文字字符转成 16 进位码的 HTML 实体，这样的格式可以糊弄一些不好的邮址收集机器人，例如：<br>
\<address@example.com><br>
<address@example.com>

Markdown 会转成：<br>
\<a href="&#x6D;&#x61;i&#x6C;&#x74;&#x6F;:&#x61;&#x64;&#x64;&#x72;&#x65;
&#115;&#115;&#64;&#101;&#120;&#x61;&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;
&#109;">&#x61;&#x64;&#x64;&#x72;&#x65;&#115;&#115;&#64;&#101;&#120;&#x61;
&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;&#109;\</a>

在浏览器里面，这段字串（其实是 \<a href="mailto:address@example.com">address@example.com\</a>）会变成一个可以点击的「address@example.com」链接。<br>

（这种作法虽然可以糊弄不少的机器人，但并不能全部挡下来，不过总比什么都不做好些。不管怎样，公开你的信箱终究会引来广告信件的。）<br>
### 反斜杠
Markdown 可以利用反斜杠来插入一些在语法中有其它意义的符号，例如：如果你想要用星号加在文字旁边的方式来做出强调效果（但不用 \<em> 标签），你可以在星号的前面加上反斜杠：<br>
\\\*literal asterisks\\*

Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：<br>
\   反斜线<br>
`   反引号<br>
\*   星号<br>
_   底线<br>
{}  花括号<br>
[]  方括号<br>
()  括弧<br>
\#   井字号<br>
\+   加号<br>
\-   减号<br>
.   英文句点<br>
!   惊叹号<br>
## 总结
markdown是一个非常好用的书写语言:<br>
特点就是容易读容易写,并且兼容HTML这点非常舒服
HTML的任何标签格式 Markdown都好使<br>
在我认为Markdown中无论是标签也好,引用也罢都非常简单
也很容易上手 对列表的格式要求非常松  列表也可以含有多个段落

段落代码还可以表示颜色

markdown的链接分为两种  行内和参考两种<br>
行内:<br>
This is \[an example](http://example.com/ "Title") inline link.<br>

\[This link](http://example.net/) has no title attribute<br>

参考:<br>
This is [an example][id] reference-style link.<br>
然后还需定义id:<br>
[id]: http://example.com/  "Optional Title Here"

插入图片也差不多:<br>
行内:<br>
![Alt text](/path/to/img.jpg)<br>
!\[Alt text](/path/to/img.jpg)<br>
参考:<br>
![Alt text][id]<br>
同样也需要定义[id]<br>
\[id]: url/to/image  "Optional title attribute"

在Markdown中反斜杠有很多用到的地方最直接的就是可以让markdown不去转换代码成Html格式

总而言之 :markdown是一个非常非常耗用的书写语言
比word不知NB了多少倍
-------------
