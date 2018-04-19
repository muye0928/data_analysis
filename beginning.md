这是一个介绍[编程思想](http://chengyichao.info/learnable-programming/)的文，讲的不错。

> 编程的意义在于概括某段代码，我们可以修改程序，让他在任何我们想要的地方画房子，我们可以让程序画很多房子，画不同高度的房子，重要的是通过一句说明我们就可以画不同高度的房子。

    function house(x,y){
        rect(x,y,40,105-y);
        }
    house(35,48)
    house(79,80)

 - 找到了一个找小项目的地方：[JOBBOLE](http://python.jobbole.com/category/project/)

- 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key
- set的原理和dict一样，所以，同样不可以放入可变对象