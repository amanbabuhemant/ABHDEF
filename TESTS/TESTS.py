class Test:
    def __init__(self, function):
        self.passed = 0
        self.failed = 0
        self.function = function

    def sfill(self, obj, n=0):
        if n and n > len(str(obj)):
            return str(obj) + " " * (n - len(str(obj)))
        n += 4
        return self.sfill( obj, n)


    def load_test(self):
        try:
            exec("from ." + self.function.__name__ + " import TESTCASES as TC", globals(), locals())
            TESTCASES = locals()["TC"]
        except ImportError:
            return None
        return TESTCASES

    def run_tests(self):
        test_cases = self.load_test()
        if not test_cases:
            print("No testcases found for function", self.function.__name__)
            return None

        testno = 0
        print("Test", "Status", "Arguments             ", "Expected", "Returnd", sep="\t")
        for test_case in test_cases:
            testno += 1
            function_return = self.function(*test_case["positional"], **test_case["keyword"])
            if test_case["return"] == function_return:
                self.passed += 1
                status = "\033[32mPassed\033[0m"
            else:
                self.failed += 1
                status = "\033[31mFailed\033[0m"
            print(
                self.sfill(testno, 4),
                status,
                self.sfill(test_case["positional"]),
                test_case["keyword"],
                self.sfill(test_case["return"], 8),
                self.sfill(function_return, 8),
                sep="\t"
            )
        print("\nPassed ", self.passed, "out of ", self.failed + self.passed)

