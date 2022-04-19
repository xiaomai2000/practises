class TestClassAssert():
    
    value = 1

    def test_m1(self):
        self.value = 2
        assert self.value == 2

    def test_m2(self):
        self.value = 3
        assert self.value == 4

        
