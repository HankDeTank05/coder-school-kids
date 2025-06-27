pico-8 cartridge // http://www.pico-8.com
version 42
__lua__

function _init()
	list={}
	size=126
	for i=1,size do
		add(list, flr(rnd(size*4))+1)
	end
	qsort(list)
	timer_max=30
	timer=timer_max
	
	target_i=flr(rnd(#list))+1
	target=list[target_i]
	l=1
	r=size
	p=flr((l+r)/2)
	times=0
	prev={}
end

function _update()
	if timer>0 then
		timer-=1 --run down the timer
	elseif timer==0 then
		add(prev,{l=l,r=r,p=p,ti=target_i})
		--reset the timer to max
		timer=timer_max
		--update the l/r/p's
		if target>list[p] then
			l=p+1
			times+=1
		elseif target<list[p] then
			r=p-1
			times+=1
		else
			timer=-1
		end
		assert(l<=r)
		p=flr((l+r)/2)
		assert(l<=p)
		assert(p<=r)
	end
end

function _draw()
	cls()
	
	--draw previous runs
	for run_y=1,#prev do
		--draw the list as a line
		--where each pixel is an item
		--gray=not in search range
		--white=is in search range
		for i=1,#list do
			if i<prev[run_y].l or i>prev[run_y].r then
				pset(i,run_y,5)
			else
				pset(i,run_y,13)
			end
		end
		
		--draw the target pos as a
		--red pixel
		pset(prev[run_y].ti,run_y,2)
		
		--draw the l/r pos's as
		--green pixels
		pset(prev[run_y].l,run_y,3)
		pset(prev[run_y].r,run_y,3)
		
		--draw the pivot pos as a
		--blue pixel
		pset(prev[run_y].p,run_y,1)
		
	end
	
	--draw the list as a white line
	--where each pixel is an item
	--gray=not in search range
	--white=is in search range
	local y=1+times
	for i=1,#list do
		if i<l or i>r then
			pset(i,y,6)
		else
			pset(i,y,7)
		end
	end
	
	--draw the target pos as a
	--red pixel
	pset(target_i,y,8)
	
	--draw the l/r pos's as
	--green pixels
	pset(l,y,11)
	pset(r,y,11)
	
	--draw the pivot pos as a
	--blue pixel
	pset(p,y,12)
end
-->8
-- quicksort function
--credit (url) : https://pico-8.fandom.com/wiki/qsort

-- qsort(a,c,l,r)
--
-- a
--    array to be sorted,
--    in-place
-- c
--    comparator function(a,b)
--    (default=return a<b)
-- l
--    first index to be sorted
--    (default=1)
-- r
--    last index to be sorted
--    (default=#a)
--
-- typical usage:
--   qsort(array)
--   -- custom descending sort
--   qsort(array,function(a,b) return a>b end)
--
function qsort(a,c,l,r)
	c,l,r=c or function(a,b) return a<b end,l or 1,r or #a
	if l<r then
		if c(a[r],a[l]) then
			a[l],a[r]=a[r],a[l]
		end
		local lp,k,rp,p,q=l+1,l+1,r-1,a[l],a[r]
		while k<=rp do
			local swaplp=c(a[k],p)
			-- "if a or b then else"
			-- saves a token versus
			-- "if not (a or b) then"
			if swaplp or c(a[k],q) then
			else
				while c(q,a[rp]) and k<rp do
					rp-=1
				end
				a[k],a[rp],swaplp=a[rp],a[k],c(a[rp],p)
				rp-=1
			end
			if swaplp then
				a[k],a[lp]=a[lp],a[k]
				lp+=1
			end
			k+=1
		end
		lp-=1
		rp+=1
		-- sometimes lp==rp, so 
		-- these two lines *must*
		-- occur in sequence;
		-- don't combine them to
		-- save a token!
		a[l],a[lp]=a[lp],a[l]
		a[r],a[rp]=a[rp],a[r]
		qsort(a,c,l,lp-1       )
		qsort(a,c,  lp+1,rp-1  )
		qsort(a,c,       rp+1,r)
	end
end
__gfx__
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
