Beautiful Soup对文档的解析速度不会比它所依赖的解析器更快,如果对计算时间要求很高或者计算机的时间比程序员的时间更值钱,那么就应该直接使用 lxml .
换句话说,还有提高Beautiful Soup效率的办法,使用lxml作为解析器.nBeautiful Soup用lxml做解析器比用html5lib或Python内置解析器速度快很多.


解析部分文档(利用SoupStrainer类定义文档的某段内容)不会节省多少解析时间,但是会节省很多内存,并且搜索时也会变得更快.

如果同样的代码在不同环境下结果不同,可能是因为两个环境下使用不同的解析器造成的.例如这个环境中安装了lxml,而另一个环境中只有html5lib,
解析器之间的区别 中说明了原因.修复方法是在 BeautifulSoup 的构造方法中中指定解析器。

默认情况下,Beautiful Soup会将当前文档作为HTML格式解析,如果要解析XML文档,要在 BeautifulSoup 构造方法中指定第二个参数 “xml”:
soup = BeautifulSoup(markup, "xml")