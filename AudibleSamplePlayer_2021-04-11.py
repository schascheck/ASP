import random, requests, json, vlc, webbrowser


with open("publishers_list.txt","r")as filehandle:
    publishers_list=json.load(filehandle)

#publishers_list.sort(key=len)

sum_samples=[]
print(f"{len(publishers_list)} Directories!")
for x in publishers_list:
    split=x.split("_")
    value=int(split[2])
    sum_samples.append(value)
print(f"{sum(sum_samples)} Samples available!")

count=0
while True:
    ans=input("Welcome to the Audible Sample Player! What would you like to try? rando(m), (c)ustom: ")
    if ans=="m" or ans=="M" or ans=="c" or ans=="C":
        break
x=True
while x:
    while True:
        if ans=="c" or ans=="C":
            for x in publishers_list:
                print(x)
            while True:
                print(f'What "Category_Publisher_Max Sample Number" would you like? Example: {publishers_list[-1]}')
                custom=input("Scroll up the list to find one, copy it, then paste it here: ")
                if custom in publishers_list:
                    split_custom=custom.split("_")
                    category=(split_custom[0])
                    publisher=(split_custom[1])
                    max_sample_number=(split_custom[2])
                    break
            while True:   
                    number=input("Choose the sample number you would like to listen to: ")
                    if 0<int(number)<=int(max_sample_number):
                        break
            break
        elif ans=="n" or ans=="N":
            number=str(int(number)+1)
            #print(number)
            break
        elif ans=="p" or ans=="P":
            number=str(abs(int(number)-1))
            #print(number)
            break
        elif ans=="m" or ans=="M":
            unsplit=random.choice(publishers_list)
            #print(unsplit)
            split=unsplit.split("_")
            #print(split)
            category=split[0]
            #print(category)
            publisher=split[1]
            #print(publisher)
            max_sample_number=split[2]
            #print(max_sample_number)
            number=str(random.randint(1,int(max_sample_number)))
            #print(number)
            break
    number_full=number.zfill(6)
    #print(number_full)
    mp3_url="https://samples.audible.com/"+category+"/"+publisher+"/"+number_full+"/"+category+"_"+publisher+"_"+number_full+"_sample.mp3"
    #print(mp3_url)
    exist=requests.get(mp3_url)
    code=(exist.status_code)
    #print(code)
    if code==200:
        count=0        
        history_value=(category+"_"+publisher+"_"+number_full)
        print("Now playing:")
        print(history_value)
        print('Type "a" and "enter" to search for this sample at Audible.com')
        with open("history.txt","r")as filehandle:
            history=json.load(filehandle)
        history.append(history_value)
        with open("history.txt","w")as filehandle:
            json.dump(history,filehandle)
        bfs=vlc.MediaPlayer(mp3_url)
        bfs.play()
        while True:
            ans=input("(a)udible, rando(m), (r)eplay, (n)ext +1, (p)revious -1, (c)ustom, e(x)it, enter = play/pause: ")
            #print(ans)
            if ans=="m" or ans=="M" or ans=="n" or ans=="N" or ans=="p" or ans=="P" or ans=="c" or ans=="C":
                bfs.stop()
                break
            elif ans=="r" or ans=="R":
                bfs.stop()
                bfs.play()    
            elif ans=="x" or ans=="X":
                bfs.stop()
                x=False
                break
            elif ans=="a" or ans=="A":
                webbrowser.open(f"https://www.audible.com/search?keywords={history_value}&ref=a_categories_t1_header_search")
            else:
                bfs.pause()
    else:
        print("That sample doesn't exist, let's try the next one")
        ans="n"
        count+=1
        if count>=10:
            while True:
                ans=input(f"Oops! You found {count} bad links in a row! Better try one of these options: rando(m), (c)ustom, e(x)it ")
                if ans=="m" or ans=="M" or ans=="c" or ans=="C" or ans=="x" or ans=="X":
                    break
            count=0
            if ans=="x" or ans=="X":
                x=False


            
            

                

    
    


    
        
