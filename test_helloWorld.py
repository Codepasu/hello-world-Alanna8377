import io
import sys

from answer import solution

def test_solution():
    buffer = io.StringIO()
    old_std_out = sys.stdout
    sys.stdout = buffer
    try:
        solution()
    except:
        sys.stdout = old_std_out
    
    output = buffer.getvalue().strip()
    assert output == "Hello World!"


if __name__ == "__main__":
    test_solution()
