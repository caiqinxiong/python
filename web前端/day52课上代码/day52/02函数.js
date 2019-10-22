// 函数的定义
// function foo(a,b) {
//     console.log("a:", a);
//     console.log("b:", b);
//     return a+b;
// }
// 匿名函数
// var func = function (a, b) {
//     console.log("a:", a);
//     console.log("b:", b);
//     return a+b;
// };

// 立即执行函数
// (function (a,b) {
//     console.log("立即执行函数");
//     console.log(a+b);
//     var sss = "我是函数内部的变量";
// })(11,22);

// console.log(sss);  // 外部访问不到函数内部定义的变量(用立即执行函数防止变量污染全局变量)
// console.log("立即执行函数");
// console.log(a+b);
// var sss = "我是函数内部的变量";

console.log("===========================");
// 函数的调用
// var ret1 = foo(11,22,33,44,55);
// var ret1 = foo(11); // 11+undefined --> NaN
// console.log("a+b=", ret1);

// var ret2 = func(11, 22);
// console.log(ret2);

// arguments
// function func2(a,b) {
//     console.log("总共有" + arguments.length + "个参数");
//     var ret = 0;
//     for (var i=0;i<arguments.length;i++){
//         ret += arguments[i]
//     }
//     return ret;
// }
//
// console.log(func2(11,22,33));


// JS中的词法分析
var age = 18;
function func3(){
  console.log(age);  // 去AO找age
  var age = 22;  // AO.age=undefined
  console.log(age);
  // function age() {  // AO.age= function(){...}
  //     console.log("xxxx");
  // }
}

func3();  // 问：执行func3()之后的结果是？



// 18 22
// 22 22
// 22 18
// 18 18
// null 22
// undefind 22


var age = 18;
function foo(){
  console.log(age);
  var age = 22;
  console.log(age);
  function age(){
    console.log("呵呵");
  }
  console.log(age);
  age();
}
foo();  // 执行后的结果是？

// 1. 先分析 给AO赋值
// var age = 22;  --> AO.age=undefined;
// function age(){console.log("呵呵");}  --> AO.age=function(){...}

// 2. 真正执行阶段 就去AO上找
// function(){...}
// 22
// 22

// 总共三个值


