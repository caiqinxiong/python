# -*- coding:utf-8 -*-

# 股票查询接口
class Shares:
    # 获取股票列表信息
    def shares_lst(self):
        with open("file","r",encoding="utf-8") as f:
            f_title = f.readline().strip().split(" ")
            f_title = list(filter(None,f_title))
            # print(f_title)
            lst = []
            for line in f:
                line = line.strip().split(" ")
                f_lst = list(filter(None,line))
                dic = {}
                for i in range(len(f_lst)):
                    dic[f_title[i]] = f_lst[i]
                # print(dic)
                lst.append(dic)
            return lst
    # 股票查询
    def shares_query(self):
        shares_list = self.shares_lst()
        query_lst = []
        query = input("股票查询接口>>").strip()
        for item in shares_list:
            for key in item:
                if key == "名称" and query in item[key]:
                    query_lst.append(item)
                    print(item)

                elif (query.split(">")[0] in key) and (">" in query) and float(item[key].split("%")[0]) > float(query.split(">")[-1]):
                    query_lst.append(item)
                    print(item)

                elif (query.split("<")[0] in key) and ("<" in query) and float(item[key].split("%")[0]) < float(query.split("<")[-1]):
                    query_lst.append(item)
                    print(item)

        print(f"共查询出 {len(query_lst)} 条数据")
        query_lst.clear()

        isContinue = input("要继续查询吗？'b'(继续）/ 'q'(退出):")
        if isContinue.upper() == "B":
            self.shares_query()  # 满足条件递归查询
        elif isContinue.upper() == "Q":
            print("退出股票查询系统")
if __name__ == "__main__":
    p=Shares()
    p.shares_query()


# 二分法递归查询
# li为列表，item为要查询的元素
def merge_search(li,item):
    if not li:   # 里面查到尽头没有元素
        return False
    mid = len(li)//2 # 记录中间位置
    if li[mid] == item: # 查询元素就在中间位置
        return True
    elif li[mid] > item: # 中间的位置比要查找的item元素大
        return merge_search(li[:mid],item)  # 如果mid比item大，说明item可能会出现在mid左边，对左半部分进行再查找
    else: # 中间的位置比要查找的item元素小
        return merge_search(li[mid+1:], item)  # 对右半部分进行查询

if __name__ == "__main__":
    li = [2, 1, 3, 5, 6, 4]
    li.sort()  # 缺点必须是有序序列
    print(merge_search(li,10)) # 查询不存在元素
    print(merge_search(li,6))  # 查询存在的元素
