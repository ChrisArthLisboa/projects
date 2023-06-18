import pyautogui as pyg

m = str(input("Mensagem: ")).capitalize()
q = int(input("Quantidade: "))

pyg.sleep(3)

for c in range(1,q):
	pyg.write(m)
	pyg.press("Enter")
