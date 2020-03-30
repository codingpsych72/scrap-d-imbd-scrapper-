import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import time
genere_req_page=requests.get('https://www.imdb.com/feature/genre/?ref_=nv_ch_gr')
#print(genere_req_page)
print(" ")
soupy_genere=BeautifulSoup(genere_req_page.text,'html.parser')
genere_name=soupy_genere.find(id="main")
genere_movie=genere_name.find(class_="ab_links")
genere_name_list=genere_movie.find_all('a')
print("Are you ready to search for Popular Movie by Genere")
print(' ')
print("\nCan I statrt fetching the genere for you :")
print("\n")
choice=input("Please enter -->yes<-- to continue -->no<-- to quit\n\n")
if choice=="yes":
   print("\nFetching the genere it takes only seconds........\n")
   for r in tqdm(range(100)):
       time.sleep(0.01)
elif choice=="quit":
    print("\nThank you see you later...")
    exit
print('\nThe genere available are:\n')
time.sleep(2)
for genere in genere_name_list:
   print(genere.contents[0],end="")
   print(' ')
select_genere=input("\nEnter the genere you are interested in:\t")
print("\nGenere choosen:{0}\t\t".format(select_genere))
print("\nFetching the list of movies in {0} category\n".format(select_genere.upper()))
movie_request_page=requests.get('https://www.imdb.com/search/title/?genres='+select_genere.lower()+'&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=RHJ4YYHY7XVT653KP8RX&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_1')
if (movie_request_page):
   print("Fetching Completed")
movie_request_parsed=BeautifulSoup(movie_request_page.text,"html.parser")
#print(movie_request_parsed)
remove1=movie_request_parsed.find(class_="loadlate")
remove1.decompose()
remove2=movie_request_parsed.find(class_="lister-item-image float-left")
remove2.decompose()
remove3=movie_request_parsed.find(class_="text-muted")
remove3.decompose()
remove4=movie_request_parsed.find(class_="ghost")
remove4.decompose()
remove7=movie_request_parsed.find(class_="starBarWidget")
remove7.decompose()
remove5=movie_request_parsed.find(class_="inline-block ratings-user-rating")
remove5.decompose()
remove6=movie_request_parsed.find(class_="rating-stars")
remove6.decompose()
movie_request_header=movie_request_parsed.find(class_="lister list detail sub-list")
#print(movie_request_header)
#print("@@@\n")
movie_request_moviename=movie_request_header.find_all("a")
name=[]
movie_heading_list=[]
for j in movie_request_moviename:
    name.append(str(j))
for k in name:
    if not("/register/login") in k and not("/name/nm") in k and not("class=\"loadlate\"") in k and not("rel=\"nofollow\"") in k:
        movie_heading_list.append(k)
        #print("\n")
        #print(type(k))
#print(movie_request_moviename)
#print(movie_heading_list)
splitted=[]
for l in movie_heading_list:
    splitted.append(l.split("\">"))
print("\n")
for o in splitted:
    o[0]=""
splitted_new=[]
for p in splitted:
    splitted_new.append(p[1:])
splitted_new1=[]
for q in splitted_new:
    splitted_new1.append(q[0].split("</a>"))
splitted_new2=[]
for r in splitted_new1:
    splitted_new2.append(r[0])
for s in tqdm(range(100)):
       time.sleep(0.01)
time.sleep(0.1)
print("\n")
for count,movie in enumerate(splitted_new2,1):
    print("{0}:::{1}".format(count,movie))
#print("@@@@@@@@@@@@@@@@@@@") 

    
    


