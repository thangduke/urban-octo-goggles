import requests
import json
# from tuya_connector import (
#     TuyaOpenAPI,
#     TuyaOpenPulsar,
#     TuyaCloudPulsarTopic,
#     TUYA_LOGGER,
# ) 

def getAPI():
    api_url =  "https://api.atmocube.app/v1/public/devices/1g8VOYn/latest_measurements/"
    headers = {
        "Authorization": "APIkey 645e951c29e5b80c1a56566823edc06327503ac9",  # Thay YOUR_API_KEY bằng khóa API của bạn
    }
    

    Access_ID = "va4kt7jufkgkpcnyyeax"
    Access_key = "47d58e66c351454a80a7ef96efd30332"
    API_Endpoint = "https://openapi.tuyaus.com"
    # Gửi yêu cầu GET đến API
    while True:
        response = requests.get(api_url,headers=headers)

        # Kiểm tra mã trạng thái của phản hồi
        if response.status_code == 200:
            # Lấy dữ liệu từ phản hồi
            data = response.json()
            print(data)
            # print("OKE:", response.status_code)
            # Kiểm tra cấu trúc dữ liệu để xác định làm thế nào để trích xuất thông số chất lượng không khí
            co2 = data.get("co2", {}) 
            pm10 = data.get("pm10", {})
            pm25 = data.get("pm25", {})
            iaqi = data.get("iaqi", {})
            t = data.get("temperature", {})
            h = data.get("humidity",())
            eiaqi = data.get("eiaqi",())
            avti = data.get("avti",())
            tci = data.get("tci",())
            pm1 = data.get("pm1",())
            ch2o = data.get("ch2o",())
            vocindex = data.get("vocindex",())
            noxindex = data.get("noxindex",())
            noise = data.get("noise",())
            light = data.get("light",())
            pm4 = data.get("pm4",())
            pressure = data.get("pressure",())
        header = {'Content-Type':'application/json', 'Authorization': 'Basic YWRtaW46', 'Host':'localhost'}
        logon = requests.get("http://localhost/WaWebService/Json/Logon",headers=header)
        #print(logon.text)

        taglist = requests.get("http://localhost/WaWebService/Json/TagList/TEST",headers=header)
        #print(taglist.text)

        #body = json.dumps({"tag":[{"Name":"pm25"}]})
        Getvalue_co2 = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/co2/ %f" %co2 ,headers=header)
        Getvalue_pm10 = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/pm10/ %f" %pm10 ,headers=header)
        Getvalue_pm25 = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/pm25/ %f" %pm25 ,headers=header)
        Getvalue_iaqi = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/iaqi/ %f" %iaqi ,headers=header)
        Getvalue_t = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/t/ %f" %t ,headers=header)
        Getvalue_h = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/h/ %f" %h ,headers=header)
        # Getvalue_eiaqi = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/eiaqi/ %f" %eiaqi ,headers=header)
        # Getvalue_avti = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/avti/ %f" %avti ,headers=header)
        # Getvalue_tci = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/tci/ %f" %tci ,headers=header)
        # Getvalue_pm1 = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/pm1/ %f" %pm1 ,headers=header)
        
        # Getvalue_ch2o = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/ch2o/ %f" %ch2o ,headers=header)
        Getvalue_vocindex = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/vocindex/ %f" %vocindex ,headers=header)
        # Getvalue_noxindex = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/noxindex/ %f" %noxindex ,headers=header)
        # Getvalue_noise = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/noise/ %f" %noise ,headers=header)
        # Getvalue_light = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/light/ %f" %light ,headers=header)
        # Getvalue_pm4 = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/pm4/ %f" %pm4 ,headers=header)
        # Getvalue_pressure = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/pressure/ %f" %pressure ,headers=header)
        print(Getvalue_co2.text)
 getAPI()       
        
#         #####
#         openapi = TuyaOpenAPI(API_Endpoint,Access_ID,Access_key)
#         openapi.connect()
#         Air = "eb18cdbde15788a33cbrr0"
#         #/v1.0/iot-03/devices/xxxxId/status
#         response = openapi.get("/v1.0/iot-03/devices/{}/status".format(Air))
#         print(response)
#         air_pm25 = response['result'][1]['value']
#         air_temp = response['result'][9]['value']
#         air_humidity = response['result'][10]['value']
#         air_tvoc = response['result'][11]['value']
#         air_quality = response['result'][16]['value']
#         air_filter = response['result'][4]['value']
#         air_fan = response['result'][3]['value']
#         air_anion = response['result'][5]['value']
#         air_uv = response['result'][6]['value']
#         air_wet = response['result'][7]['value']
        
#         if air_quality == "great":
#             air_quality_f = 1
#         elif air_quality == "mild":
#             air_quality_f = 2
#         elif air_quality == "good":
#             air_quality_f = 3
#         elif air_quality == "medium":
#             air_quality_f = 4
#         elif air_quality == "sereve":
#             air_quality_f = 5
        
#         if air_fan == "high":
#             air_fan_f = 1
#         elif air_fan == "mid":
#             air_fan_f = 2
#         elif air_fan == "low":
#             air_fan_f = 3
#         elif air_fan == "sleep":
#             air_fan_f = 4
            
#         if air_uv == True:
#             uv_f = 1
#         else:
#             uv_f = 0
        
#         if air_anion == True:
#             anion_f = 1
#         else:
#             anion_f = 0
            
#         if air_wet == True:
#             wet_f = 1
#         else:
#             wet_f = 0  
              
#         Getvalue_air_pm25 = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_pm25/ %f" %air_pm25,headers=header)
#         Getvalue_air_temp = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_temp/ %f" %air_temp,headers=header)
#         Getvalue_air_humidity = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_humi/ %f" %air_humidity,headers=header)
#         Getvalue_air_tvoc = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_tvoc/ %f" %air_tvoc,headers=header)
#         Getvalue_air_quality = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_quality/ %f" %air_quality_f,headers=header)
#         Getvalue_air_filter = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_filter/ %f" %air_filter,headers=header)
#         Getvalue_air_fan = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_tt_fan/ %f" %air_fan_f,headers=header)
#         Getvalue_air_anion = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_tt_ion/ %f" %anion_f,headers=header)
#         Getvalue_air_uv = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_tt_uv/ %f" %uv_f,headers=header)
#         Getvalue_air_wet = requests.get("http://localhost/WaWebService/Json/SetTagValue/TEST/Air_tt_wet/ %f" %wet_f,headers=header)
        
        
        
#         commands = {"commands":[{"code":"anion","value": True}]}
#         send = openapi.post("/v1.0/iot-03/devices/{}/commands".format(Air),commands)
#         if pm25>50 or air_tvoc>50:
#             commands = {"commands":[{"code":"fan_speed_enum","value":"high"}]}
#             send = openapi.post("/v1.0/iot-03/devices/{}/commands".format(Air),commands)  ``
#         else:
#             commands = {"commands":[{"code":"fan_speed_enum","value":"low"}]}
#             send = openapi.post("/v1.0/iot-03/devices/{}/commands".format(Air),commands)
