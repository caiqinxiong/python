1. cookie session 

   django操作cookie

   ```
   request.COOKIES.get()
   response.set_cookie(key,value,max_age=5)
   response.delete_cookie(key)
   ```

   django操作session

   ```
   request.session.get()
   request.session[key] = value
   request.session.pop(key)
   del request.session[key] 
   request.session.delete() 
   request.session.flush() 
   ```

2. 中间件

   5个方法  4个特点

   process_request(self,reuqest)

   执行时间: 路由匹配之前

   执行顺序: 按照注册顺序  顺序执行

   返回值:

   ​			None   正常流程

   ​			response 当前中间件之后的中间件的process_request 路由匹配 process_view 视图 都不执行,直接去执行当前中间件的process_response的方法

   

   process_view(self,reuqest,view_func,args,kwargs)

   执行时间: 路由匹配之后,视图之前

   执行顺序: 按照注册顺序  顺序执行

   返回值:

   ​			None   正常流程

   ​			response 当前中间件之后的中间件的 process_view 视图 都不执行,直接去执行最后一个中间件的process_response的方法

   

   process_response(self,reuqest,response)

   执行时间:  视图之后

   执行顺序: 按照注册顺序  倒叙执行

   返回值:

   ​			response :必须返回

   

   process_exception(self,reuqest,exception)

   执行时间: 视图层面有错误才执行

   执行顺序: 按照注册顺序  倒叙执行

   返回值:

   ​			None   交由下一个中间件处理异常,都不处理Django处理异常

   ​			response 当前中间件之后的中间件的 process_exception  不执行,直接去执行最后一个中间件的process_response的方法

   

   process_template_response(self,reuqest,response)

   执行时间: 视图返回一个template_response

   执行顺序: 按照注册顺序  倒叙执行

   返回值:

   ​		 response :必须返回

   

3. ajax

   ajax 是js技术, 发请求. 

   特点: 异步. 局部刷新, 数据量小

   jq :

   ```
   
   $.ajax({
   	url :  发请求的地址,
   	type:  'post',
   	data: {'xx','xx' },
   	succsess:function (res) {  
   		
   	}
   
   })
   
   ```

   上传文件

   ```
   var form_data = new FormData()
   form_data.append('f1',$('#f1')[0].files[0])
   form_data.append('k1','v1')
   $.ajax({
   	url :  发请求的地址,
   	type:  'post',
   	data: form_data,
   	processData:false,
   	contentType:false,
   	succsess:function (res) {  	
   	}
   
   })
   ```

   ajax通过Django的csrf的校验

   ```
   $.ajax({
   	url :  发请求的地址,
   	type:  'post',
   	data: { 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val() },
   	succsess:function (res) {  	
   	}
   
   })
   ```

   ```
   $.ajax({
   	url :  发请求的地址,
   	type:  'post',
   	hearders :{'x-csrftoken':$('[name="csrfmiddlewaretoken"]').val() },
   	data: { },
   	succsess:function (res) {  	
   	}
   
   })
   
   ```

4. form

   form组件



CMDB

自动采集服务器的资产信息

配置管理数据库

excel 

跳板机

代码发布



实现的思路

1. 代码的架构
   - agent   
   - api
   - 后台管理

2. 

   agent 

   - 将agent脚本放在每台被采集的主机上
   - 每天定时启动脚本(subprocess)执行命令,采集资产 进行汇报资产
   - api接收到请求 资产入库

   salt\ansible

   - 将agent脚本放在中控机,(ansible\saltstack )
   - 每天定时启动脚本,从api获取今日采集的主机列表,通过salt或ansible连接主机采集资产 进行汇报资产
   - api接收到请求 资产入库

   ssh

   - 将agent脚本放在中控机
   - 每天定时启动脚本,从api获取今日采集的主机列表,通过ssh(Paramiko)连接主机采集资产 进行汇报资产
   - api接收到请求 资产入库

目标: 兼容三种模式 + 支持扩展 







类的约束

```python
import abc


class Person(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        print('talk')

class China(Person):

    def talk(self):
        pass

p = China()



class Person():

    def talk(self):
        raise NotImplementedError('talk must be Implemented')

class China(Person):
    pass

p = China()
p.talk()

```











