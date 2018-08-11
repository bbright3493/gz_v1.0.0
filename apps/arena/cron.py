# _*_ encoding:utf-8 _*_



from users.models import UserAchievement, UserProfile, ClassInfo, CityInfo
from django.utils import timezone


def my_scheduled_job():
    """
    定期执行任务
    每天23：59分进行日排行更新 班级范围内排序
    检查是否是周一 如果是周一 进行周排行更新  城市范围内更新
    检查是否是每月的一号 如果是 进行总排行更新  全国范围内更新
    :return:
    """
    #遍历所有班级
    classes = ClassInfo.objects.all()
    for one_class in classes:
        #查询该班级的所有学生
        students = one_class.get_students()
        #依据积分对学生进行排序
        order_students = students.order_by('score')
        #更新名次信息
        for rank, stu in enumerate(order_students):
            rank_user = UserAchievement.objects.get(user=stu)
            rank_user.class_rankings = rank

    #判断是否是星期一
    now = timezone.now()
    if now.isoweekday()==1:
        #查询所有城市信息
        cities = CityInfo.objects.all()
        for city in cities:
            students = city.get_students()
            # 依据积分对学生进行排序
            order_students = students.order_by('score')
            # 更新名次信息
            for rank, stu in enumerate(order_students):
                rank_user = UserAchievement.objects.get(user=stu)
                rank_user.monthly_rankings = rank

    #判断是否是每个月的一号
    if now.day==1:
        students = UserProfile.objects.all()
        order_students = students.order_by('score')
        # 更新名次信息
        for rank, stu in enumerate(order_students):
            rank_user = UserAchievement.objects.get(user=stu)
            rank_user.total_ranking = rank


