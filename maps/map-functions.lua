require 'player'

local tileW, tileH, tileSet, quads, tileTable


function loadMap(path)
	love.filesystem.load(path)()
end


function newMap(tileWidth, tileHeight, tileSetPath, quadInfo, tileString)

	tileW, tileH = tileWidth, tileHeight
	tileSet = love.graphics.newImage(tileSetPath)

	local tileSetW, tileSetH = TileSet:getWidth(), TileSet:getHeight()
	local width = #(tileString:match("[^\n]+"))

	map = {
		x = 0,
		y = 0,
		width = width * tileW
	}

	quads = {}

	for i=1, #quadInfo do
		local info = quadInfo[i]
		quads[info[1]] = love.graphics.newQuad(info[2], info[3], TileW, TileH, tileSetW, tileSetH)
	end

	tileTable = {}


	for x = 1,width,1 do TileTable[x] = {} end

	local x,y = 1,1
	for row in tileString:gmatch("[^\n]+") do
		assert(#row == width, 'Map is not aligned: width of row ' .. tostring(rowIndex) .. ' should be ' .. tostring(width) .. ', but it is ' .. tostring(#row))
		x = 1
		for character in row:gmatch(".") do
			tileTable[x][y] = character
			x = x + 1
		end
		y = y + 1
	end
end

function mapToWorld(mx, my)
	return (mx-1)*tileW, (my-1)*tileH
end

function drawMap()

	-- Determine whether to move the player or the background

	for columnIndex,column in ipairs(tileTable) do
		for rowIndex,char in ipairs(column) do
			local x,y = (columnIndex-1)*tileW + shift, (rowIndex-1)*tileH
			love.graphics.draw(tileSet, Quads[char], x, y) 
		end
	end
end
