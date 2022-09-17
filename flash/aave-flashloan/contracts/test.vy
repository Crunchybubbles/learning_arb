# @version 0.3.3



numb: uint256

@external
def get_numb() -> (uint256):
    return self.numb

@external
def set_numb(new_numb: uint256):
    self.numb = new_numb
