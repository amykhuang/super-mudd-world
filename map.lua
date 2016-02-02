--
--  map.lua
--  defines the Map class
--  loads and updates maps for each corresponding level 
--

require 'resources'

require 'blocks'
require 'items'
require 'enemy'
require 'friend'

require '/maps/map01'
require 'endscreen'


Map = {}
Map.__index = Map

local toPrint = ''	-- DEBUG


function Map.new(mapNum)
	local self = setmetatable({}, Map)

	-- get specific map class
	map = self:loadMap(mapNum)

	-- position
	self.x = 0
	self.y = 0

	self.quads = {}			
	self.tileTable = {}
	self.blocks = {}
	self.items = {}
	self.enemies = {}
	self.friends = {}
	
	-- combined list of everything on the map
	self.entities = {}

	self.width = map.width
	self.tileset = love.graphics.newImage(map.tilesetPath)

	self:newMap(map)

	return self
end

function Map:update(dt)
	for i=1, #self.entities do
		local entity = self.entities[i]
		if entity.active then entity:update(dt, self.x) end
	end
end

function Map:draw()

	-- draw background
	for columnIndex,column in ipairs(self.tileTable) do
		for rowIndex,char in ipairs(column) do
			local x,y = self:scale(columnIndex, rowIndex)
			love.graphics.draw(self.tileset, self.quads[char], x, y) 
		end
	end

	-- draw other objects
	for i=1, #self.entities do
		local e = self.entities[i]
		if e.active and e.img then e:draw() end
	end

	love.graphics.print(toPrint, 100, 100)	-- DEBUG

end

function Map:scale(mx, my)
	-- scales tile coordinate to actual tile position
	return (mx-1)*TILE_W + self.x, (my-1)*TILE_H + self.y
end

function Map:shiftWorld(dx)
	self.x = self.x - dx

	for i=1, #self.entities do
		local e = self.entities [i]
		if e.active then
			e.x = e.x - dx
			e.rect:moveTo(e.x + e.width/2 + e.offset.x, e.y + e.height/2 + e.offset.y)
		end
	end
end

function Map:newMap(map)
	-- loads a map from string info

	local tilesetW, tilesetH = self.tileset:getWidth(), self.tileset:getHeight()

	-- create quads for the background image
	for i=1, #map.quadInfo do
		local info = map.quadInfo[i]
		self.quads[info[1]] = love.graphics.newQuad(info[2], info[3], TILE_W, TILE_H, tilesetW, tilesetH)
	end

	-- create tiles for display
	local width = #(map.tileString:match('[^\n]+'))

	for x = 1,width,1 do self.tileTable[x] = {} end

	local x,y,i = 1,1,1
	for row in map.tileString:gmatch('[^\n]+') do
		assert(#row == width, 'Map is not aligned: width of row ' .. tostring(rowIndex) .. ' should be ' .. tostring(width) .. ', but it is ' .. tostring(#row))
		x = 1
		for character in row:gmatch(".") do
			self.tileTable[x][y] = character
			x = x + 1
		end
		y = y + 1
	end

	-- create list of tiles
	local i = 1
	for row=1, #map.tiles do
		for col=1, #map.tiles[1] do
			local char = map.tiles[row][col]
			if char ~= 0 then
				self.blocks[i] = Block.new(char, (col-1)*TILE_W, (row-1)*TILE_H)
				i = i + 1
			end
		end
	end

	-- create list of items
	for i=1, #map.items do
		local item = map.items[i]
		self.items[i] = Item.new(item[1], (item[2]-1)*TILE_W, (item[3]-1)*TILE_H)
	end

	-- create list of enemies
	for i=1, #map.enemies do
		local e = map.enemies[i]
		self.enemies[i] = Enemy.new(e[1], (e[2]-1)*TILE_W, (e[3]-1)*TILE_H)
	end

	-- create list of friends
	for i=1, #map.friends do
		local f = map.friends[i]
		self.friends[i] = Friend.new(f[1], (f[2]-1)*TILE_W, (f[3]-1)*TILE_H)
	end

	-- create combined list
	for i=1, #self.blocks do
	    self.entities[#self.entities+1]=self.blocks[i]
	end
	for i=1, #self.items do
		self.entities[#self.entities+1] = self.items[i]
	end
	for i=1, #self.enemies do
		self.entities[#self.entities+1] = self.enemies[i]
	end
	for i=1, #self.friends do
		self.entities[#self.entities+1] = self.friends[i]
	end

end

function Map:loadMap(num)
	local map

	if num == 1 then
		map = Map01.new()
	end

	return map
end

