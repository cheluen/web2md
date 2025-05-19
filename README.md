# 网页转 Markdown 脚本

这是一个简单的 Python 脚本，用于将网页内容转换为 Markdown 格式。

## 依赖

本脚本依赖于 `requests` 和 `markdownify` 库。

## 安装依赖

建议使用虚拟环境来安装依赖。

1. **创建虚拟环境** (如果还没有安装 `virtualenv`，请先安装: `pip install virtualenv`)

   ```bash
   virtualenv venv
   ```

2. **激活虚拟环境**

   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **安装依赖**

   激活虚拟环境后，使用以下命令安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 在脚本所在的同一目录下创建一个名为 `url.txt` 的文件。
2. 在 `url.txt` 文件中，每行输入一个你要转换的网页 URL。
3. 运行脚本：

   ```bash
   python web2md.py
   ```

脚本将读取 `url.txt` 中的 URL，并将每个网页的内容转换为 Markdown 格式。

转换后的 Markdown 文件将根据 URL 的一级域名自动存放到相应的文件夹中（例如，`google/index.md` 或 `example/path_to_page.md`）。

## 注意

- 本脚本目前只转换主页面内容，不处理子页面或页面内的链接。
- 转换效果取决于网页的结构和 `markdownify` 库的能力，可能无法完美还原所有网页布局。
