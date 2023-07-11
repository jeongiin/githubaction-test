# https://docs.pytest.org/en/7.4.x/

# content of test_sample.py
def inc(x):
    # 함수를 정답(test 예상 결과값)에 맞게 고쳐야 함
    return x + 1


def test_answer():
    assert inc(3) == 5
