import os
import sys

EXES = str(os.getcwd() + "/exes")

def number_of_chapters(folder):
    elps = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".elp"):
                elps.append({'folder':})
    elps.sort()
    return elps


def generate_html(elps):
    for i in range(len(elps)):
        os.system("exe_do -s style=base -w exes/" + elps[i])
        os.system(
            "exe_do -x website exes/" + elps[i] + " exes/Modulo_" + str((i + 1)) + " -f"
        )

        # os.system('exe_do -s style=base -w exes/' + elps[i])
        # os.system('exe_do -x website exes/' + elps[i] + ' exes/Modulo_' + str((i+1)) + ' -f')


if __name__ == "__main__":
    elps = number_of_chapters(EXES)
    generate_html(elps)
