

# 实际返回结果
d1 = {
    "title" : "1",
    "slogan" : "way to explore",
    "description" : "创意工作者们的社区",
    "domain" : "www.v2ex.com"
}

# 预期结果
d2 = {
    "title" : "V2EX",
    "slogan" : {
        "k1": {
            "k2":"v2"
        }
    },
}
for k, v in d2.items():
    # print(k, v)
    if d1[k] != d2[k]:
        print({k:v} == {k:d1[k]})
        break
else:
    print({k:v},{k:d1[k]})

# for k in d2:
#     if k in d1:
#         print(111, k)



