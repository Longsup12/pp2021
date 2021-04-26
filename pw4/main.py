from output import *
import curses


def main(stdscr):
    system(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)