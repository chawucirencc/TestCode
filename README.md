# TestCode
测试代码，各个函数模块和类模块不联系。实现基础的测试功能。

在`iptest`代码内，192行的select_data函数的功能是查询数据库中已经存在的数据，并且将其保存到一个list中，这样在每次进行判断的时候都会进行一次查询，虽然数据量不大，但是非常的麻烦和浪费性能。