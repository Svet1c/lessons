# task 1 = done
import time


class TrafficLight:
    __color = ''

    def running(self, count):
        while count:
            time.sleep(7)
            self.__color = 'red'
            print(f"TrafficLight show {self.__color}")
            time.sleep(2)
            self.__color = 'yellow'
            print(f"TrafficLight show {self.__color}")
            time.sleep(5)
            self.__color = 'green'
            print(f"TrafficLight show {self.__color}")
            count -= 1


if __name__ == "__main__":
    a = TrafficLight()
    a.running(count=int(input("enter num: ")))