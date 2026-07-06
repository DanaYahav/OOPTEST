from cat import Cat
from fish import Fish
from spider import Spider


def main():

    cat = Cat("Kitty")

    fish = Fish()
    fish.set_name("Nemo")

    spider = Spider()

    print(cat)
    cat.play()
    cat.walk()
    cat.eat()

    print()

    print(fish)
    fish.play()
    fish.walk()
    fish.eat()

    print()

    print(spider)
    spider.walk()
    spider.eat()

if __name__ == "__main__":
    main()