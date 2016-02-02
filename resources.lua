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

-- hardon collider
HC = require 'hardoncollider'
-- Collider = HC(64)


-- fonts
fonts = {
	fippsM	= love.graphics.newFont('data/fonts/Fipps-Regular.otf', 32),
	fippsS	= love.graphics.newFont('data/fonts/Fipps-Regular.otf', 24),
	emu 	= love.graphics.newFont('data/fonts/emulogic.ttf', 15)
}


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
