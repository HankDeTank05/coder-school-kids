function love.load()
    player = {
        x = 0,
        y = 0,
        width = 30,
        height = 50,
        speed = 700,
    }

    platform = {
        x = 0 ,
        y = 100 ,
        width = 70,
        height = 20
    }

    gravity = 10

end

function love.update(frame_time)
    position_delta = player.speed * frame_time

    -- move right
    if love.keyboard.isDown('d') then
        player.x = player.x + position_delta
    end
    
    --move left
    if love.keyboard.isDown('a') then
        player.x = player.x + -position_delta
    end

    -- move down
    if love.keyboard.isDown('s') then
        player.y = player.y + position_delta
    end

    -- move up
    if love.keyboard.isDown("w") then
        player.y = player.y + -position_delta
    end

    --  apply gravity
    player.y = player.y + gravity

    -- prevent the rectangle from going off-screen on the left and right edge
    if player.x < 0 then
        player.x = 0
    elseif player.x + player.width - 1 > love.graphics.getWidth() then
        player.x = love.graphics.getWidth() - player.width + 1
    end

    -- prevent the rectangle from going off-screen on the top and bottom edge
    if player.y < 0 then 
        player.y = 0
    elseif player.y + player.height - 1 > love.graphics.getHeight() then
        player.y = love.graphics.getHeight() - player.height + 1
    end

end

function love.draw()
    love.graphics.rectangle('fill', player.x, player.y, player.width, player.height)
    love.graphics.rectangle('fill', platform.x , platform.y , platform.width , platform.height)
    love.graphics.print("Hello World", 400, 300)
end