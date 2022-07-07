from character import Character

spidey = Character("Peter Parker","Spiderman")
spidey.set_power("Web-Slinging")
hulk = Character("Bruce Banner","Hulk")
hulk.set_power("smashing")

print(f"{spidey.name} is actually the superhero {spidey.super} and his power is {spidey.power}")
print(f"{hulk.name} is actually the superhero {hulk.super} and his power is {hulk.power}")

spidey.get_power()
hulk.get_power()