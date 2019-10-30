#coding=UTF-8
import pandas as pd

'''
利用python的切片语法，通过查看每个DataFrame的前几行验证一下数据加载工作是否一切顺利

'''
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('.\\ml-1m\\users.dat',sep='::',header=None,names=unames,engine = 'python')
print(users[:5])

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('.\\ml-1m\\ratings.dat', sep='::', header=None, names=rnames,  engine='python')
print(ratings[:3])


mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('.\\ml-1m\\movies.dat', sep='::', header=None, names=mnames,  engine='python')
print(movies[:4])
print('==========分割线==========')
'''
利用python中的merge函数将ratings跟users合并到一起，然后再将movies也合并进去
并查看合并后的第一行数据
'''
data = pd.merge(pd.merge(ratings,users),movies)
print(data.ix[0])

print('==========分割线==========')
'''
现在只要熟悉一下pandas，就能轻松地根据任意个用户或电影属性对评分数据进行聚合操作了。
为了按性别计算每部电影的平均得分，我们用pivot_table方法
'''
mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
print(mean_ratings[:5])
print('==========分割线==========')


'''
现在打算过滤掉评分数据不足250条的电影，为了达到这个目的，先对title进行分组，然后利用size()得到一个含有
各电影分组大小的Series对象
'''
ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])

active_titles = ratings_by_title.index[ratings_by_title >= 250]
# print active_titles
#将评分数据超过250条的电影按照男女评分
mean_ratings = mean_ratings.ix[active_titles]
print(mean_ratings)

'''
为了了解女性观众最喜欢的电影，我们可以对F列降序排列
'''
top_female_ratings = mean_ratings.sort_values(by='F',ascending=False)
print("女性观众最喜欢的10部电影")
print(top_female_ratings[:10])

'''
假设我们想找出男性和女性观众分歧最大的电影，一个办法是给出mean_ratings加上
一个用于存放平均得分之差的列，并对其进行排序
'''
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:10])
#对结果反序并取出前15行，得到的则是男性观众更喜欢的电影
print(sorted_by_diff[::-1][:15])
'''
如果只是想找出分歧最大的电影(不考虑性别因素),则可以计算得分数据的方差或标准差
'''
#根据电影名称分组的得分数据的标准差
rating_std_by_title = data.groupby('title')['rating'].std()
# #根据active_titles进行过滤
rating_std_by_title = rating_std_by_title.ix[active_titles]
# #根据值对Series进行降序排列
print(rating_std_by_title.sort_values()[-10:])
