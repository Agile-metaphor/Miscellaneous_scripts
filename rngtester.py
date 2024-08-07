import random, colorama, os, sys, time
from colorama import Fore

colorama.init(autoreset=True)

def iv_gen():
    print(f"\n [{Fore.CYAN}+{Fore.RESET}] {Fore.CYAN}(Ctrl C to exit) Press enter to generate more IV's\n")

    while True:
        Hp = f"HP: {random.randint(0,31)}"
        Attack = f"Attack: {random.randint(0,31)}"
        Defense = f"Defense: {random.randint(0,31)}"
        Special_Attack = f"Special_Attack: {random.randint(0,31)}"
        Special_Defense = f"Special_Defense: {random.randint(0,31)}"
        Speed = f"Speed: {random.randint(0,31)}"

        Stats = [Hp, Attack, Defense, Special_Attack, Special_Defense, Speed]

        count = 0
        zero_count = 0
        for stat in Stats:
            stat_name, stat_value = stat.split(":")
            stat_value = int(stat_value)
        
            if int(stat_value) == 0:
                stat_value_format = f"{Fore.RED}{stat_value}{Fore.RESET}"
                zero_count += 1
            else:
                stat_value_format = int(stat_value)
                if stat_value_format == 31:
                    stat_value_format = f"{Fore.GREEN}{stat_value_format}{Fore.RESET}"
                    count += 1

            print(f" [{Fore.CYAN}+{Fore.RESET}] {stat_name}: {stat_value_format}")

        if count == 6:
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: Bro theres no way.")
        elif zero_count == 6:
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: ...")
        elif count >= 1 and zero_count >= 1:
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: Weird ahh IV's")
        elif zero_count >= 2:
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: LMAO WHAT AM I LOOKING AT RIGHT NOW")
        elif count == 1:
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: You got a max stat!")
        elif count > 1:
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: {count} max stats, not bad!")
        elif zero_count == 1:
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: Having a 0 IV stat is crazy")
        else:
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: These IV's mid as hell.")
        

        again = input()

        if again not in {""}:
            main()

def shiny_gen():
    print(f"\n [{Fore.CYAN}+{Fore.RESET}] {Fore.CYAN}(Ctrl C to exit) Press enter to try again{Fore.RESET}")

    while True:
        count = 0
        shiny = random.randint(1, 30000)

        while True:
            encounter = random.randint(1, 30000)
            count += 1

            if shiny == encounter:
                print(f"\n [{Fore.CYAN}+{Fore.RESET}] Number of encounters: {Fore.GREEN}{count}{Fore.RESET}")
                if count == 1:
                    print(f" [{Fore.CYAN}+{Fore.RESET}] RNG: Get out")
                elif count <= 1000:
                    print(f" [{Fore.CYAN}+{Fore.RESET}] RNG: Damn you lucky!")
                elif count <= 5000:
                    print(f" [{Fore.CYAN}+{Fore.RESET}] RNG: Damn not bad!")
                elif count <= 10000:
                    print(f" [{Fore.CYAN}+{Fore.RESET}] RNG: You alright I guess.")
                elif count <= 30000:
                    print(f" [{Fore.CYAN}+{Fore.RESET}] RNG: Meh")
                elif count <= 50000:
                    print(f" [{Fore.CYAN}+{Fore.RESET}] RNG: Trash ahh luck")
                elif count >= 50000:
                    print(f" [{Fore.CYAN}+{Fore.RESET}] RNG: I don't think shiny hunting is for you lil bro LMAOOOO")
                break

        again = input()
        if again != "":
            break

    return count

def main():
    try:
        os.system("cls")
        os.system("title PokeMMO RNG tester!")
        print(f'''{Fore.CYAN}
                                            ┏━━━┓┏━┓━┏┓┏━━━┓┏┓
                                            ┃┏━┓┃┃┃┗┓┃┃┃┏━┓┃┃┃
                                            ┃┗━┛┃┃┏┓┗┛┃┃┃━┗┛┃┃
                                            ┃┏┓┏┛┃┃┗┓┃┃┃┃┏━┓┗┛
                                            ┃┃┃┗┓┃┃━┃┃┃┃┗┻━┃┏┓
                                            ┗┛┗━┛┗┛━┗━┛┗━━━┛┗┛
                          [>] An RNG luck tester specified for the game PokeMMO       
            
            [>] If you liked this tool, be sure to star it on my github page: github.com/6vns
            ╔══════════════════════════════════════════════════════════════════════════════╗{Fore.RESET}
            {Fore.CYAN}║{Fore.RESET} [{Fore.CYAN}1{Fore.RESET}] Random IV generator                                                      {Fore.CYAN}║{Fore.RESET}
            {Fore.CYAN}║{Fore.RESET} [{Fore.CYAN}2{Fore.RESET}] Shiny encounter simulator                                                {Fore.CYAN}║{Fore.RESET}
            {Fore.CYAN}║{Fore.RESET} [{Fore.CYAN}3{Fore.RESET}] {Fore.RED}Exit program{Fore.RESET}                                                             {Fore.CYAN}║{Fore.RESET}
            {Fore.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}
        ''')
        
        choice = input(f" [{Fore.CYAN}+{Fore.RESET}] Enter an option: ")
        if choice == "1":
            iv_gen()
        elif choice == "2":
            result = shiny_gen()
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] Number of encounters: {result}")
        elif choice == "3":
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] Thanks for using RNG!")
            sys.exit()
        elif choice == "exit":
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] Thanks for using RNG!")
            sys.exit()
        else:
            print(f" '{choice}' aint an option lil bro.")
            print(f"\n [{Fore.CYAN}+{Fore.RESET}] RNG: {Fore.CYAN}Taking you back to the main menu in 2 seconds...{Fore.RESET}")
            time.sleep(2)
            main()
            
    except KeyboardInterrupt:
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        main()