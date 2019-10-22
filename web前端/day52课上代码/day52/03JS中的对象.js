// JS中自定义对象

// var person = {name: '小强', age: 38};  // 在JS的对象中,键(属性)默认不用加引号;并且自动把单引号转成双引号
// console.log(person);
// // 单独取对象的属性
// console.log("name:", person.name);
// console.log("age:", person.age);
//
// // 遍历对象的属性
// for (var i in person){
//     console.log(i);
//     console.log(person[i]);
// }


// Date对象
var d1 = new Date();
console.log(d1);
console.log(typeof d1);
console.log(d1.toLocaleString());  // 转成字符串格式的本地时间
console.log(typeof d1.toLocaleString());

// 生成指定时间的Date对象
// var d2 = new Date("2004/3/20 11:12");
// console.log(d2.toLocaleString());  // 转成字符串格式的本地时间
// console.log(d2.toUTCString());  // 转成字符串格式的UTC时间

var d2 = new Date("2018-3-11 11:12");
console.log(d2.toLocaleString());  // 转成字符串格式的本地时间
console.log(d2.toUTCString());  // 转成字符串格式的UTC时间

console.log(d2.getDate());  // 获取那一天(多少号)
console.log(d2.getDay());  // 获取星期几
console.log(d2.getMonth());  // 获取月份
console.log(d2.getFullYear());  // 获取年
console.log(d2.getHours());  // 获取小时
console.log(d2.getMinutes());  // 获取分钟
console.log(d2.getSeconds());  // 获取秒
console.log(d2.getTime());  // 获取时间戳

// JSON对象
console.log("==============================");

var s = '{"name": "xiaoqiang", "age": 38}';
// 把字符串转换成JS内部的对象
var ret = JSON.parse(s);
console.log(ret);
console.log(typeof ret);
// 把JS内部的对象转换成字符串
var s2 = JSON.stringify(ret);
console.log(s2);
console.log(typeof s2);

// RegExp对象 --> Python re模块
// 生产 RegExp对象
var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$");
var regexpRet1 = reg1.test("xiaoqiang");
console.log(regexpRet1);

var regexpRet2 = reg1.test("1xiaoqiang");
console.log(regexpRet2);

console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("xiaoqiang"));
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("1xiaoqiang"));

// 坑1 (正则表达式中间一定不可以有空格)
console.log("============================================");
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("xiaoqiang"));
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("1xiaoqiang"));

// 坑2
// test()不传值相当于传了一个undefined进去
// 然后test()就把这个undefined当成是"undefined"来判断
console.log("============================================");
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("undefined"));
console.log(/^[0-9a-zA-Z][a-zA-Z0-9_]{5,11}$/.test());
console.log(/^[0-9][a-zA-Z0-9_]{5,11}$/.test(undefined));
console.log(/^[0-9][a-zA-Z0-9_]{5,11}$/.test("undefined"));

// JS正则的两种模式
// 1. g 表示全局
// 2. i 忽略大小写
var ss = "Alexdashabi";
var s3 = ss.replace(/a/gi, "哈哈哈");  // 不是改变默认的字符串,而是生成了一个新的字符串
console.log(s3);

// 坑3
// 当正则表达式使用了全局模式(g)的时候,并且你还让它去检测一个字符串,此时会引出来一个lastIndex
// lastIndex会记住上一次匹配成功的位置,并把下一次要开始椒盐的位置记住
//
console.log("===============================");
var r = /alex/g;
console.log(r.test("alex"));  // true
console.log(r.lastIndex);  // 4
console.log(r.test("alex"));  // false
console.log(r.lastIndex);
console.log(r.test("alex"));  // true
console.log(r.lastIndex);
console.log(r.test("alex"));  // false

