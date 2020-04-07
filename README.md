# OmegaTensor

![starkidstory](Image/starkidstory_title.png)

![omega](Image/omega_title.png)

### Omega Tenser

Omega Tensor 是一个整理和实践众多有关 Tensorflow 和 神经网络 的教程或项目，整个项目包括 一级目录、二级目录。

一级目录为整个教程或项目的名称，一级目录的命名需要独一无二，若是教程的实践，命名最好直接反映教程的名称或来源。一级目录下需要添加
README.md 文件说明这个教程或项目的来源。

二级目录是一级目录下教程或项目的实现。如是教程，二级目录名最好是教程的章节名，命名也需要独一无二，二级目录内也需要添加 README.md 
作为这个实现的说明和作者提名，实现可以使用 jupyter 或 python 脚本，但实现的每个函数都要写好函数的作用，参数及返回值。

Python:

```python
def some_function(a: int, b: bool) -> float:
    """
    这个函数的作用是。。。。
    :param a: 参数 a 是。。。
    :param b: 参数 b 是。。。
    :return: 返回值是。。。
    """
```

若是 jupyter，函数的作用说明可以任意设置，大致以清楚的笔记形式展出。

若你的实现需要一些前提条件或说明，均可写于当前二级目录下的 README.md 中，格式均以 MarkDown 形式为准。

目前一级目录包括：

- [Tensorflow_official](Tensorflow_official) - 主要包括 tensorflow 的官方教程。
- [Github_eat_tensorflow2](Github_eat_tensorflow2) - Github 上的 'eat_tensorflow2_in_30_days' 教程。
- [Other](Other) - 其他的不成体系的教程或项目，例如单独的博客教程。
- [Project](Project) - 大型项目。

### 关于 commit 到 GitHub 的 summary

一般起名 'Update xxx' 为更新教程里的 xxx，'Fixed xxx' 为修复 xxx bug，'Remove xxx' 为删除 xxx。

多看别人的代码，这个 repo 的关键就是要代码交流，写其他人易懂的代码。
