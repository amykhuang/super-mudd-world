--
--  blocks.lua
--  defines the Block class
--

Block = {}
Block.__index = Block

function Block.new(type, x, y)

	local self = {}
	setmetatable(self, Block)

	local b = blocks[type]

	-- position
	self.x = x 
	self.y = y
	self.width = b.width
	self.height = b.height
	self.offset = b.offset
	self.rect = HC.rectangle(x+self.offset.x,y+self.offset.y,self.width,self.height)

	-- descriptors
	self.type = 'block'
	self.name = b.name
	self.description = b.description
	self.typ = b.typ
	self.img = b.image
	self.health = b.health
	self.active = true

	-- moving
	self.start = x 
	self.range = b.range
	self.fin = self.start + self.range
	self.step_x = b.step_x
	self.vel = { x = b.step_x, y = 0 }

	return self

end

function Block:update(dt, bgPos)

	-- walk back and forth
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

function Block:draw()
	love.graphics.draw(self.img, self.x, self.y)
end

