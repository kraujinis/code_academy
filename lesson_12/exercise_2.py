# Sukurkite funkciją, kuri apimtų visą klaidų tvarkymo ciklą
# (try/except/else/finally) su realaus pasaulio scenarijaus
# pavyzdžiu.

def count_chickens(chickens_buys: int, chickens_sells: int) -> None:
    try:
        our = chickens_buys + chickens_sells

    except TypeError as e:
        print(f"Error: {e}")
    else:
        print(f"Our chickens in farm: {our} ")

    finally:
        print("We growing chickens!")


count_chickens(chickens_buys=10, chickens_sells='ds')
