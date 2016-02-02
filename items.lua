--
--  items.lua
--  a list of objects that the Player can pick up or use
--

Item = {}
Item.__index = Item

function Item.new(type, x, y)

	local self = {}
	setmetatable(self, Item)

	local i = items[type]

	-- position
	self.x = x 
	self.y = y
	self.width = i.width
	self.height = i.height
	self.offset = i.offset
	self.rect = HC.rectangle(x+i.offset.x,y+i.offset.y,i.width,i.height)

	-- descriptors
	self.type = 'item'
	self.name = i.name
	self.img = i.image
	self.description = i.description
	self.health = i.health
	self.action = i.action
	self.pickedUp = false
	self.active = true

	return self

end

function Item:update()
	-- do nothing
end

function Item:draw()
	love.graphics.draw(self.img, self.x, self.y)
end

function Item:kill()
	self.active = false
	HC.remove(self.rect)
end
