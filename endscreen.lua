--
--  endscreen.lua
--  the gameover screen
--

Endscreen = {}
Endscreen.__index = Endscreen

function Endscreen.new()
	local self = {}
	setmetatable(self, Endscreen)

	self.title = 'Game Over'
	self.subtitle = 'Press space to play again. Press q to quit.'

	return self
end

function Endscreen:update()
	-- does nothing
end

function Endscreen:draw()
	local title = love.graphics.newText(fonts['fippsM'], {red, self.title})
	local subtitle = love.graphics.newText(fonts['fippsS'],{red, self.subtitle}) 

	love.graphics.setBackgroundColor(black)
	love.graphics.draw(title, WINDOW_W/2-title:getWidth()/2, WINDOW_H/2-title:getHeight()/2-20)
	love.graphics.draw(subtitle, WINDOW_W/2-subtitle:getWidth()/2, WINDOW_H/2-subtitle:getHeight()/2+70)
end

