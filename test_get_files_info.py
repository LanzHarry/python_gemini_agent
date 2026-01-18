from functions.get_files_info import get_files_info

test_cases = (("calculator", "."), 
              ("calculator", "pkg"), 
              ("calculator", "/bin"),
              ("calculator", "../"))

def run_test_cases(test_cases, func_to_test):
    for case in test_cases:
        if case[1] == ".":
            dir_label = "current"
        else:
            dir_label = f"'{case[1]}'"
        print(f"Result for {dir_label} directory:")
        print(func_to_test(case[0], case[1]))

def main():
    run_test_cases(test_cases, get_files_info)

if __name__ == "__main__":
    main()
