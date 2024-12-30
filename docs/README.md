# AutoCoder 快速入门指南


> auto-coder 是一个基于YAML配置的命令行开发辅助工具，可以根据您的需求自动迭代开发已有项目。

我的目标是开发一个深度结合 cursor 的版本, 丢弃许多其他的逻辑, 只关心生成合适的提示词 ---  生成需求文档, 然后交给 cursor 来完成代码的生成. 
- 但是感觉成本很不划算呢，我直接让 cursor 是自己设计提示词不就行了吗 ... 
- 另外一个解答的方式就是我把它当成一个提示词生成器使用不就行了吗？ `Mode: nature language auto detect (ctl+k) | Human as Model: true (ctl+n)` 
  

这个项目相当于一个开源的 cursor 项目，有一种 128k 手搓上下文的感觉. 



[AutoCoder 飞书文档](https://swze06osuex.feishu.cn/docx/YkuOdnq3doiA5nx1ntCcor28nhe)

## 快速安装

### 基础环境配置

```bash
# 创建并激活 conda 环境
conda create --name auto-coder python=3.10.11
conda activate auto-coder

# 安装 auto-coder
pip install -U auto-coder

# 启动 Ray
ray start --head
```


### 启动模型代理

你需要先申请 deepseek 的 token，然后执行：

```bash
# 替换 ${MODEL_DEEPSEEK_TOKEN} 为你的实际 token
easy-byzerllm deploy deepseek-chat --token $MODEL_DEEPSEEK_TOKEN --alias deepseek_chat
```

验证模型是否正常工作：

```bash
easy-byzerllm chat deepseek_chat "你好"
```

## 使用方式


### 方式一：Chat 模式（推荐）

在项目根目录执行：

```bash
chat-auto-coder
```

然后可以直接输入编程指令：

```bash
/coding 在 src 目录下创建app.py, 在该文件中实现一个计算器，使用 gradio 来实现。
```

系统会自动生成代码并保存到指定位置。

### 方式二：命令行模式

1. 初始化项目

```bash
# 在项目根目录执行
auto-coder init --source_dir .
```

这会生成 `.auto-coder` 和 `actions` 两个目录。

2. 编辑配置文件

打开 `actions/000_example.yml`，修改内容：

```yaml
project_type: py
include_file:
  - ./base/base.yml
  - ./base/enable_index.yml
  - ./base/enable_wholefile.yml    

human_as_model: false  

query: |  
  帮我在项目根目录下创建一个 src/server.py, 使用 fastapi ，创建一个 /hello 接口，返回 world.
```

3. 执行命令

```bash
auto-coder --file actions/000_example.yml
```
## 本地预览文档

```bash
# 安装 docsify-cli
npm i docsify-cli -g

# 运行本地服务器
docsify serve .
``` 