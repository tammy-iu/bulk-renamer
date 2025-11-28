# Bulk Renamer

一个简单易用的 Python 批量文件重命名工具。

## 功能
- 批量重命名指定文件夹中的文件
- 支持自定义前缀、后缀、起始编号和文件后缀名
- 使用 `config.json` 配置行为

---

## 使用方法

### 1. 放置文件
将你需要重命名的文件放入一个文件夹，如 `files/`。

### 2. 修改配置
编辑 `config.json`：

```json
{
  "folder": "./files",
  "prefix": "image_",
  "suffix": "",
  "start_num": 1,
  "extension": ".jpg"
}
