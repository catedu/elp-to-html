import os
import sys

EXES = str(os.getcwd() + "/exes")


def list_of_chapters(folder):
    elps = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".elp"):
                elps.append({"folder": root, "file": file})
    return elps


def generate_html(elps):
    for item in elps:
        elp_file_path = os.path.join(item["folder"], item["file"])
        html_folder_path = item["folder"].replace("/exes/", "/htmls/")
        try:
            os.mkdir(html_folder_path)
        except:
            pass
        html_file_path = os.path.join(html_folder_path, item["file"][:-4])
        os.system(f"exe_do -s style=base -w {elp_file_path}")
        os.system(f"exe_do -x website {elp_file_path} {html_file_path} -f")


if __name__ == "__main__":
    elps = list_of_chapters(EXES)
    generate_html(elps)
