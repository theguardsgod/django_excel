from django import views
from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import (
    render, redirect, reverse, HttpResponse
)

from lenovo import models
from lenovo.utils import auth_code
from lenovo.forms import formAuth

# 用户登录视图类
class Login(views.View):
    def get(self, request):
        # get请求返回登录页面
        return render(request, "login.html")

    def post(self, request):
        data = request.POST
        # 获取用户登录信息
        authcode = data.get("authcode")
        username = data.get("username")
        password = data.get("password")

        # 验证码不正确
        if request.session.get("authcode").upper() != authcode.upper():
            print("qqq")
            return JsonResponse({"status": "1"})

        else:
            # 使用django的auth模块进行用户名密码验证
            user = auth.authenticate(username=username, password=password)
            if user:
                # 将用户名存入session中
                request.session["user"] = username
                print("sss")
                auth.login(request, user)  # 将用户信息添加到session中
                return JsonResponse({"status": "2"})
            else:
                print("aaa")
                return JsonResponse({"status": "3"})


# 验证码视图类
class GetAuthImg(views.View):
    """获取验证码视图类"""

    def get(self, request):
        data = auth_code.get_authcode_img(request)
        print("验证码：", request.session.get("authcode"))
        return HttpResponse(data)



# 注册视图类
class Register(views.View):
    def get(self, request):
        # 注册页面的生成我们并没有用form，因为我们使用的别人的模板样式
        return render(request, "register.html")

    def post(self, request):
        # post请求提交注册数据
        data = request.POST
        form_obj = formAuth.RegForm(data)  # 数据交给form实例化
        print("ddd")
        if form_obj.is_valid():  # 验证提交数据的合法性
            
            valid_data = form_obj.cleaned_data
            username = valid_data.get("username")
            phone = valid_data.get("phone")
            # 判断帐号是否已存在
            if models.UserInfo.objects.filter(username=username):
                # 如果存在，给form中的username字段添加一个错误提示。
                form_obj.add_error("username", "帐号已存在")
                return render(request, "register.html", {"form_obj": form_obj})
            elif models.UserInfo.objects.filter(phone=phone):
                # 如果存在，给form中的username字段添加一个错误提示。
                form_obj.add_error("phone", "电话已存在")
                return render(request, "register.html", {"form_obj": form_obj})
            else:
                # 帐号可用，去掉多余密码，在数据库创建记录
                del valid_data["r_password"]
                models.UserInfo.objects.create_user(**valid_data)  # 创建普通用户
                return redirect("login")
        else:
            print("数据不合法")
            # 数据验证不通过，返回页面和错误提示，保留数据
            return render(request, "register.html", {"form_obj": form_obj})