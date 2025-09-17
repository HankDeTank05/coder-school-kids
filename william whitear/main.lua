function love.load()
    x = 0 
    y = 0
    width = 30
    height = 100
    speed = 25

end

function love.update(frame_time)
    -- move right
    if love.keyboard.isDown('d') then
        x = x + speed
    end
    --move left
    if love.keyboard.isDown('a') then
        x = x + -speed
    end
    -- move down
    if love.keyboard.isDown('s') then
        y = y + speed
    end
    -- move up
    if love.keyboard.isDown("w") then
        y = y + -speed
    end

    -- prevent the rectangle from going off-screen on the top edge
    if y < 0 then
        -- TODO: next time!
    end
end

function love.draw()
    love.graphics.rectangle('fill', x, y, width, height)
    love.graphics.print("Hello World", 400, 300)
end