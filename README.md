# Python Practice

四个 Python 基础练习项目，覆盖字典、文件 I/O、异常处理、命令行交互等核心知识点。

## 环境要求

- Python 3.8+
- 无需第三方依赖

## 练习清单

### 练习 1：学员花名册管理器（customer.py）

用字典管理学员信息（姓名、邮箱、加入日期），支持查询、添加、删除三种操作。

**运行方式：**
```bash
python customer.py
```

**功能点：** 字典操作、命令行菜单循环、大小写归一化处理。

---

### 练习 2：文本词频统计器（word_count.py）

输入一段英文文本，统计每个单词出现次数，过滤停用词后输出 Top 10。

**运行方式：**
```bash
python word_count.py
```

**功能点：** 字符串清洗、`collections.Counter` 计数、按值排序。

---

### 练习 3：待办事项清单(todo_list.py)

支持添加、查看、完成待办事项，数据持久化到 `Todo List.json` 文件，重启程序后自动加载。

**运行方式：**
```bash
python todo_list.py
```

**功能点：** JSON 文件读写、文件不存在的异常处理、增量保存。

---

### 练习 4：安全的计算器（safe_calculator.py）

支持四则运算（+ - * /），对非数字输入、除零错误、退出操作做了完整异常处理。

**运行方式：**
```bash
python safe_calculator.py
```

**功能点：** 多层异常防御（`ValueError` / `ZeroDivisionError`）、输入校验函数封装、优雅退出。

---

## 作者

Lilian
