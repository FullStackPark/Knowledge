Python File(文件) 方法
==================

  file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数： 

 
<table>


</table>

<table>
<tbody><tr>
<th style="width:5%">序号</th><th>方法及描述</th></tr>
<tr><td>1</td><td><p><a href="file-close.html">file.close()</a></p><p>关闭文件。关闭后文件不能再进行读写操作。</p></td></tr>
<tr><td>2</td><td><p><a href="file-flush.html">file.flush()</a></p><p>刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。</p></td></tr>
<tr><td>3</td><td><p><a href="file-fileno.html">file.fileno()</a></p><p>
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。</p></td></tr>
<tr><td>4</td><td><p><a href="file-isatty.html">file.isatty()</a></p><p>如果文件连接到一个终端设备返回 True，否则返回 False。</p></td></tr>
<tr><td>5</td><td><p><a href="file-next.html">file.next()</a></p><p>返回文件下一行。</p></td></tr>
<tr><td>6</td><td><p><a href="python-file-read.html">file.read([size])</a></p><p>从文件读取指定的字节数，如果未给定或为负则读取所有。</p></td></tr>
<tr><td>7</td><td><p><a href="file-readline.html">file.readline([size])</a></p><p>读取整行，包括 "\n" 字符。</p></td></tr>
<tr><td>8</td><td><p><a href="file-readlines.html">file.readlines([sizehint])</a></p><p>读取所有行并返回列表，若给定sizeint&gt;0，则是设置一次读多少字节，这是为了减轻读取压力。</p></td></tr>
<tr><td>9</td><td><p><a href="file-seek.html">file.seek(offset[, whence])</a></p><p>设置文件当前位置</p></td></tr>
<tr><td>10</td><td><p><a href="file-tell.html">file.tell()</a></p><p>返回文件当前位置。</p></td></tr>
<tr><td>11</td><td><p><a href="file-truncate.html">file.truncate([size])</a></p><p>截取文件，截取的字节通过size指定，默认为当前文件位置。 </p></td></tr>
<tr><td>12</td><td><p><a href="python-file-write.html">file.write(str)</a></p><p>将字符串写入文件，没有返回值。</p></td></tr>
<tr><td>13</td><td><p><a href="file-writelines.html">file.writelines(sequence)</a></p><p>向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。</p></td></tr>
</tbody>
</table>