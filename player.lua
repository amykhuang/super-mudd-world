--
--  player.lua
--  defines the Player class
--

require 'resources'

Player = {}
Player.__index = Player


local gravity = 1500
local stepSize = 3


function Player.new()
	local self = {}
	setmetatable(self, Player)

	self.img = love.graphics.newImage('/data/images/walkR1.png')

	-- position
	self.x = 10
	self.y = 400

	-- collisions
	self.width = self.img:getWidth()
	self.height = self.img:getHeight()
    self.rect = HC.rectangle(self.x,self.y,self.width,self.height)

	-- jumping
	self.y_vel = 0
	self.jump_fuel = 0.5
	self.jump_fuel_max = 0.5
	self.jump_height = -500

	-- state
	self.state = "jumping"
	self.health = 10
	self.walking = false
	self.x_platform_speed = 0
	self.damaged = false
	self.active = false

	-- walkcycle
	self:loadImages()
	self.dwalk = 0		-- time elapsed		
	self.imgNum = 1 	-- image rotation number

	self.ddamage = 0	-- damage inflicted at discrete intervals

	return self

end

function Player:update(dt, bg)

	local dx, dy

	-- move left
	if love.keyboard.isDown('left') and self.x > 0 then
		dx = -stepSize

	-- move right
	elseif love.keyboard.isDown('right') and self.x < 900 then
		dx = stepSize

	else
	    dx = 0
	end

	-- add platform speed
	dx = dx + self.x_platform_speed

	dy = self.y_vel * dt
	self.y_vel = self.y_vel + gravity * dt


	-- jump
	if self.jump_fuel > 0 and love.keyboard.isDown('up') then
		-- begin jump
		if self.state == 'standing' then
			self.y_vel = self.jump_height
			self.state = 'jumping'
		end

		-- continue jumping
		self.jump_fuel = self.jump_fuel - dt
		self.y_vel = self.y_vel + 0.6 * self.jump_height * (dt / self.jump_fuel_max)
	end

	self:move(bg, dt, dx, dy)

	-- change the game state, if necessary
	if self.health <= 0 then
		return 'gameover'
	end
	
	return 'play'

end

function Player:draw()
	local health = love.graphics.newText(fonts['fippsM'], {black,self.health})

	love.graphics.draw(health, WINDOW_W - health:getWidth() - 10, 10)
	love.graphics.draw(self.img, self.x, self.y)
end

function Player:move(bg, dt, dx, dy)

	-- move left
	if dx < 0 and self.x > 0 then
		if self.x - bg.x <= 200
			or (bg.width + bg.x <= WINDOW_W and self.x > 200) then
			self.x = self.x + dx
		elseif bg.x < 200 then
	    	bg:shiftWorld(dx)
	    end

	-- move right
	elseif dx > 0 and self.x < WINDOW_W - self.width then
		if self.x < 200 or bg.width + bg.x <= WINDOW_W then
			self.x = self.x + dx
		elseif bg.x > WINDOW_W - bg.width then
			bg:shiftWorld(dx)
		end
	end

	-- gravity
	self.y = self.y + dy

	-- update collision rect
	self.rect:moveTo(self.x + self.width/2.0, self.y + self.height/2.0)

	--
	-- collision checking
	--

	for i=1, #bg.entities do

		thing = bg.entities[i]
		local x,y = thing.rect:center()

		if self.rect:collidesWith(thing.rect) and thing.active then

			if thing.type == 'block' then

				-- if landing on top of the block
				if dy > 0 and self.y + self.height < y - thing.height/4 then
					self.y = y - thing.height/2 - self.height
					self.y_vel = 0
					self.jump_fuel = self.jump_fuel_max
					self.x_platform_speed = thing.vel.x
					self.state = 'standing'

					self:updateHealth(dt, thing)
				end

			elseif thing.type == 'item' then
				self:updateHealth(dt, thing)
				thing:kill()

			elseif thing.type == 'enemy' then

				-- if landing on top of the enemy
				if dy >= 0 and self.y + self.height < y - thing.height/4 then
					self.y = y - thing.height/2 - self.height
					self.y_vel = 0
					self.jump_fuel = self.jump_fuel_max
					self.x_platform_speed = thing.vel.x
					self.state = 'standing'

				-- if hitting the side of the enemy
				else
				    self:updateHealth(dt, thing)
				end
			end

		end
	end

	-- update walkcycle image
	self:walkcycle(dt, dx)

end

function Player:kill()
	self.active = false
end

function Player:keypressed(bg)
	-- check keypresses
end


function Player:updateHealth(dt, thing)

	self.ddamage = self.ddamage + dt

	if thing.health >= 0 then
		self.health = self.health + thing.health

	-- take damage at discrete time intervals
	elseif self.damaged == false then
		self.health = self.health + thing.health
		self.damaged = true
	end

	-- reset time counter
	if self.ddamage > 0.5 then
		self.damaged = false
		self.ddamage = self.ddamage - 0.5
	end
end


function Player:loadImages()
-- load images for walkcycles

	self.walkL = {}
	self.walkL[1] = love.graphics.newImage('data/images/walkL1.png')
	self.walkL[2] = love.graphics.newImage('data/images/walkL2.png')
	self.walkL[3] = love.graphics.newImage('data/images/walkL3.png')
	self.walkL[4] = love.graphics.newImage('data/images/walkL2.png')

	self.walkR = {}
	self.walkR[1] = love.graphics.newImage('data/images/walkR1.png')
	self.walkR[2] = love.graphics.newImage('data/images/walkR2.png')
	self.walkR[3] = love.graphics.newImage('data/images/walkR3.png')
	self.walkR[4] = love.graphics.newImage('data/images/walkR2.png')

end



function Player:walkcycle(dt, dx)
	self.dwalk = self.dwalk + dt

	-- if jumping
	if self.state == 'jumping' then
		if dx < 0 then 
			self.img = self.walkL[2]
		elseif dx > 0 then
			self.img = self.walkR[2]
		end
	end

	-- while walking
	if dx ~= 0 and self.state == 'standing' and self.dwalk > 0.3 then
		if dx < 0 then 
			self.img = self.walkL[self.imgNum]
		else
			self.img = self.walkR[self.imgNum]
		end

		-- increment imgNum
		self.imgNum = self.imgNum + 1
		if self.imgNum > 4 then self.imgNum = 1 end

		self.dwalk = self.dwalk - 0.3
	end
end

function Player:isNearFriend(friends)
	for i=1, #friends do
		if self.rect:collidesWith(friends[i].rect) then
			return friends[i]
		end
	end
	return false
end

