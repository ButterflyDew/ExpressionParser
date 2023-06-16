# Expression Parser

编译原理大作业

> python main.py 即可使用

允许本应用需要下载 graphviz 包等一些常见 python 库，本界面在 MacOS 下开发，Windows 可能存在一些兼容性问题

ExpressionParser 为后端内容与接口文件。

OutFile 为输出文件，分别存在词法分析表，语法分析树，语法分析DFA，语义分析四元式

test 为参考测试数据
1. (x+2)^2/Y 发生词法分析错误
2. (z-3^2+4*x+)*5.6/7*8 发生语法分析错误
3. (1+x)^a/2*x
4. 2^(1-x)/3

小组成员：[ButterflyDew](https://github.com/ButterflyDew), [Wepdekr](https://github.com/Wepdekr)

