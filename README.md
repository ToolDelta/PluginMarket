# ToolDelta 插件市场 Official
<b>如何使用插件市场？</b>
 - 直接在启动器进入插件市场
 - 在最新版的 ToolDelta 的控制台输入 <code>插件市场</code>

<b>为什么选择插件市场？</b>
 - 共享 ToolDelta 插件
 - 便捷的安装和使用插件
 - 你可以在此发布和分享你所制作的 ToolDelta 插件

<b>NOTE</b>
 - 我们无法保证所有插件的安全性, 请自行检查部分插件有无恶意行为。

<b>如何上传你的插件？</b>
 - 在 <code>Pull Requests</code> 处提交请求即可
 - 将插件文件夹上传到本项目主目录下
 - 在 `market_tree.json` 添加自己的插件信息

<b>上传的插件的规范格式和要求？</b>
 - 允许上传的文件类型: Python脚本, 文本文件(包括Markdown, TXT file等)
 - 插件需要放在 <code>your_plugin_name/</code> 目录下, 主插件文件需要以 <code>__init__.py</code> 命名
 - 上传之后, 请务必同时更改 <code>market_tree.json</code> ,  按照其格式添加上自己的插件信息.
    - <b>market_tree.json更改说明</b>
    这是一个标准的插件详情的例子.
    ```
    "聊天栏菜单": {
        "author": "SuperScript",
        "version": "0.0.4",
        "description": "所有使用到聊天栏菜单的组件的前置组件",
        "limit_launcher": null,
        "pre-plugins": {},
        "plugin-type": "classic"
    },
    ```
    - "聊天栏菜单" 键: 插件的名字, 创建插件文件夹的时候也将使用这个名字
    - "plugin-type" 值:
        - 如果是 原 DotCS 插件: "dotcs"
        - 如果是 ToolDelta 组合式插件: "classic"
        - 如果是 ToolDelta 注入式插件: "injected"
    - "description" 值: 插件的简介(功能摘要)
    - "limited-launcher" 值: 限制插件只能在哪种启动器框架运行, 通用即null  
    - "pre-plugins" 值: 前置插件的名称与最低需求版本的键值对, 都为string  
 - 上传内容若会对用户的设备造成损害, 或会盗窃用户信息的插件, <b>将不予通过审核。</b>