--[[
    Pairs: Listas desordenadas (Tambem multidimensionais)
    iPairs: Listas ordendas

    Termos:
        Chaves(Indexador) e valores. Como um dicionario
]]

--[[
    Shows array with respective index

    local array = {"Ol".. string.char(160),"Hola","Hello"} -- char(161) = á que não tem comumente

    for index, value in ipairs( array ) do
        print(index, value)
    end
]]

local array = {"Portugues", "Ingles", "Espanhol"}
array.Portugues = "Ol" .. string.char(160)
array.Ingles = "Hello"
array.Espanhol = "Hola"

print(("-----"):rep(6))
print(#array)
print(("-----"):rep(6))

for index, value in pairs(array) do
    print(("%10s:"):format(index),value)
end
print(("-----"):rep(6))
