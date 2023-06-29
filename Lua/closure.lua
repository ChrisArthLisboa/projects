--[[
    função anonima dentro de outra

    Geralmente usada para retornar ou passar informação como parametros
]]

local function teste()
    i = 0
    return function ()
        i = i+1
        return i
    end
end

local a = teste()

print(a())
print(a())
print(a())