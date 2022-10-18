from task03 import calc_dragon_heads

def main():
    age = int(input("Imput dragon age: "))

    head = calc_dragon_heads(age)

    msg = f"Dragon witn {age} years has {head} heads"

    print(msg)
    if __name__ == "__main__":
        main()