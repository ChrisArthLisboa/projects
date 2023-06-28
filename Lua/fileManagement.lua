--[[

io.output("tempfile")

io.write("42")

io.close()

io.input("tempfile")


local info = io.read()

print(info)

]]

local file = io.open("tempfile","w")
file:write([[Ola esse é um teste rapido para um arquivo de texto.
Eu quero ver até onde isso vai]]) -- O ":" é uma representação de função(var1, var2) sendo var1 a variavel colocada atras.
file:close() -- OBS talvez seja na verdade uma representação da função rodar na variavel.

local file = io.open("tempfile","r")
local temp = file:read("*line")
file:close()
print(temp)