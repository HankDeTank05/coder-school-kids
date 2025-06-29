pico-8 cartridge // http://www.pico-8.com
version 42
__lua__
-- and vs or

function _init()
	a=false
	b=false
	a_and_b = a and b
	a_or_b = a or b
end

function _update()
	if btnp(🅾️) then
		a = not a
	end
	if btnp(❎) then
		b = not b
	end
	a_and_b = a and b
	a_or_b = a or b
end

function _draw()
	cls()
	
	local r2y=8
	
	local ax=0
	print("a",ax,0,7)
	if a then
		print(a,ax,r2y,11)
	else
		print(a,ax,r2y,8)
	end
	
	-- vert line btwn col a/b
	local vlx=22
	line(vlx,0,vlx,r2y+4,7)
	
	local bx=26
	print("b",bx,0,7)
	if b then
		print(b,bx,r2y,11)
	else
		print(b,bx,r2y,8)
	end
	
	-- vert line btwn col b/and
	vlx=48
	line(vlx,0,vlx,r2y+4,7)
	
	local andx=52
	print("a and b",andx,0,7)
	if a_and_b then
		print(a_and_b,andx,r2y,11)
	else
		print(a_and_b,andx,r2y,8)
	end
	
	-- vert line btwn col and/or
	vlx=82
	line(vlx,0,vlx,r2y+4,7)
	
	local orx=85
	print("a or b",orx,0,7)
	if a_or_b then
		print(a_or_b,orx,r2y,11)
	else
		print(a_or_b,orx,r2y,8)
	end
end
-->8
--draw table

function draw_table(tbl)
	--column labels are keys
	local col_width={}
	for k,v in pairs(tbl) do
		add(col_width,#k)
	end
end
__gfx__
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
