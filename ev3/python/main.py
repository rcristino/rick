#!/usr/bin/env python3
from classes.Motor import Motor
from time import sleep

def main():
    print("RICK starting")

    mLeft = Motor("outA")
    mRight = Motor("outD")

    mLeft.moveTime(500, 10000)
    mRight.moveTime(500, 10000)

    mLeft.wait()
    mRight.wait()

    mLeft.stop()
    mRight.stop()

    sleep(5) # check if wheels are released

    mLeft.stopRelax()
    mRight.stopRelax()

    print("RICK stopping")


if __name__ == "__main__":
    main()