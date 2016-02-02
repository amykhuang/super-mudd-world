--
--  main.lua
--

require 'game'

g = Game.new()

function love.load(args)
	g:load()
end

function love.update(dt)
	g:update(dt)
end

function love.keypressed(key)
	g:keypressed(key)
end

function love.draw(dt)
	g:draw()
end
