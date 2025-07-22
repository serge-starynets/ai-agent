from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def test():
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for pkg/does_not_exist.py:")
    print(result)

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for lorem.txt:")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for pkg/morelorem.txt:")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for /tmp/temp.tx:")
    print(result)

    result = run_python_file("calculator", "main.py")
    print("Result for main.py:")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for main.py 2:")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result for tests.py:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result for ../main.py:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for nonexistent.py:")
    print(result)


if __name__ == "__main__":
    test()