altura_chico = 150  
altura_ze = 130  # 
crescimento_chico = 2  
crescimento_ze = 3  
anos = 0  

while altura_ze <= altura_chico:
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    anos += 1

print(f"Serão necessários {anos} anos para que Zé seja mais alto que Chico.")
