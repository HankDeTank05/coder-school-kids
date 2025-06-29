pico-8 cartridge // http://www.pico-8.com
version 42
__lua__
function _init()
	px=64
	py=64
	help=true
	u=false
	d=false
	l=false
	r=false
end

function _update()
	u=btn(⬆️)
	if u then
		py-=1
	end
	
	d=btn(⬇️)
	if d then
		py+=1
	end
	
	l=btn(⬅️)
	if l then
		px-=1
	end
	
	r=btn(➡️)
	if r then
		px+=1
	end
	
	if btnp(❎) then
		help=not help
	end
end

function _draw()
	cls()
	
	--[[
	--draw axis lines
	
	--x-axis is red
	print("x-axis",10,5,8)
	line(0,0,127,0,8)
	
	--y-axis is green
	print("y-axis",5,10,11)
	line(0,0,0,127,11)
	--]]
	
	--draw points on the screen
	
	--top-left corner
	point(0,0,12)
	
	--top-right corner
	point(127,0,12)
	
	--bottom-left corner
	point(0,127,12)
	
	--bottom-right corner
	point(127,127,12)
	
	--movable point
	
	if help then
		pset(px,py,12)
		
		local ucol,dcol,lcol,rcol
		if u then ucol=7 else ucol=5 end
		if d then dcol=7 else dcol=5 end
		if l then lcol=7 else lcol=5 end
		if r then rcol=7 else rcol=5 end
		print("⬆️",px-3 ,py-10,ucol)
		print("⬇️",px-3 ,py+6 ,dcol)
		print("⬅️",px-12,py-2 ,lcol)
		print("➡️",px+6 ,py-2 ,rcol)
	else
		point(px,py,12)
	end
	
	--help text
	local htext="press ❎ to toggle help"
	print(htext,64-(4*#htext/2),110,14)
end
-->8
--point-drawing functions

function point(px,py,colr)
	--text padding from screen edge
	local pad=1
	--text to print
	local label="("..px..","..py..")"
	--[[
	if this rect overlaps anything
	then reposition it until it
	doesn't overlap any others
	--]]
	local lrect={
		x=px+2,
		y=py+2,
		w=#label*4,
		h=5,
	}
	
	--adjust if text goes
	--off-screen
	
	--left
	while lrect.x<0+pad do
		lrect.x+=1
	end
	
	--right
	while lrect.x+lrect.w-1>127-pad do
		lrect.x-=1
	end
	
	--top
	while lrect.y<0+pad do
		lrect.y+=1
	end
	
	--bottom
	while lrect.y+lrect.h-1>127-pad do
		lrect.y-=1
	end
	
	--point text background
	--(for readability)
	rectfill(lrect.x,lrect.y,
	lrect.x+lrect.w-1,
	lrect.y+lrect.h-1,0)
	
	--point text
	print(label,
	lrect.x,lrect.y,colr)
	
	--point background
	--(for contrast)
	rectfill(px-1,py-1,px+1,py+1,0)
	
	--the point itself
	pset(px,py,colr)
end
__gfx__
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
