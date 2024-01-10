## 每次运行自动为测试报告添加时间戳
- 依赖于pytest-html插件
- 要让本插件生效需要在命令行参数中指定 `--html=xxx.html`
- 本插件运行时将会替换该参数

```shell
pytest
# ...
# plugins: ..., report-autoname-0.0.1
# ...
```
