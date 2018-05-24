看看要做成什么样子：

> ![结果](https://img-blog.csdn.net/20170524215244525?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzE2NTU5NjU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
>
> 界面不好看我知道。。。

## **环境搭建**

> 本文使用 dva + antd 做开发，别问我为什么，公司要用。。

### **1.安装nodejs。**

* 打开这篇文章的应该都已经装好了，我就不多说了。

### **2.安装dva-cli**

* `npm install dva-cli -g`

    > dva ： https://github.com/dvajs/dva

### **3.创建新应用**

* `dva new todo-list`

    > 应该会自动执行npm start的，如果没有就自己执行一下。之后启动项目，访问 [http://localhost:8000](http://localhost:8000/)，看到dva欢迎页面，证明创建成功

### **4.使用 antd**

通过 npm 安装 antd 和 babel-plugin-import 。babel-plugin-import 是用来按需加载 antd 的脚本和样式的

* `npm install antd babel-plugin-import --save`

编辑 .roadhogrc，使 babel-plugin-import 插件生效。

```language-js
"extraBabelPlugins": [
    "transform-runtime",
    ["import", { "libraryName": "antd", "style": "css" }]
],
```


> antd: [https://ant.design](https://ant.design/)

### **5.定义路由，使用 dva-cli 创建。**

* `dva g route List`

在routes目录下自动创建了List.js 和 List.css，并且在router.js中添加了路由信息。

访问http://localhost:8000/#/List 可以看到List.js自动生成的模板。 

编辑List.js：

```language-js
import React from 'react';
import { connect } from 'dva';
import List from '../components/List';
import Add from '../components/Add';

const Lists = ({ dispatch, lists, inputs }) => {
  function handleDelete(id) {
    dispatch({
      type: 'lists/delete',
      payload: id,
    });
  }
  function handleAdd() {
    dispatch({
      type: 'lists/add',
      payload: inputs.input,
    });
  }

  function handelChange(e) {
    dispatch({
      type: 'inputs/change',
      payload: e.target.value
    })
  }
  return (
    <div>
      <Add onAdd={handleAdd} onChange={handelChange} input={inputs.input}/>
      <br/>
      <hr/>
      <h2>List of Products</h2>
      <br/>
      <List onDelete={handleDelete} lists={lists} />
    </div>
  );
};

// export default Lists;
export default connect(({ inputs, lists }) => ({
  inputs, lists,
}))(Lists);
```



我们使用了两个模板：List和Add， 我们来创建一下。

### **6.创建模板**

在component下新建 Add.js 和 List.js。

Add.js:

```language-javascript
/**
 * Created by chengfan on 2017/5/24.
 */
import React from 'react'
import PropTypes from 'prop-types';
import { Input, Icon, Button } from 'antd'

const Add = ({ onAdd, onChange, input }) => {
  return (
    <div>
      <Input
        placeholder="Enter your userName"
        prefix={<Icon type="user" />}
        value={input}
        onChange={onChange}
      />
      <Button type="primary" onClick={ onAdd }>添加</Button>
    </div>
  )
};

Add.propTypes = {
  onAdd: PropTypes.func.isRequired,
  input: PropTypes.string.isRequired,
};

export default Add;
```


List.js

```language-js
/**
 * Created by chengfan on 2017/5/23.
 */
import React from 'react';
import PropTypes from 'prop-types';
import { Table, Popconfirm, Button } from 'antd';

const List = ({ onDelete, lists }) => {
  const columns = [
    {
      title: 'Id',
      dataIndex: 'id',
    },
    {
      title: 'Name',
      dataIndex: 'name',
    }, {
    title: 'Actions',
    render: (text, record) => {
      return (
        <Popconfirm title="Delete?" onConfirm={() => onDelete(record.id)}>
          <Button>Delete</Button>
        </Popconfirm>
      );
    },
  }];
  return (
    <Table
      dataSource={lists}
      columns={columns}
      pagination = {{ pageSize: 6}}
    />
  );
};

List.propTypes = {
  onDelete: PropTypes.func.isRequired,
  lists: PropTypes.array.isRequired,
};

export default List;
```


接下来创建相应的model

### **7.创建model，使用 dva-cli 创建**

* `dva g model List`
* `dva g model Add`

> 使用 cli 创建的 model 会自动在 index.js 里绑定

models/list.js:

```language-js
export default {
  namespace: 'lists',
  state: [],
  reducers: {
    add(state, { payload: name }){
      let id = state.reduce( (previous,current) => previous.id > current.id ? previous : current).id;
      id++;
      return [...state, { name, id}];
    },
    delete(state, { payload: id }) {
      return state.filter(item => item.id !== id);
    },
  },
};
```


models/add.js

```language-js
export default {
  namespace: 'inputs',
  state: {
    input: 'name',
  },
  reducers: {
    change(state, { payload: name }){
      return  {input: name}
    },
  },
};
```


### **8.在index.js里放一些初始数据**

index.js

```language-js
import dva from 'dva';
import './index.css';

// 1. Initialize
const app = dva({
  initialState: {
    lists: [
      { name: 'dva', id: 1 },
      { name: 'antd', id: 2 },
    ]
  },
});

app.model(require('./models/list'));
app.model(require('./models/add'));

// 2. Plugins
// app.use({});

// 3. Model
// app.model(require('./models/example'));

// 4. Router
app.router(require('./router'));

// 5. Start
app.start('#root');
```


### **9.完成，测试**

启动项目，访问http://localhost:8000/#/list，可以看到一开始展示的效果

界面不是很美观，但是基本功能已经有了。代码虽然不够优雅，但是通过写这个demo 让我对 react 的理解更深了一些。

文章是流水账的形式，只是把代码贴了出来，没有详细的讲解，因为我自己也是初学者，怕讲错了。。。如果需要讲解的话，请给我留言，我再补上，最近一直忙着学习，所以码字的时间就少了。

代码可以到github上取。新建的账号，以前的太乱了。。如果对你有帮助，可以点一波star~
