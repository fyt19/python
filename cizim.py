import turtle

pen=turtle.Turtle()
pen.pencolor("red")
pen.pensize(3)
#şimdide bir 3gen çizelim


for a in range(3):
    pen.forward(50)
    pen.left(120)
turtle.done()

'''
burada yaptıklarımız;
pen diye bir degisken atadik 
sonra bu pen in rangini atadik
pen boyunu ayarladık
sonra dongude range ettik a 4 degerine gelene kadar
bu for dongusu devam edicek
left derken kalemin oradaki yaptigi aci 
her seferinde 90 derece sola dogru aci ile donuyor
islemlerimiz bu kadar

beni izlediginiz için tesekkür ederim
'''
