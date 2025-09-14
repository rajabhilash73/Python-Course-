# import random
#
# PlayerHp = 260  # Player starts with 260 hit points (health)
# Enemyatkl = 60  # Enemy's minimum attack damage
# Enemytkh = 80   # Enemy's maximum attack damage
#
# while PlayerHp >= 0:  # Keep looping as while as the player is alive
#     damage = random.randrange(Enemyatkl, Enemytkh)  # Random damage between 60 and 79 (80 is exclusive)
#     PlayerHp = PlayerHp - damage
#
#     if PlayerHp <= 30:
#         PlayerHp = 30
#
#     print("Enemy strikes for damage", damage, "current hp is ", PlayerHp)
#
#     if PlayerHp == 30:
#         print("You have low hp, you have been teleported to the nearest inn")
#         break

# import random
#
# def battle():
#     # Initialize values
#     player_hp = 260          # Player's starting health
#     enemy_attack_min = 60    # Minimum enemy attack damage
#     enemy_attack_max = 80    # Maximum enemy attack damage
#
#     print("⚔️ Battle begins! Player HP:", player_hp)
#
#     # Run the battle loop
#     while player_hp > 0:
#         # Enemy deals random damage
#         damage = random.randrange(enemy_attack_min, enemy_attack_max)
#         player_hp -= damage
#
#         # Ensure HP doesn't drop below 30
#         if player_hp <= 30:
#             player_hp = 30
#
#         # Show attack results
#         print(f" Enemy strikes for {damage} damage! Current HP: {player_hp}")
#
#         # Check if player should be teleported
#         if player_hp == 30:
#             print(" You have low HP! You have been teleported to the nearest inn.")
#             break
#
# # Run the game
# battle()


import random

def battle():
    # Initialize values
    player_hp = 260
    enemy_hp = 300
    player_attack_min, player_attack_max = 40, 70
    enemy_attack_min, enemy_attack_max = 60, 80

    print("⚔️ Battle begins!")
    print(f"Player HP: {player_hp} | Enemy HP: {enemy_hp}\n")

    # Battle loop
    while player_hp > 0 and enemy_hp > 0:
        # --- Player attacks ---
        damage_to_enemy = random.randrange(player_attack_min, player_attack_max)
        enemy_hp -= damage_to_enemy
        print(f"🗡️ Player strikes for {damage_to_enemy} damage! Enemy HP: {max(enemy_hp, 0)}")

        # Check if the enemy is defeated
        if enemy_hp <= 0:
            print("\n🎉 Enemy defeated! You are victorious!")
            break

        # --- Enemy attacks ---
        damage_to_player = random.randrange(enemy_attack_min, enemy_attack_max)
        player_hp -= damage_to_player
        if player_hp <= 30:
            player_hp = 30
        print(f"💥 Enemy strikes for {damage_to_player} damage! Player HP: {player_hp}")

        # Check if player needs teleport
        if player_hp == 30:
            print("\n🌀 You have low HP! You have been teleported to the nearest inn.")
            break

# Run the game
battle()

import random

class enemy:
    hp = 200
    def __init__(self, EnemyAttackLow, EnemyAttackHigh):
        # self.EnemyAttcakLow = None
        self.EnemyAttackLow = EnemyAttackLow
        self.EnemyAttackHigh = EnemyAttackHigh

    def attack(self):
        print("The attack power is ", self.EnemyAttackLow)

    def getHp(self):
        print("The enemy Hp is : ", self.hp)

enemy1 = enemy(50, 58)
enemy1.attack()
enemy1.getHp()

enemy2 = enemy(60, 69)
enemy2.attack()
enemy2.getHp()






