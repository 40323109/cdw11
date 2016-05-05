# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag4_40323130 = Blueprint('ag4_40323130', __name__, url_prefix='/ag4_40323130', template_folder='templates')

# 展示傳回 Brython 程式
@ag4_40323130.route('/A')
def task1():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
   
    basic10 = cmbr.dup()
    basic10.rotate(0)
    basic10.translate(0, 20)
    
    basic11 = cmbr.dup()
    basic11.rotate(170)
    basic11.translate(0, 20)
    
    basic12 = cmbr.dup()
    basic12.rotate(165)
    basic12.translate(4, 40)
    
    basic13 = cmbr.dup()
    basic13.rotate(90)
    basic13.translate(9.5, 60)
    
    basic14 = cmbr.dup()
    basic14.rotate(197)
    basic14.translate(36, 40)
    
    basic15 = cmbr.dup()
    basic15.rotate(192)
    basic15.translate(40, 20)
    
    basic16 = cmbr.dup()
    basic16.rotate(0)
    basic16.translate(40, 20)
    
    basic17 = cmbr.dup()
    basic17.rotate(0)
    basic17.translate(40, 0)
    
    basic18 = cmbr.dup()
    basic18.rotate(90)
    basic18.translate(0, 0)
    
    basic19 = cmbr.dup()
    basic19.rotate(90)
    basic19.translate(20, 0)
    
    basic110 = cmbr.dup()
    basic110.rotate(0)
    basic110.translate(0, 0)
    
    basic20 = cmbr.dup()
    basic20.rotate(0)
    basic20.translate(60, 20)
    
    basic21 = cmbr.dup()
    basic21.rotate(170)
    basic21.translate(60, 20)
    
    basic22 = cmbr.dup()
    basic22.rotate(165)
    basic22.translate(64, 40)
    
    basic23 = cmbr.dup()
    basic23.rotate(90)
    basic23.translate(69.5, 60)
    
    basic24 = cmbr.dup()
    basic24.rotate(197)
    basic24.translate(96, 40)
    
    basic25 = cmbr.dup()
    basic25.rotate(192)
    basic25.translate(100, 20)
    
    basic26 = cmbr.dup()
    basic26.rotate(0)
    basic26.translate(100, 20)
    
    basic27 = cmbr.dup()
    basic27.rotate(0)
    basic27.translate(100, 0)
    
    basic28 = cmbr.dup()
    basic28.rotate(90)
    basic28.translate(60, 0)
    
    basic29 = cmbr.dup()
    basic29.rotate(90)
    basic29.translate(80, 0)
    
    basic210 = cmbr.dup()
    basic210.rotate(0)
    basic210.translate(60, 0)
    
    basic30 = cmbr.dup()
    basic30.rotate(0)
    basic30.translate(120, 20)
    
    basic31 = cmbr.dup()
    basic31.rotate(170)
    basic31.translate(120, 20)
    
    basic32 = cmbr.dup()
    basic32.rotate(165)
    basic32.translate(124, 40)
    
    basic33 = cmbr.dup()
    basic33.rotate(90)
    basic33.translate(129.5, 60)
    
    basic34 = cmbr.dup()
    basic34.rotate(197)
    basic34.translate(156, 40)
    
    basic35 = cmbr.dup()
    basic35.rotate(192)
    basic35.translate(160, 20)
    
    basic36 = cmbr.dup()
    basic36.rotate(0)
    basic36.translate(160, 20)
    
    basic37 = cmbr.dup()
    basic37.rotate(0)
    basic37.translate(160, 0)
    
    basic38 = cmbr.dup()
    basic38.rotate(90)
    basic38.translate(120, 0)
    
    basic39 = cmbr.dup()
    basic39.rotate(90)
    basic39.translate(140, 0)
    
    basic310 = cmbr.dup()
    basic310.rotate(0)
    basic310.translate(120, 0)
    
    basic40 = cmbr.dup()
    basic40.rotate(0)
    basic40.translate(180, 20)
    
    basic41 = cmbr.dup()
    basic41.rotate(170)
    basic41.translate(180, 20)
    
    basic42 = cmbr.dup()
    basic42.rotate(165)
    basic42.translate(184, 40)
    
    basic43 = cmbr.dup()
    basic43.rotate(90)
    basic43.translate(189.5, 60)
    
    basic44 = cmbr.dup()
    basic44.rotate(197)
    basic44.translate(216, 40)
    
    basic45 = cmbr.dup()
    basic45.rotate(192)
    basic45.translate(220, 20)
    
    basic46 = cmbr.dup()
    basic46.rotate(0)
    basic46.translate(220, 20)
    
    basic47 = cmbr.dup()
    basic47.rotate(0)
    basic47.translate(220, 0)
    
    basic48 = cmbr.dup()
    basic48.rotate(90)
    basic48.translate(180, 0)
    
    basic49 = cmbr.dup()
    basic49.rotate(90)
    basic49.translate(200, 0)
    
    basic410 = cmbr.dup()
    basic410.rotate(0)
    basic410.translate(180, 0)
    
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic110)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic210)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic310)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)
    cmbr.appendPath(basic44)
    cmbr.appendPath(basic45)
    cmbr.appendPath(basic46)
    cmbr.appendPath(basic47)
    cmbr.appendPath(basic48)
    cmbr.appendPath(basic49)
    cmbr.appendPath(basic410)

    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 0, 0, 0, 0, "green", True, 4)
</script>

<script type="text/python" src="/ag4_40323130/task1"></script>

</body>
</html>
'''
    return outstring
    
@ag4_40323130.route('/B')
def task2():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -4500, 5000, 5000) 

# 決定要不要畫座標軸線
#cgo.drawAxes(0, 5000, 0, 5000, {
#    "strokeColor":"#aaaaaa",
#   "fillColor": "#aaaaaa",
#    "xTickInterval": 20,
#    "xLabelInterval": 20,
#    "yTickInterval": 20,
#    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0, 20)
    
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0, 40)
    
    basic3 = cmbr.dup()
    basic3.rotate(90)
    basic3.translate(0, 0)
    
    basic4 = cmbr.dup()
    basic4.rotate(90)
    basic4.translate(20, 0)
    
    basic5 = cmbr.dup()
    basic5.rotate(0)
    basic5.translate(40, 0)
    
    basic6 = cmbr.dup()
    basic6.rotate(0)
    basic6.translate(40, 20)
    
    basic7 = cmbr.dup()
    basic7.rotate(0)
    basic7.translate(40, 40)
    
    basic8 = cmbr.dup()
    basic8.rotate(150)
    basic8.translate(0, 40)
    
    basic9 = cmbr.dup()
    basic9.rotate(210)
    basic9.translate(40, 40)
    
    basic10 = cmbr.dup()
    basic10.rotate(90)
    basic10.translate(20*math.cos(60*deg), (20*math.sin(60*deg)+40))
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(350, 0, 0, 0, 0, "lightgreen", True, 4)
'''
    return outstring
    

    
@ag4_40323130.route('/D')
def task4():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -4500, 5000, 5000) 

# 決定要不要畫座標軸線
#cgo.drawAxes(0, 5000, 0, 5000, {
#    "strokeColor":"#aaaaaa",
#   "fillColor": "#aaaaaa",
#    "xTickInterval": 20,
#    "xLabelInterval": 20,
#    "yTickInterval": 20,
#    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0, 20)
    
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0, 40)
    
    basic3 = cmbr.dup()
    basic3.rotate(90)
    basic3.translate(0, 0)
    
    basic4 = cmbr.dup()
    basic4.rotate(90)
    basic4.translate(20, 0)
    
    basic5 = cmbr.dup()
    basic5.rotate(0)
    basic5.translate(40, 0)
    
    basic6 = cmbr.dup()
    basic6.rotate(0)
    basic6.translate(40, 20)
    
    basic7 = cmbr.dup()
    basic7.rotate(0)
    basic7.translate(40, 40)
    
    basic8 = cmbr.dup()
    basic8.rotate(150)
    basic8.translate(0, 40)
    
    basic9 = cmbr.dup()
    basic9.rotate(210)
    basic9.translate(40, 40)
    
    basic10 = cmbr.dup()
    basic10.rotate(90)
    basic10.translate(20*math.cos(60*deg), (20*math.sin(60*deg)+40))
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(1050, 0, 0, 0, 0, "lightgreen", True, 4)
'''
    return outstring
    
