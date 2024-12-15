import os, sys,time 
try:
  from faker import Faker
  from requests import session
  import requests, random, re
  from random import randint
  import concurrent.futures
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  from faker import Faker
  from requests import session
  import requests, random, re
  from random import randint
  import concurrent.futures


def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()
def checkvalid():
  print ('')
  print ('             \033[1;34m[ \033[1;37mTool Facebook \033[1;34m]')
  print ('')
  try:
    print ("\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;93m LƯU Ý :")
    print ("\033[1;93m•KHÔNG HỖ TRỢ ĐỊNH DẠNG MAIL|PASS")
    print ("\033[1;93m•TOOL CHẠY ĐA LUỒNG ĐỒNG NGHĨA VỚI IP CỦA BẠN SẼ DỄ BỊ FB BLOCK HƠN")
    print ("\033[1;93m•VUI LÒNG FAKE IP TRƯỚC CHẠY TOOL NÀY")
    print ("\033[1;93m•MỖI IP CHECK ĐƯỢC 50-80 MAIL RỒI ĐỔI IP KHÁC")
    print("\033[1;31m────────────────────────────────────────────────────────────")
    fileEmail = open(input("\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;32mNhập File Chứa Email(ex: email.txt) : \033[1;37m")).readlines()
    valid = input("\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;32mNhập File Lưu Email Valid Facebook(ex: validfb.txt) : \033[1;37m")
    print("\033[1;31m────────────────────────────────────────────────────────────")
  except:
    print (" \033[1;31mKHÔNG TÌM THẤY FILE BẠN ĐÃ NHẬP !")
    quit()
  list_email_fb = []
  for line_email_fb in fileEmail:
    email_fb = line_email_fb.strip("\n")
    list_email_fb.append(email_fb)
  link1='https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0'
  h1={
          'Accept': '*/*',
          'Pragma': 'no-cache',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
  }
          
  ses=requests.Session()
  get_data=ses.get(link1,headers=h1)
  cookie=get_data.cookies.get_dict()['datr']
  get_data = get_data.text
  lsd=get_data.split('"lsd" value="')[1].split('"')[0]
  jazoest=get_data.split('"jazoest" value="')[1].split('"')[0]
  def run_check_valid(emailfb):
    data = f'lsd={lsd}&jazoest={jazoest}&email={emailfb}&did_submit=Rechercher'
          
    link2='https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0'
          
    h2={
              'Accept': 'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*',
              'Referer': 'https://m.facebook.com/login/identify/?ctx=recover&search_attempts=2&ars=facebook_login&alternate_search=0&toggle_search_mode=1',
              'Accept-Language': 'fr-FR,fr;q=0.8,ar-DZ;q=0.5,ar;q=0.3',
              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729',
              'Host': 'm.facebook.com',
              'Connection': 'Keep-Alive',
              'Cache-Control': 'no-cache',
              'Cookie':f'datr={cookie}',
              'Content-Length': '84',
  }
          
    check = requests.post(link2,headers=h2,data=data).text
    #cc = check.split('Votre recherche ne donne aucun résultat')
    kq_check = re.search("Votre recherche ne donne aucun résultat", check)
    if kq_check == None:
      print ("\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;37m| \033[1;31mCó Liên Kết \033[1;37m| "  +  emailfb)
      open(valid,"a").write(emailfb + "\n")
    else:
      print ("\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;37m| \033[1;32mKhông Liên Kết \033[1;37m| "  + emailfb)
  with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_check_valid, list_email_fb)


def clr():return f'\033[{random.randint(91,96)}m'

def logo():
  logo = """
                    
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;33mTool Check Valid
\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36m NGUYỄN DUY KHÁNH 
\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;32mBOX ZALO: \033[1;37m https://zalo.me/g/nguadz335
\033[1;31m────────────────────────────────────────────────────────────
"""
  for pr in logo:sys.stdout.write(pr);sys.stdout.flush();time.sleep(0.001)
  choice_user = input("\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;32mNhập \033[1;33m1+1 \033[1;32mLà: \033[1;37m")
  if choice_user == '2':
    clear()
    checkvalid()
  if choice_user == '3':
    clear()
    Print (" Chúc Bạn 1 Ngày Vui Vẻ.")
    quit()
logo() 
