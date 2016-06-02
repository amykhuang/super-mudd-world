--
--  game.lua
--  controls the flow of the game
--

require 'resources'
require 'map'
require 'player'

Game = {}
Game.__index = Game

local map, player, friend

function Game.new()
	local self = {}
	setmetatable(self, Game)

	self.state = 'intro'
	self.level = 1

	return self
end


function Game:load()

	map = Introscreen.new()
	player = Player.new()

end

function Game:update(dt)

	-- intro state
	if self.state == 'intro' then

		map:update(dt)

		-- begin game with finished
		if map.page == map.lastpage then

			self.state = 'play'

			map = Map.new(self.level)
			player.active = true

		end

	end

	-- play state
	if self.state == 'play' then

		self.state = player:update(dt, map)
		map:update(dt)

	-- talk state
	elseif self.state == 'talk' then

		friend.speaking = true
		map:update(dt)

		if friend:isDone() then
			self.state = 'play'
		end

	-- gameover state
	elseif self.state == 'gameover' then

		player:kill()

		map = Endscreen.new()

	end
end

function Game:keypressed(key)

	-- exit game if 'escape' is pressed
	if key == 'escape' then
		love.event.push('quit')
	end

	if self.state == 'intro' then

		-- continue with spacebar
		if key == 'space' then
			map.page = map.page + 1
		end

	end

	if self.state == 'play' then

		-- talk if spacebar is pressed within range
		if key == 'space' and player.state == 'standing' then
			friend = player:isNearFriend(map.friends)

			if friend then
				self.state = 'talk'
			end
		end

	end

	if self.state == 'talk' then

		-- exit talking mode if 'x' is pressed
		if key == 'x' then
			friend.speaking = false
			self.state = 'play'

		-- continue talking with spacebar
		elseif key == 'space' then
			friend.lineNum = friend.lineNum + 1
		
		end

	end

	if self.state == 'gameover' then
		if key == 'q' then
			love.event.push('quit')

		elseif key == 'space' then
			self:reload()
		end
	end

end

function Game:draw()
	
	map:draw()
	if player.active then player:draw() end

end

function Game:reload()
	
	self.state = 'play'
	self.level = 1

	self:load()
end
