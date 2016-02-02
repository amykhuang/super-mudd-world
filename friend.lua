--
--  friend.lua
--  defines the Friend class
--

Friend = {}
Friend.__index = Friend

function Friend.new(type, x, y)
	local self = {}
	setmetatable(self, Friend)

	f = friends[type]

	-- position
	self.x = x
	self.y = y
	self.width = f.width
	self.height = f.height
	self.offset = f.offset
	self.rect = HC.rectangle(x+self.offset.x,y+self.offset.y,self.width,self.height)

	-- descriptors
	self.type = 'friend'
	self.name = f.name
	self.description = f.description
	self.img = f.image
	self.health = 0
	self.active = true

	-- speaking
	self.dialogue = f.dialogue
	self.speaking = false
	self.lineNum = 0
	self.text = nil

	return self
end


function Friend:update()
	-- do nothing
end

function Friend:draw()
	love.graphics.draw(self.img, self.x, self.y)

	if self.speaking then
		self:makeText()
		love.graphics.draw(self.text, WINDOW_W - self.text:getWidth(), 10)
	end
end

function Friend:makeText()
	local words = self.dialogue[self.lineNum]
	self.text = love.graphics.newText(fonts['emu'], {black,words})
end

function Friend:isDone()
	if self.lineNum >= #self.dialogue+1 then
		self.lineNum = 0
		return true
	end
	return false
end
