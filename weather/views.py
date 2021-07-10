from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests
from requests.models import HTTPError
from weather.models import form


# Create your views here.
def top(request):
    return render(request, "top.html")

def gaiyou(request):
    return render(request, "gaiyou.html")

def form_get(request):
    return render(request, "form.html")

def toukou(request):
    if request.method =="POST":
        email_content = request.POST["email"]
        if email_content == "":
            email_content = "None"
        content = form(email = email_content, body = request.POST["body"])
        content.save()
        naiyou = {
            "thank": True,
        }
        return render(request, "form.html", naiyou)
    
    else:
        return render(request, "form.html")

def prefecture(request, article_id):
    id = str(article_id)
    with open("weather/area.json", "r", encoding="utf-8") as txt:
        txt_json = json.load(txt)
    
    result = txt_json[id]["city"]
    image = txt_json[id]["image"]
    l = []
    for a in result:
        l.append(a["city"])
    
    content = {
        "pref":txt_json[id]["name"],
        "citys":l,
        "test":image,
    }

    return render(request,"pref.html",content)

def select(request, article_id):
    content = {
        "city": str(article_id),
    }
    if str(article_id)[-1] == "市" or str(article_id)[-1] == "区":
        content["picture"] = "../static/picture/city.jpg"
    
    else:
        content["picture"] = "../static/picture/country.jpg"

    return render(request, "select.html", content)


def weather(request, article_id):
    if request.method == "POST":
        temp_yn = request.POST.get("temp_yn", False)
        wind_yn = request.POST.get("wind_yn", False)
        wind_d_yn = request.POST.get("wind_d_yn", False)
        clouds_yn = request.POST.get("clouds",False)
        times = request.POST.get("times", False)

        if times == False:
            return HttpResponse("時間を選択してください")

        elif int(times) < 0 or int(times) > 16:
            return HttpResponse("時間は1以上16以下でないといけません")

        id = str(article_id)
        #郵便番号取得
        txt = requests.get("http://zipcoda.net/api?address=" + id)
        txt_json = txt.json()
        zipcode = txt_json["items"][0]["zipcode"]

        #緯度経度取得
        res_dict = requests.get("http://geoapi.heartrails.com/api/json?method=searchByPostal&postal=" + zipcode).json()['response']['location'][0]
        x = res_dict["x"]
        y = res_dict["y"]

        #天気情報取得
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"
        querystring = {"lon":x, "lat":y}

        headers = {
            'x-rapidapi-key': "61f699f4e9mshe2b6b4590f00c5ep19dc30jsnab68d14dfd73",
            'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
            }



        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        day=data["data"]

        days = {}
        
        for n,h in enumerate(day):
            d = {}

            d["weather"] = day[n]["weather"]["description"]
            if temp_yn == "temp_y":
                d["min"] = day[n]["min_temp"]
                d["max"] = day[n]["high_temp"]
            
            if wind_yn == "wind_y":
                d["wind"] = day[n]["wind_spd"]
            
            if wind_d_yn == "wind_d_y":
                d["wind_dir"] = day[n]["wind_cdir_full"]
            
            if clouds_yn == "clouds_y":
                d["clouds"] = day[n]["clouds"]

            days[str(n + 1)] = d        

            if n + 1 == int(times):
                break


        return JsonResponse(days)
    return HttpResponse("ERROR")


def weather2(request, article_id):
    if request.method == "POST":
        temp_yn = request.POST.get("temp_yn2", False)
        wind_yn = request.POST.get("wind_yn2", False)
        wind_d_yn = request.POST.get("wind_d_yn2", False)
        clouds_yn = request.POST.get("clouds2",False)
        times = request.POST.get("times2", False)

        if times == False:
            return HttpResponse("時間を選択してください")

        elif int(times) < 0 or int(times) > 49:
            return HttpResponse("時間は1以上48以下でないといけません")
            
        id = str(article_id)
        #郵便番号取得
        txt = requests.get("http://zipcoda.net/api?address=" + id)
        txt_json = txt.json()
        zipcode = txt_json["items"][0]["zipcode"]

        #緯度経度取得
        res_dict = requests.get("http://geoapi.heartrails.com/api/json?method=searchByPostal&postal=" + zipcode).json()['response']['location'][0]
        x = res_dict["x"]
        y = res_dict["y"]

        #天気情報取得
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly"
        querystring = {"lon":x, "lat":y}

        headers = {
            'x-rapidapi-key': "61f699f4e9mshe2b6b4590f00c5ep19dc30jsnab68d14dfd73",
            'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
            }



        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        day=data["data"]

        days = {}
        
        for n,h in enumerate(day):
            d = {}

            d["weather"] = day[n]["weather"]["description"]
            if temp_yn == "temp_y":
                d["temp"] = day[n]["temp"]
            
            if wind_yn == "wind_y":
                d["wind"] = day[n]["wind_spd"]
            
            if wind_d_yn == "wind_d_y":
                d["wind_dir"] = day[n]["wind_cdir_full"]
            
            if clouds_yn == "clouds_y":
                d["clouds"] = day[n]["clouds"]

            days[str(n + 1)] = d        

            if n + 1 == int(times):
                break


        return JsonResponse(days)
    return HttpResponse("ERROR")