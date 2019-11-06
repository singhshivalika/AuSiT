import cv2
import speech_recognition as sr
import pygame as pg
global text 
text=''
r = sr.Recognizer()

dict_1={
      'a':'images/ASL/a.png',
      'b':'images/ASL/b.png',
      'c':'images/ASL/c.png',
      'd':'images/ASL/d.png',
      'e':'images/ASL/e.png',
      'f':'images/ASL/f.png',
      'g':'images/ASL/g.png',
      'h':'images/ASL/h.png',
      'i':'images/ASL/i.png',
      'j':'images/ASL/j.png',
      'k':'images/ASL/k.png',
      'l':'images/ASL/l.png',
      'm':'images/ASL/m.png',
      'n':'images/ASL/n.png',
      'o':'images/ASL/o.png',
      'p':'images/ASL/p.png',
      'q':'images/ASL/q.png',
      'r':'images/ASL/r.png',
      's':'images/ASL/s.png',
      't':'images/ASL/t.png',
      'u':'images/ASL/u.png',
      'v':'images/ASL/v.png',
      'w':'images/ASL/w.png',
      'x':'images/ASL/x.png',
      'y':'images/ASL/y.png',
      'z':'images/ASL/z.png',
      ' ':'images/ASL/SPACE.png'}

dict_2={
      'a':'images/BSL/a.png',
      'b':'images/BSL/b.jpg',
      'c':'images/BSL/c.jpg',
      'd':'images/BSL/d.jpg',
      'e':'images/BSL/e.jpg',
      'f':'images/BSL/f.jpg',
      'g':'images/BSL/g.jpg',
      'h':'images/BSL/h.jpg',
      'i':'images/BSL/i.jpg',
      'j':'images/BSL/j.jpg',
      'k':'images/BSL/k.jpg',
      'l':'images/BSL/l.jpg',
      'm':'images/BSL/m.jpg',
      'n':'images/BSL/n.jpg',
      'o':'images/BSL/o.jpg',
      'p':'images/BSL/p.jpg',
      'q':'images/BSL/q.jpg',
      'r':'images/BSL/r.jpg',
      's':'images/BSL/s.jpg',
      't':'images/BSL/t.jpg',
      'u':'images/BSL/u.jpg',
      'v':'images/BSL/v.jpg',
      'w':'images/BSL/w.jpg',
      'x':'images/BSL/x.jpg',
      'y':'images/BSL/y.jpg',
      'z':'images/BSL/z.jpg',
      ' ':'images/BSL/SPACE.png'}


dict_3={   
      'a':'images/ISL/a.jpg',
      'b':'images/ISL/b.jpg',
      'c':'images/ISL/c.jpg',
      'd':'images/ISL/d.jpg',
      'e':'images/ISL/e.jpg',
      'f':'images/ISL/f.jpg',
      'g':'images/ISL/g.jpg',
      'h':'images/ISL/h.jpg',
      'i':'images/ISL/i.jpg',
      'j':'images/ISL/j.jpg',
      'k':'images/ISL/k.jpg',
      'l':'images/ISL/l.jpg',
      'm':'images/ISL/m.jpg',
      'n':'images/ISL/n.jpg',
      'o':'images/ISL/o.jpg',
      'p':'images/ISL/p.jpg',
      'q':'images/ISL/q.jpg',
      'r':'images/ISL/r.jpg',
      's':'images/ISL/s.jpg',
      't':'images/ISL/t.jpg',
      'u':'images/ISL/u.jpg',
      'v':'images/ISL/v.jpg',
      'w':'images/ISL/w.jpg',
      'x':'images/ISL/x.jpg',
      'y':'images/ISL/y.jpg',
      'z':'images/ISL/z.jpg',
      ' ':'images/ISL/SPACE.png'}

choice=int(input("Choose Sign Language: 1-ASL, 2-BSL, 3-ISL => "))

if choice == 1:
    img_dict  = dict_1
elif choice ==2:
    img_dict  = dict_2
elif choice == 3:
    img_dict = dict_3

with sr.Microphone() as source:
    print('Speak Anything: ')
    print('speak now')
    audio = r.listen(source, phrase_time_limit=10)
    print('recording done')
    try:
        print('converting to text...')
        text=r.recognize_google(audio)
        text=text.lower()
        print("You said: {}".format(text))
    except:
        print('Sorry could not recognise your voice!!')

#ord=input('Please enter any word: ')



for i in text:
    #im = cv2.imread(dict_2[i])                              # Read image
    #im = cv2.resize(im, (960, 540))                   # Resize image
    #cv2.imshow("output", im)                          # Show image
    win = pg.display.set_mode((960,540))
    img = pg.transform.scale(pg.image.load(img_dict[i]),(960,540))
    win.blit(img, (0,0))
    pg.display.update()
    cv2.waitKey(500)

