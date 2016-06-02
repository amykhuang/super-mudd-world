-- 
--  resources.lua
--  global variables and the like

-- sizes
WINDOW_W = 1024
WINDOW_H = 640

TILE_W = 64
TILE_H = 64

-- colors
black = {0,0,0}
white = {255,255,255}
red = {100,0,0}
aqua = {0,204,204}

-- collision management
HC = require 'hardoncollider'
-- Collider = HC(64)

-- pretty text
lib = require 'tastytext.tastytext'

-- animations
require("AnAL")

-- fonts
fonts = {
	fippsXL	= love.graphics.newFont('data/fonts/Fipps-Regular.otf', 48),
	fippsL	= love.graphics.newFont('data/fonts/Fipps-Regular.otf', 40),
	fippsM	= love.graphics.newFont('data/fonts/Fipps-Regular.otf', 32),
	fippsS	= love.graphics.newFont('data/fonts/Fipps-Regular.otf', 24),
	fippsXS	= love.graphics.newFont('data/fonts/Fipps-Regular.otf', 16),
	emuS 	= love.graphics.newFont('data/fonts/emulogic.ttf', 24),
	emuXS 	= love.graphics.newFont('data/fonts/emulogic.ttf', 16)
}

--
-- entity info

blocks = {}

blocks[1] = {
	name = 'solid',
	description = 'a basic solid, invisible platform.',
	health = 0,
	image = nil,
	step_x = 0,
	range = 0,
	width = TILE_W,
	height = TILE_H,
	offset = { x = 0, y = 0 }
}

blocks[2] = {
	name = 'moving',
	description = 'a platform the moves in the x direction.',
	health = 0,
	image = nil,
	step_x = 0,
	range = 0,
	width = TILE_W,
	height = TILE_H,
	offset = { x = 0, y = 0 }
}

blocks[3] = {
	name = 'spikes',
	description = 'warning. lowers health.',
	health = -1,
	image = nil,
	step_x = 0,
	range = 0,
	width = TILE_W,
	height = TILE_H,
	offset = { x = 0, y = 0 }
}


items = {}

items[1] = {
	name = 'solo cup',
	description = 'a red solo cup. increases health.',
	action = 'pass',
	health = 1,
	image = love.graphics.newImage('/data/images/cup.png'),
	width = 22,
	height = 30,
	offset = { x = 21, y = 31 }
}

items[2] = {
	name = 'broken glass',
	description = 'broken glass. beware.',
	action = 'danger',
	health = -1,
	image = love.graphics.newImage('/data/images/glass.png'),
	width = TILE_W,
	height = 21,
	offset = { x = 0, y = 43 }
}

enemies = {}

enemies[1] = {
	name = 'wart',
	description = 'a walking purple wart.',
	health = -1,
	image = love.graphics.newImage('data/images/wart1L.png'),
	step_x = 3,
	range = 100,
	width = 39,
	height = 48,
	offset = { x = 5, y = 15 },
	cycleImages = {
		love.graphics.newImage('data/images/wart1L.png'),
		love.graphics.newImage('data/images/wart2L.png'),
		love.graphics.newImage('data/images/wart3L.png'),
		love.graphics.newImage('data/images/wart1R.png'),
		love.graphics.newImage('data/images/wart2R.png'),
		love.graphics.newImage('data/images/wart3R.png')
	}
}

friends = {}

friends[1] = {
	name = 'ron',
	description = 'the sausage king.',
	image = love.graphics.newImage('data/images/ron.png'),
	dialogue = {
		"Hello, my name is Ron.",
		"I am a sausage."
	},
	width = 52,
	height = 126,
	offset = { x = 4, y = 2 }
}

--
-- useful functions

function centerAlignPos(text, x_offset, y_offset)

	pos_x = WINDOW_W/2 - text:getWidth()/2 + x_offset
	pos_y = WINDOW_H/2 - text:getHeight()/2 + y_offset
	
	return pos_x, pos_y

end


function leftAlignPos(text, x_offset, y_offset)

	pos_x = 50 + x_offset
	pos_y = 30 + y_offset
	
	return pos_x, pos_y

end
