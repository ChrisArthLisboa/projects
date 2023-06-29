
--[[
    - Arrays
    - Records
    - Lists
    - Queues
    - Sets
]]

function ShTb(Array)

    --[[ Show table. 
        Array é a table que você quer que seja mostrada.
        Ela não retorna nada.
    ]]

    local str = ""
    for i=1, #Array do
        str = str .. Array[i] .. " "
    end
    print("[ " .. str .. "]")
end

local Array = {}

for i=1, 10 do
    print("Enter a number: ")
    Array[i] = io.read()
end
print(("-----"):rep(6))

print(#Array) -- Mostra quantos valores
print(("-----"):rep(6))

ShTb(Array)
print(("-----"):rep(6))

table.remove(Array, 9) -- Remove a nona posição
ShTb(Array)
print(("-----"):rep(6))


table.insert(Array, "4") 
--[[ Coloca um baguio novo na posição.
    (Tem que ser string pra ser do mesmo tipo que a array else o sort não funfa) 
    ]]
ShTb(Array)
print(("-----"):rep(6))

table.sort(Array)
ShTb(Array)
print(("-----"):rep(6))
