# test1013lh

一个使用 Python 标准库的最小项目，无第三方依赖。

## 环境

Python 3.10 或更高版本；云环境已验证 Python 3.12。

## 运行

在仓库根目录执行：

```sh
python3 main.py
```

预期输出：`Hello, world!`

## 测试

```sh
python3 -m unittest discover -s tests -v
```

云任务使用 `/workspace/test1013lh` 中现有的检出，无需创建 Git worktree。
