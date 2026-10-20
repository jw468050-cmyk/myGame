def setup():
    size(2000,1300)
    global wp,rgp,mainbg,cannon,page,cx,cy,bullet,bx,by,fire,monster1,score,monster2
    global bulletx,bullety,monster1x,monster1y,start1,monster2x,monster2y,fireball,fireballx,firebally
    global monster2LastShotTime,life,heart,deathpage,bosslife,bossx,bossy,boss,bossAttack,btx,bty
    global start2,startTime5,attackDirect,lastShotTime,winpage,shop,pauseStartTime,loadTime,doublebullet
    global none1, none2, none3,none4,cspeed,bomb,numbomb,bombx,bomby
    cspeed=15
    doublebullet=False
    lastShotTime=0
    monster2LastShotTime=[]
    wp=loadImage("startpage.png")
    rgp=loadImage("game rules.png")
    mainbg=loadImage("background.jpg")
    cannon=loadImage("cannon.png")
    bullet=loadImage("bullet.png")
    monster1=loadImage("monster2.png")
    monster2=loadImage("monster1.png")
    fireball=loadImage("fireball.png")
    deathpage=loadImage("deathpage.png")
    boss=loadImage("boss.png")
    bossAttack=loadImage("attack2.png")
    winpage=loadImage("winpage.png")
    shop=loadImage("shop.png")
    bomb=loadImage("bomb.png")
    loadTime=1.5
    page=1
    cx=1000-190
    cy=1300-250 
    bx=cx+200
    by=cy+100
    bulletx=[]
    bullety=[]
    start1=True
    monster1x=[]
    monster1y=[]
    monster2x=[]
    monster2y=[]
    score=0
    fireballx=[]
    firebally=[]
    life=7
    heart=loadImage("heart.png")
    bosslife=50
    bossx=800
    bossy=150
    btx=[]
    bty=[]
    start2=True
    attackDirect=[]
    pauseStartTime=0
    numbomb=1
    none1=True
    none2=True
    none3=True
    none4=True
    bombx=[]
    bomby=[]

def draw():
    global monster1x,monster1y,bulletx,bullety,score,monster2x,monster2y,monster2LastShotTime
    global page,cx,cy,startTime,start1,startTime2,startTime3,startTime4,fireballx,firebally,life
    global start2,startTime5,startTime6,bosslife,boss,bossx,bossy,loadTime
    
    if page==7:
        image(shop,0,0,width,height)
        fill(255)
        textSize(100)
        text(score, 900, 1200)
        return

    if page==1:
        image(wp,0,0,width,height)
        
    if page==2:
        image(rgp,0,0,width,height)
        
    if page==3:
        image(mainbg,0,0,width,height)
        image(cannon,cx,cy,400,400)
        
        image(bomb,200,1150,100,100)
        
        
        textSize(50)
        fill(255)
        text("LIFE:",1400,90)
        text(":"+str(numbomb),300,1220)
        
        for i in range(life):
            image(heart,1500+i*60,15,130,130)
            
        if start1:
            startTime=millis()
            startTime2=millis()
            startTime3=millis()
            startTime4=millis()
            start1=False
            
        lose()
            
        
        textSize(60)
        fill(255)
        text("Points:"+str(score),50,70)
        
        firebomb()
        
        for i in range(len(bulletx)):
            image(bullet,bulletx[i],bullety[i],200,200)
            bullety[i]-=120
            if bullety[i]<=-200:
                bullety.pop(i)
                bulletx.pop(i)
                break
        
        if ((millis()-startTime2)/1000)>2:
            monster1x.append(random(200,1800))
            monster1y.append(200)
            startTime2=millis()
            
        for i in range(len(monster1x)-1,-1,-1):
            image(monster1,monster1x[i],monster1y[i],200,200)
            monster1y[i]+=10
            if monster1y[i]==1100:
                monster1x.pop(i)
                monster1y.pop(i)
                life-=1
                
                
            
        for i in range(len(bulletx)-1,-1,-1):
            for j in range(len(monster1x)-1,-1,-1):
                if bulletx[i]<monster1x[j]+200 and bulletx[i]+200>monster1x[j] and bullety[i]+200>monster1y[j] and bullety[i]<monster1y[j]+200:
                    bulletx.pop(i)
                    bullety.pop(i)
                    monster1x.pop(j)
                    monster1y.pop(j)
                    score+=1
                    break
                
        
        if ((millis()-startTime)/1000)>30:
            if ((millis()-startTime3)/1000)>4:
                monster2x.append(random(200,1800))
                monster2y.append(200)
                startTime3=millis()
                monster2LastShotTime.append(millis())  
                            
        for i in range(len(monster2x)):
            image(monster2,monster2x[i],monster2y[i],200,200)

            if(millis() - monster2LastShotTime[i]) / 1000 > 6:
                    fireballx.append(monster2x[i] + 100)
                    firebally.append(monster2y[i] + 200)
                    monster2LastShotTime[i] = millis()

            
        for i in range(len(fireballx)-1, -1, -1):
            image(fireball, fireballx[i], firebally[i], 100, 100)
            firebally[i] += 20
  
            if firebally[i] > height:
                fireballx.pop(i)
                firebally.pop(i)
                
        for i in range(len(bulletx)-1,-1,-1):
            for j in range(len(monster2x)-1,-1,-1):
                if bulletx[i]<monster2x[j]+200 and bulletx[i]+200>monster2x[j] and bullety[i]+200>monster2y[j] and bullety[i]<monster2y[j]+200:
                    bulletx.pop(i)
                    bullety.pop(i)
                    monster2x.pop(j)
                    monster2y.pop(j)
                    score+=2
                    break
                
        for i in range(len(fireballx)-1,-1,-1):
            if fireballx[i]<cx+300 and fireballx[i]>cx and firebally[i]+100>cy+80 and firebally[i]<cy+400:
                fireballx.pop(i)
                firebally.pop(i)
                life-=1
                break
        
        
        if ((millis()-startTime)/1000)>=200:
            page=5
        
    if page==4:
        image(deathpage,0,0,width,height)
        textSize(80)
        fill(255)
        text("PLAY",400,900)
        text("EXIT",1460,900)  
        
        
    if page==5:
        
        if start2:
            startTime5=millis()
            startTime6=millis()
            start2=False
            
        
        
        image(mainbg,0,0,width,height)
        image(cannon,cx,cy,400,400)
        image(bomb,200,1150,100,100)
        
        textSize(50)
        fill(255)
        text("LIFE:",1400,90)
        text(":"+str(numbomb),300,1220)
        
        textSize(60)
        fill(255)
        text("BOSS'S LIFE:"+str(bosslife),700,90)
        
        lose()
        
        for i in range(life):
            image(heart,1500+i*60,15,130,130)
            
        for i in range(len(bulletx)):
            image(bullet,bulletx[i],bullety[i],200,200)
            bullety[i]-=80
            if bullety[i]<=-200:
                bullety.pop(i)
                bulletx.pop(i)
                score-=1
                break
        
        
        if (millis()-startTime5)/1000>4:
            bossx=random(400,width-400)
            startTime5=millis()
        
        image(boss,bossx,bossy,400,400)
        
        attack()
        
        for i in range(len(btx)-1,-1,-1):
            if btx[i]<cx+200 and btx[i]>cx and bty[i]+100>cy+80 and bty[i]<cy+400:
                btx.pop(i)
                bty.pop(i)
                life-=1
                break
        
        for i in range(len(bulletx)):
            if bulletx[i]<=bossx+400 and bulletx[i]+200>=bossx and bullety[i]+200>=bossy and bullety[i]<=bossy+300:
                bulletx.pop(i)
                bullety.pop(i)
                bosslife-=1
                break
            
        if bosslife<=0:
            win()
        
    if page==6:
        image(winpage,0,0,width,height)
        textSize(80)
        fill(255)
        print(mouseX,mouseY)
        
        
def keyPressed():
    global page,cx,cy,bulletx,bullety,lastShotTime,pauseStartTime,loadTime,numbomb
    if page==2:
        page=3
    if page==1:
        page=2
        
    if page==3 or page==5:
        if keyCode==LEFT:
            cx-=cspeed
        if keyCode==RIGHT:
            cx+=cspeed
        if key==" ":
            if (millis()-lastShotTime)/1000>=loadTime:
                bulletx.append(cx+80)
                bullety.append(cy-50)
                if doublebullet:
                    bulletx.append(cx+100)
                    bullety.append(cy-50)
                lastShotTime=millis()
        if (page==3 or page==5) and key=="s" or key=="S": 
            page=7
            pauseStartTime = millis()
            
        if (key=="g" or key=="G") and numbomb>0:
            bombx.append(cx+150)
            bomby.append(cy-50)
            numbomb-=1
            
            

            
        
            
def mousePressed():
    global page,life,paused,pauseStartTime,startTime,startTime2,startTime3,startTime4,startTime5,startTime6,lastShotTime,monster2LastShotTime,loadTime,doublebullet,score,none1,none2,none3,cspeed
    global none4,numbomb
    if page==4:
        if 370<=mouseX<=620 and 770<=mouseY<=970:
            setup()
        if 1420<=mouseX<=1680 and 770<=mouseY<=970:
            exit()   
    if page==6:
       if 320<=mouseX<=830 and 780<=mouseY<=930:
           setup()
       if 1160<=mouseX<=1670 and 780<=mouseY<=930:
           exit()
    
    if page==7:
        if 1640<=mouseX<=1780 and 570<=mouseY<=642:
            if none1 and score>=15:
                loadTime-=1
                none1=False
                score-=15
        if 1050<=mouseX<=1190 and 910<=mouseY<=994:
            if life<7 and score>=15:        
                life+=1 
                score-=15
        if 1056<=mouseX<=1185 and 262<=mouseY<=339:
            if none3 and score>=15:
                score-=15
                doublebullet=True  
                none3=False  
        if 1060<=mouseX<=1190 and 605<=mouseY<=685:
            if none4 and score>=15:
                score-=15
                cspeed+=5
                none4=False
        
        if 1643<=mouseX<=1762 and 198<=mouseY<=275 and score>=10:
            score-=10
            numbomb+=1

                
        if 1700<=mouseX<=2000 and 1000<=mouseY<=1300:
            page=3
            pausedDuration = millis() - pauseStartTime
            startTime += pausedDuration
            startTime2 += pausedDuration
            startTime3 += pausedDuration
            startTime4 += pausedDuration
            lastShotTime += pausedDuration
            for i in range(len(monster2LastShotTime)):
                monster2LastShotTime[i] += pausedDuration
                
                        
            
def lose():
    global page
    if life<=0:
        page=4

def attack():
    global startTime6,life
    if ((millis()-startTime6)/1000)>5:
        for i in range(3):
            btx.append(bossx+200)
            bty.append(bossy+200)
            attackDirect.append([random(20,50),random(10,30),int(random(0,2))])
        startTime6=millis()
            
    for i in range(len(btx)-1,-1,-1):
        image(bossAttack,btx[i],bty[i],100,60)
    
        if attackDirect[i][2]==1:
            btx[i]+=attackDirect[i][0]
            bty[i]+=attackDirect[i][1]
            if btx[i]<=120:
                btx[i]=120
                attackDirect[i][0]*=-1
            if btx[i]+100>=width-120:
                btx[i]=width-220
                attackDirect[i][0]*=-1
            if bty[i]>=height-100:
                btx.pop(i)
                bty.pop(i)
                
        if attackDirect[i][2]==0:
            btx[i]-=attackDirect[i][0]
            bty[i]+=attackDirect[i][1]
            if btx[i]<=120:
                btx[i]=120
                attackDirect[i][0]*=-1
            if btx[i]+100>=width-120:
                btx[i]=width-220
                attackDirect[i][0]*=-1
            if bty[i]>=height-100:
                btx.pop(i)
                bty.pop(i)
                
def win():
    global page
    page=6
    
def firebomb():
    global bombx, bomby, numbomb,score
    for i in range(len(bombx)-1,-1,-1):
        image(bomb,bombx[i],bomby[i],100,100)
        bomby[i]-=40
        
        if bomby[i] < -100:
            bombx.pop(i)
            bomby.pop(i)
            continue
        
        if bomby[i] <450:
            for j in range(len(monster1x)-1, -1, -1):
                    distance = dist(bombx[i]+50, bomby[i]+50, monster1x[j]+100, monster1y[j]+100)
                    if distance < 600:
                        monster1x.pop(j)
                        monster1y.pop(j)
                        score += 1
                        
            for j in range(len(monster2x)-1, -1, -1):
                    distance = dist(bombx[i]+50, bomby[i]+50, monster2x[j]+100, monster2y[j]+100)
                    if distance < 600:
                        monster2x.pop(j)
                        monster2y.pop(j)
                        score += 1
                    
            bombx.pop(i)
            bomby.pop(i)
            break

        
        
    
            
     
            
                
            
