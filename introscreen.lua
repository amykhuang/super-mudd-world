--
--  introscreen.lua
--  the introductory screen
--

Introscreen = {}
Introscreen.__index = Introscreen

function Introscreen.new()
	local self = {}
	setmetatable(self, Introscreen)

	self.title = 'Super Mudd World'
	self.subtitle = 'The most badass game Amy and Sarah have ever made.'
	self.page = 0 				-- current page number
	self.lastpage = 3 			-- number of total pages
	self.timer = 0				-- for blinking text and animations
	self.showBlinking = true 	-- blinking text
	self.nextPage = false		-- when to move to next page

	return self
end

function Introscreen:update(dt)
	
	-- timer for blinking text
	self.timer = self.timer + dt

	if self.timer > 0.4 then
		self.showBlinking = false
	end

	if self.timer > 0.8 then
		self.showBlinking = true
		self.timer = self.timer - 0.8
	end

end

function Introscreen:draw()
	local p = self.page

	if p == 0 then
		self:page0()
	elseif p == 1 then
		self:page1()
	elseif p == 2 then
		self:page2()
	end
end

function Introscreen:page0()

	local title = love.graphics.newText(fonts['fippsXL'], {white, self.title})
	local subtitle = love.graphics.newText(fonts['emuXS'], {aqua, self.subtitle})
	
	local text = '(Press space to continue.)'
	local info = love.graphics.newText(fonts['emuS'], {white, text})

	local title_x, title_y = centerAlignPos(title, 0, -60)
	local subtitle_x, subtitle_y = centerAlignPos(subtitle, 0, 30)
	local info_x, info_y = centerAlignPos(info, 0, 200)

	local titl = love.graphics.newText(fonts['fippsXL'], {white, self.title:sub(0,1)})
	
	love.graphics.setBackgroundColor(black)
	love.graphics.draw(titl, title_x, title_y)
	love.graphics.draw(subtitle, subtitle_x, subtitle_y)
	
	-- blinking text
	if self.showBlinking then
		love.graphics.draw(info, info_x, info_y)
	end

end

function Introscreen:page1()

	local l1 = 'Use the arrow keys to move.'
	local l2 = 'Use the spacebar to jump.'
	local l3 = 'Pick up objects for health.'
	local l4 = 'Avoid enemies.'

	local title = love.graphics.newText(fonts['fippsL'], {white, 'Instructions'})
	local line1 = love.graphics.newText(fonts['emuS'], {white, l1})
	local line2 = love.graphics.newText(fonts['emuS'], {white, l2})
	local line3 = love.graphics.newText(fonts['emuS'], {white, l3})
	local line4 = love.graphics.newText(fonts['emuS'], {white, l4})

	local title_x, title_y = leftAlignPos(title, 0, 0)
	local line1_x, line1_y = leftAlignPos(line1, 0, 150)
	local line2_x, line2_y = leftAlignPos(line2, 0, 200)
	local line3_x, line3_y = leftAlignPos(line3, 0, 250)
	local line4_x, line4_y = leftAlignPos(line4, 0, 300)

	love.graphics.setBackgroundColor(black)
	love.graphics.draw(title, title_x, title_y)
	love.graphics.draw(line1, line1_x, line1_y)
	love.graphics.draw(line2, line2_x, line2_y)
	love.graphics.draw(line3, line3_x, line3_y)
	love.graphics.draw(line4, line4_x, line4_y)
end

function Introscreen:page2()
	
	local text = '(Press space to begin.)'
	local info = love.graphics.newText(fonts['emuS'], {white, text})

	local info_x, info_y = centerAlignPos(info, 0, 0)
	
	love.graphics.setBackgroundColor(black)

	-- blinking text
	if self.showBlinking then
		love.graphics.draw(info, info_x, info_y)
	end
end
