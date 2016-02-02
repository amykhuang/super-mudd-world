--
--  enemy.lua
--  defines the Enemy class
--

Enemy = {}
Enemy.__index = Enemy

function Enemy.new(type, x, y)

	local self = {}
	setmetatable(self, Enemy)

	local e = enemies[type]

	-- position
	self.x = x
	self.y = y
	self.width = e.width
	self.height = e.height
	self.offset = e.offset
	self.rect = HC.rectangle(x+self.offset.x,y+self.offset.y,self.width,self.height)

	-- descriptors
	self.type = 'enemy'
	self.name = e.name
	self.description = e.description
	self.img = e.image
	self.health = e.health
	self.active = true

	-- moving
	self.start = x 
	self.range = e.range
	self.fin = self.start + self.range
	self.step_x = e.step_x
	self.vel = { x = e.step_x, y = 0 }
	self.dwalk = 0
	self.imgNum = 1

	self:loadImages(e)


	return self

end

function Enemy:loadImages(e)
-- load images for walkcycles

	self.walkL = {}
	self.walkL[1] = e.cycleImages[1]
	self.walkL[2] = e.cycleImages[2]
	self.walkL[3] = e.cycleImages[3]

	self.walkR = {}
	self.walkR[1] = e.cycleImages[4]
	self.walkR[2] = e.cycleImages[5]
	self.walkR[3] = e.cycleImages[6]
end

function Enemy:update(dt, bgPos)

	self:walkcycle(dt)

	if self.step_x ~= 0 then
		if self.x >= self.fin + bgPos then
			self.vel.x = -self.step_x
		elseif self.x < self.start + bgPos then
			self.vel.x = self.step_x
		end

		self.x = self.x + self.vel.x

		self.rect:moveTo(self.x + self.width/2 + self.offset.x, self.y + self.height/2 + self.offset.y)
	end
end

function Enemy:draw()
	love.graphics.draw(self.img, self.x, self.y)
end

function Enemy:walkcycle(dt)
	self.dwalk = self.dwalk + dt

	-- while walking
	if self.dwalk > 0.3 then
		if self.vel.x < 0 then 
			self.img = self.walkL[self.imgNum]
		else
			self.img = self.walkR[self.imgNum]
		end

		-- increment imgNum
		self.imgNum = self.imgNum + 1
		if self.imgNum > 3 then self.imgNum = 1 end

		self.dwalk = self.dwalk - 0.3
	end
end